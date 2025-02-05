# CARGAR LIBRERIAS
import re # Manipulación de expresiones regulares.
import os # Funciones para interactuar con el sistema operativo.
import sys # Interacción con variables y funciones del intérprete.
import json # Procesamiento de datos en formato JSON.
import random # Generación de números aleatorios.
import pyttsx3 # Síntesis de voz para texto.
import Levenshtein # Cálculo de distancias entre cadenas de texto.
import speech_recognition as sr # Reconocimiento de voz.
from unidecode import unidecode # Conversión de caracteres Unicode a ASCII.

data = {}  # Definimos data fuera de las funciones para hacerlo accesible en todo el programa
# ------------------------------------------------------------------------------------------------------------------
# CARGAR ARCHIVO EXTERNO DE PREGUNTAS Y RESPUESTAS
# Todas las preguntas y las respuestas del chat-bot se encuentran en un archivo independiente llamado responses.json
# Esto permite que podamos ajustar, cambiar o agregar nuevas interacciones al chat sin tener que tocar el código principal. 
# En lugar de modificar el código, simplemente editamos este archivo externo, lo que facilita mucho la tarea de gestionar 
# y expandir el vocabulario del chat.
def load_data():
    global data
    print("Directorio actual:", os.getcwd())
    with open('./responses.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

# ------------------------------------------------------------------------------------------------------------------
# FORMATEAR PREGUNTA DEL USUARIO Y RESPUESTA DEL BOT
# Esta funcion procesa la entrada del usuario para asegurarse de que está 
# formateada de manera uniforme y eliminando tildes. Divide el mensaje en palabras individuales, 
# busca una respuesta adecuada utilizando la función check_all_messages(), y normaliza la respuesta antes de devolverla. 
# Si no se proporciona una entrada válida, solicita al usuario que repita su mensaje.
def get_response(user_input):
    if user_input is not None:
        # Eliminar tildes
        normalized_input = unidecode(user_input)
        split_message = re.split(r'\s|[,:;.?!-_]\s*', normalized_input.lower())
        response = check_all_messages(split_message)
        normalized_output = unidecode(response)     
        return normalized_output
    else:
        print("No entendi bien que dijiste. Permiteme ponerte en contacto con Atencion al Cliente...")        

# ------------------------------------------------------------------------------------------------------------------
# CALCULAR LA PROBABILIDAD DEL MENSAJE SEGUN LAS PALABRAS CLAVE USADAS
# Esta funcion calcula la certeza de que un mensaje del usuario coincida con palabras clave conocidas. 
# Evalúa la cantidad de palabras reconocidas en el mensaje del usuario en comparación con las palabras clave conocidas. 
# Además, verifica si todas las palabras requeridas están presentes en el mensaje del usuario. 
# Luego, determina un porcentaje de coincidencia basado en estas comparaciones para determinar la probabilidad del mensaje. 
# Si todas las palabras requeridas están presentes o si se espera una sola respuesta, devuelve un porcentaje basado en 
# la cantidad de coincidencias; de lo contrario, devuelve 0.
def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    
# ------------------------------------------------------------------------------------------------------------------
# ENCONTRAR PALABRAS SIMILARES CUANDO NO SE ENCUENTRAN EN EL DICCIONARIO (Ola ---> Hola)
# Esta funcion busca una palabra similar a la palabra de entrada dentro de un conjunto de palabras clave. 
# Utiliza la métrica de similitud de Levenshtein para calcular qué palabra clave tiene la mayor similitud con 
# la palabra de entrada. El umbral define la similitud mínima requerida para que una palabra se considere similar. 
# Esta función retorna la palabra clave más similar encontrada en función de la métrica de similitud de Levenshtein.
def find_similar_word(input_word, keywords, threshold=0.7):
    max_similarity = 0
    similar_word = None

    for keyword in keywords:
        similarity = Levenshtein.ratio(input_word, keyword)
        if similarity > max_similarity and similarity >= threshold:
            max_similarity = similarity
            similar_word = keyword

    return similar_word

# ------------------------------------------------------------------------------------------------------------------
# FUNCION CLAVE QUE ENCUENTRA LA RESPUESTA MAS INDICADA EN BASE A LAS PALABRAS USADAS POR EL USUARIO
# Esta es la función clave que evalúa el mensaje del usuario para encontrar la mejor respuesta del chatbot.
# - Recopila todas las respuestas posibles del archivo de datos.
# - Calcula la probabilidad de cada respuesta en función de la similitud de las palabras clave entre el mensaje del usuario y las 
#   palabras clave asociadas a cada respuesta.
# - Encuentra la respuesta con la probabilidad más alta.
# - Si ninguna respuesta supera cierto umbral de probabilidad, busca una palabra similar y devuelve una respuesta relacionada si se 
#   encuentra una palabra clave similar.
# - Si no se encuentra una respuesta con alta probabilidad o una palabra clave similar, devuelve una respuesta predeterminada 
#   indicando que no comprende el mensaje del usuario.
def check_all_messages(split_message):
    highest_prob = {}
    responses = data.get('responses', [])
    
    keywords_list = [word for sublist in [resp['keywords'] for resp in responses] for word in sublist]

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(split_message, list_of_words, single_response, required_words)

    for resp in responses:
        response(resp['message'], resp['keywords'], single_response=False if 'single_response' not in resp else resp['single_response'], required_words=resp.get('required_words', []))

    best_match = max(highest_prob, key=highest_prob.get)

    if highest_prob[best_match] < 1:
        similar_word = find_similar_word(split_message[0], keywords_list)
        if similar_word:
            for resp in responses:
                if similar_word in resp['keywords']:
                    return resp['message']

    return best_match if highest_prob[best_match] >= 1 else unknown(' '.join(split_message))

# ------------------------------------------------------------------------------------------------------------------
# RESPUESTA CUANDO NO SE ENCUENTRA LA FRASE INDICADA (CUANDO EL BOT NO TE ENTIENDE)
# Esta funcion se activa cuando no se puede encontrar una respuesta adecuada para el mensaje del usuario.
# Genera respuestas predeterminadas aleatorias que sugieren una posible repetición si no comprende la solicitud.
# También registra el mensaje del usuario si no coincide con ninguna palabra clave conocida, 
# lo que permite agregar nuevas respuestas al archivo de datos para futuras interacciones.
def unknown(user_input):
    global data
    response = ['No entendi bien que dijiste. Te paso con uno de nuestros agentes', 'No estoy seguro de lo que quieres. Te paso con uno de nuestros agentes'][random.randrange(2)]
    if ' '.join(user_input.split()) not in [kw for resp in data['responses'] for kw in resp['keywords']]:
        save_unknown_response(user_input)           
    return response

# ------------------------------------------------------------------------------------------------------------------
# ANOTAR AQUELLAS PALABRAS O FRASES QUE EL BOT NO HA ENTENDIDO PARA SU POSTERIOR ANALISIS
# Esta funcion es responsable de registrar en un archivo todas las solicitudes que el bot no puede entender. 
# Guarda el mensaje del usuario en un archivo de texto llamado respuestas_desconocidas.txt. 
# Esto permite revisar más tarde esas solicitudes para mejorar las respuestas del bot o añadir nuevas respuestas al conjunto de datos.
def save_unknown_response(user_input):
    with open('respuestas_desconocidas.txt', 'a', encoding='utf-8') as file:
        file.write(user_input + '\n')

# ------------------------------------------------------------------------------------------------------------------
engine = pyttsx3.init() # Iniciar sintetizador de voz
engine.setProperty('rate', 150)  # Velocidad

# EJECUCION DEL CHATBOT
# Esta funcion ejecuta el chatbot de forma continua, tomando las entradas del usuario y produciendo respuestas. 
# Utiliza la biblioteca pyttsx3 para convertir el texto de las respuestas del bot en voz. 
# El ciclo se detiene si el usuario menciona "adiós".
def run_chatbot():
    load_data()  # Cargamos los datos al inicio
    while True:
        user_input = reconocimiento_voz()
        response = get_response(user_input)
        
        if response is not None:
            print("Bot: " + response)
            engine.say(response)
            engine.runAndWait()

        if user_input == 'adiós':
            print("¡Hasta luego!")
            return
        
# ------------------------------------------------------------------------------------------------------------------
# RECONOCIMIENTO DE VOZ PARA INTERACTUAR CON EL BOT
# Esta función, utiliza la biblioteca speech_recognition para escuchar el audio del micrófono y convertirlo a texto mediante 
# el servicio de reconocimiento de voz de Google. Si se reconoce el habla, imprime el texto en la consola y lo devuelve. 
# En caso de errores o cuando no se entiende lo que se dice, imprime un mensaje específico y devuelve None.
def reconocimiento_voz():
    # Crear un objeto de reconocimiento de voz
    recognizer = sr.Recognizer()

    # Utilizar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)

        try:
            # Reconocer el texto en español a partir del audio
            text = recognizer.recognize_google(audio, language="es-ES")
            print("Has dicho:", text)              
            return text        
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print("Error al solicitar el reconocimiento; {0}".format(e))
            return None

# ------------------------------------------------------------------------------------------------------------------

# PROGRAMA PRINCIPAL
# Este bloque de código verifica si el script se está ejecutando como el programa principal. 
# Si es así, realiza la limpieza de la consola y luego ejecuta la función principal run_chatbot(). 
# Finalmente, sys.exit() se utiliza para terminar completamente la ejecución del programa después 
# de que run_chatbot() haya finalizado su ejecución.
if __name__ == "__main__":
    os.system('cls')
    run_chatbot()  # Ejecutamos la función principal
    sys.exit()  # Salimos del programa después de run_chatbot()