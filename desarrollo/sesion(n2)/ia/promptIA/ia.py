# 📦 Importa módulos necesarios para configuración y conexión con la API
import os
from dotenv import load_dotenv                      # Para cargar variables de entorno desde un archivo .env
from google.generativeai import configure, GenerativeModel  # SDK oficial para interactuar con Gemini

# ✅ Cargar variables de entorno desde el archivo .env
# Esto permite acceder a la clave de API sin exponerla directamente en el código
load_dotenv()

# 🔐 Configura la API de Gemini usando la clave almacenada en la variable de entorno GEMINI_API_KEY
configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Inicializa el modelo específico de Gemini que se va a usar
# "gemini-2.5-flash-lite" es una versión rápida y eficiente, ideal para respuestas ágiles
model = GenerativeModel(model_name="gemini-2.5-flash-lite")

# 🧠 Función principal que envía una pregunta a la IA y devuelve la respuesta
def api_ia(query):
    try:
        # 📝 Prompt especializado que define el comportamiento deseado de la IA
        # Le indica que debe resolver problemas algorítmicos en Python, explicar el razonamiento,
        # comentar el código y mostrar resultados entendibles en consola
        prompt = """
Resuelve el siguiente problema algorítmico en Python:

Implementa un grafo con costos en las aristas (los costos pueden ser generados aleatoriamente).
Escoge un nodo de inicio y un nodo final, e implementa:

1. El algoritmo de Dijkstra.
2. El algoritmo A* (A-Star).

Tu respuesta debe incluir obligatoriamente:
1. Explicación clara del enfoque: cómo se representa el grafo y cómo funcionan Dijkstra y A*.
2. El código completo en Python con ambas implementaciones.
3. Comparación de los caminos encontrados y sus costos.
4. Ejemplo de ejecución en consola mostrando los resultados de ambos algoritmos.
5. Comentarios dentro del código explicando los pasos importantes.

No uses JSON, ni envoltorios como "success", "result", "status" o "data".  
La salida debe estar en texto plano y Python comentado.
        """.strip()

        # 🚀 Envía el prompt + la pregunta del usuario al modelo Gemini
        # La IA genera una respuesta basada en el contexto y las instrucciones del prompt
        response = model.generate_content(f"{prompt}\n\nAcción:\n{query}")

        # 🧾 Extrae el texto plano de la respuesta generada por la IA
        response_text = response.text.strip()

        # ✅ Devuelve la respuesta final al llamador (por ejemplo, main.py)
        return response_text

    # ⚠️ Manejo de errores si ocurre algún problema durante la conexión o generación
    except Exception as e:
        print("❌ Error en la API de Gemini:", str(e))
        return {
            "type": "error",
            "data": "Error al procesar la pregunta con la IA.",
            "error": str(e),
        }