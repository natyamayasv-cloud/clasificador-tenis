# Clasificador de Calzado Deportivo (Tenis) con Deep Learning

## Descripción
Este proyecto consiste en una aplicación web capaz de clasificar imágenes de tenis en tres marcas icónicas: Adidas, Converse y Nike. Utiliza una red neuronal convolucional basada en arquitectura de última generación para ofrecer predicciones en tiempo real a través de una interfaz sencilla y eficiente.

## Demo
🚀 **Puedes probar la aplicación aquí:** [https://clasificador-tenis-3cmpfgfpt7zggwmbss57bx.streamlit.app/](https://clasificador-tenis-3cmpfgfpt7zggwmbss57bx.streamlit.app/)

## Por qué este tema
Elegí este tema porque la identificación de productos y el reconocimiento de marcas es un pilar fundamental en la modernización de inventarios y el e-commerce. Trabajo en una emprea de Retail, entiendo que la automatización del registro de activos mediante visión artificial reduce errores manuales y optimiza la cadena de suministro.

## Dataset
- **Total de imágenes:** ~900 imágenes (distribuidas en entrenamiento, validación y prueba).
- **Clases:** Adidas, Converse, Nike.
- **Fuentes:** Dataset seleccionado de Kaggle especializado en calzado deportivo.

## Resultados
**Mejor Accuracy obtenido:** 72%

| Clase | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- |
| **Adidas** | 0.81 | 0.77 | 0.79 |
| **Converse** | 0.68 | 0.76 | 0.72 |
| **Nike** | 0.67 | 0.63 | 0.67 |

## Análisis de errores
El modelo presenta una precisión sobresaliente con **Adidas**, pero muestra mayor confusión con **Nike** (F1-score de 0.67).
- **Causa:** El logo de Nike ("Swoosh") es minimalista y puede confundirse con las curvas naturales del calzado de otras marcas si el ángulo de la foto no es el adecuado.
- **Converse:** Se clasifica con mayor éxito gracias a elementos distintivos como la puntera blanca y el parche circular.

## Aprendizajes
Lo más difícil fue gestionar el entorno de despliegue (Deployment). Aprendí que la compatibilidad entre versiones de Python (específicamente la transición a Python 3.11 para soportar TensorFlow) es crítica en proyectos de IA. Asimismo, la experiencia de migrar el modelo desde un cuaderno de Colab a una URL pública brindó una visión integral del ciclo de vida de una solución de software moderna (CI/CD), alineada con mis objetivos de preparar equipos autónomos y autogestionados.

## Tecnologías usadas
- **Lenguaje:** Python
- **IA:** TensorFlow / Keras (Framework principal)
- **Arquitectura:** Transfer Learning con **ResNet50**
- **Interfaz:** Streamlit
- **Deploy:** Streamlit Cloud vinculado a GitHub

## Autor
**Natalia Amaya**