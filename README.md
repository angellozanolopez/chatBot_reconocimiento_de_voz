# chatBot_reconocimiento_de_voz

Chat inteligente por voz capaz de reconocer peticiones y dar respuestas totalmente coherentes también por voz.

## Formación en asistentes virtuales (chatbots)

## Introducción

La mayoría de empresas reciben centenares de consultas por parte de sus clientes. En muchos casos, hasta el 80% de estas consultas son repetitivas. Los chatbots permiten automatizar estas consultas, proporcionando respuestas de forma desatendida y reduciendo costos operativos. Esto permite a las empresas atender a más clientes sin necesidad de ampliar su plantilla. ¡Genial, verdad?

## Ejercicio

El ejercicio consiste en la creación de un sistema de inteligencia artificial que responda automáticamente a las consultas de los clientes. Se desarrollará un chatbot que recibirá preguntas de los usuarios y ofrecerá respuestas predefinidas. En caso de no poder responder o si se detecta una incidencia, el usuario será informado de que un humano tomará el control.

Es importante destacar que una misma consulta puede formularse de distintas maneras. Esto incluye:

- Errores ortográficos.
- Uso de sinónimos o diferentes formas de expresar una misma idea.

Ejemplos:

- "¿Cuántos meses de garantía dais?"
- "¿Cuánto dura la garantía?"
- "¿Qué plazo de soporte y corrección de errores posterior ofrecéis?"

La respuesta debe ser lo más humana posible, evitando formatos rígidos como "12 meses", y utilizando respuestas más naturales como "Te confirmo que nuestro período de garantía es de 12 meses, aunque estamos seguros de que quedarás completamente satisfecho con el servicio".

El chatbot puede desarrollarse con cualquier interfaz de ejecución, ya sea una interfaz gráfica o una línea de comandos.

## Ejemplo de Preguntas y Respuestas

- **Plazo de garantía** → 12 meses
- **Plazo de puesta en marcha del servicio** → 6 meses
- **Precio del servicio** → 30€ mensuales
- **Años de experiencia de la empresa** → Más de 25 años

Formación en asistentes virtuales (chatbots)

## Introducción

La mayoría de empresas reciben centenares de consultas por parte de sus clientes. La mayoría (en algunos casos hasta el 80%) son siempre las mismas, y esto es un hecho. Los chatbots logran automatizar este tipo de consultas, dándoles respuesta de forma desatendida, lo cual reporta una reducción de costes para las empresas. Esto permitirá a las empresas dar soporte a más clientes sin necesariamente ampliar su plantilla de trabajadores, ¿genial, verdad?

## Ejercicio

El ejercicio consiste en la creación de un sistema de inteligencia artificial para dar respuesta a sus clientes de forma automatizada. Se creará un chatbot quien recibirá las preguntas por parte de los usuarios, y les dará las respuestas predefinidas que correspondan. En caso de incidencia o de no obtener la respuesta esperada, el usuario recibirá un mensaje conforme le atenderá un humano (y el ejercicio terminará aquí).

Es importante destacar que la misma consulta puede realizarse de diferentes maneras, esto significa:

- Faltas ortográficas
- Uso de sinónimos o formas diferentes de pedir la información, ejemplo:
  - ¿Cuántos meses de garantía dáis?
  - ¿Cuánto dura la garantía?
  - ¿Qué plazo de soporte y corrección de errores posterior ofrecéis?
  - ...

La respuesta debe ser lo más humana posible, evitando dar respuestas del estilo de "12 meses" sino más bien "Te confirmo que nuestro periodo de garantía es de 12 meses, aunque ¡estamos seguros de que el resultado será muy satisfactorio!".

Para crear el chatbot, se partirá de las siguientes preguntas y respuestas (esquematizadas, siéntete libre de adornar las respuestas para hacerlas humanas):

- **Plazo de garantía** → 12 meses
- **Plazo de puesta en marcha del servicio** → 6 meses
- **Precio del servicio** → 30€ mensuales
- **Años de experiencia de la empresa** → Más de 25 años

Puedes decidir cómo será la interfaz de ejecución del chatbot. No debe ser necesariamente una interfaz con un avatar que "hable", sino que puede ser por línea de comandos sin problema.

Siéntete libre de usar la tecnología que te sea más cómoda, o incluso probar varias de ellas.

## Entregable 1

Repasa los entregables de este ejercicio para realizar el siguiente informe: análisis de tecnologías existentes y, si llevan coste asociado, pantallazo de dicho coste. Se dará prioridad a las tecnologías open source que no lleven costes asociados.

En base a ello, se decidirá por la tecnología a usar y se procederá al desarrollo de la solución.

## Entregable 2

(en un único WeTransfer):
1. Código fuente de la solución
2. Video explicativo del código fuente (máximo 3 minutos)
3. Video mostrando e interpretando los resultados (máximo 2 minutos)

## Entregable 3

Adaptar sistema speech-to-text para que el AV reciba un input de voz humana, y un sistema text-to-speech para que el AV dé respuesta con voz sintetizada lo más humana posible.

Video demostrativo.

## SOLUCIÓN

### Entregable 1: Análisis de tecnologías y costos asociados

El desarrollo de un chatbot inteligente para responder consultas implica el uso de diversas tecnologías esenciales:

1. **Lenguaje de Programación y Entorno de Desarrollo**:
   - **Python**: Su amplia comunidad, versatilidad y variedad de bibliotecas lo convierten en la elección ideal. Puede utilizarse en entornos como Jupyter Notebooks o IDEs como VSCode para construir el chatbot.

2. **Librerías para Procesamiento de Texto y Respuestas**:
   - **re (Regular Expressions)**: Para el procesamiento de texto, búsqueda y separación de palabras clave.
   - **json**: Facilita el manejo de los datos de preguntas y respuestas del chatbot.
   - **random**: Para generar respuestas variadas y aleatorias.

3. **Algoritmos de Similitud y Procesamiento de Texto**:
   - **Levenshtein**: Útil para calcular la similitud entre palabras o frases, permitiendo comprender variantes ortográficas o preguntas similares pero formuladas de manera diferente.

4. **Reconocimiento de Voz y Texto a Voz**:
   - **speech_recognition (SpeechRecognition)**: Permite reconocer y transcribir audio a texto.
   - **pyttsx3 (pyttsx)**: Ofrece funcionalidades de síntesis de voz para convertir texto en voz humana.

5. **Costos Asociados**:
   - La mayoría de estas tecnologías son de código abierto y no tienen costos asociados. Sin embargo, algunas plataformas de reconocimiento de voz pueden ofrecer planes de pago para funcionalidades avanzadas.

Dado que se priorizan tecnologías open source sin costos asociados, el uso de bibliotecas como `re`, `json`, `random`, `Levenshtein`, `speech_recognition` y `pyttsx3` es una elección sólida para desarrollar este chatbot inteligente.

### Entregables 2 y 3

### 📹 Video y Demostración

🔹 [![Ver en YouTube](https://img.shields.io/badge/🎥%20Código-red?logo=youtube&logoColor=white)](https://youtu.be/b-FszsXSLag)  
<br>
🔹 [![Ver en YouTube](https://img.shields.io/badge/🎥%20Demostración-red?logo=youtube&logoColor=white)](https://youtu.be/K28Eb5GW18Q)

📌 *Haz clic con el botón derecho encima del botón y selecciona "Abrir enlace en una nueva pestaña" para no salir del repositorio.*


