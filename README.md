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

### Entregable 2
### 📹 Video y Demostración
🔹 [![Ver en YouTube](https://img.shields.io/badge/🎥%20Código-red?logo=youtube&logoColor=white)](https://youtu.be/b-FszsXSLag)

🔹 [![Ver en YouTube](https://img.shields.io/badge/🎥%20Demostración-red?logo=youtube&logoColor=white)](https://youtu.be/K28Eb5GW18Q)
📌 *Haz clic con el botón derecho encima del botón y selecciona "Abrir enlace en una nueva pestaña" para no salir del repositorio.*
