import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json
from tensorflow.keras.applications.resnet50 import preprocess_input

# Configuración de la página
st.set_page_config(page_title="Clasificador de Tenis (Adidas, Converse, Nike)", page_icon="👟")

# Paso 1: Carga del modelo y mapeo de clases
@st.cache_resource
def load_assets():
    # Cargamos el modelo final que descargamos de Colab
    model = tf.keras.models.load_model('modelo_tenis_final.keras')
    
    # Cargamos el mapeo de clases para que los índices coincidan perfectamente
    with open('clases.json') as f:
        class_indices = json.load(f)
    
    # Invertimos el diccionario para obtener el nombre a partir del índice
    idx_to_class = {v: k for k, v in class_indices.items()}
    return model, idx_to_class

try:
    modelo, idx_to_class = load_assets()
except Exception as e:
    st.error(f"Error al cargar los archivos del modelo: {e}")
    st.stop()

# Interfaz de usuario
st.title('👟 Clasificador de Marcas de Tenis')
st.markdown("""
Esta aplicación utiliza **Deep Learning (ResNet50)** para identificar la marca de tus tenis. 
Actualmente reconoce: **Adidas, Converse y Nike**.
""")

st.write("---")

# Paso 2: Subida de imagen
uploaded_file = st.file_uploader('Elige una foto de tu tenis...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Crear dos columnas para una mejor visualización
    col1, col2 = st.columns(2)

    # Procesar la imagen
    image = Image.open(uploaded_file).convert('RGB')
    
    with col1:
        st.subheader("Imagen subida")
        st.image(image, use_container_width=True)
    
    # Paso 3: Preprocesamiento (IDÉNTICO al entrenamiento)
    IMG_SIZE = 160  
    img_resized = image.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img_resized)
    
    # Aplicar el preprocesamiento específico de ResNet50
    img_preprocessed = preprocess_input(img_array)
    img_batch = np.expand_dims(img_preprocessed, axis=0)
    
    # Realizar la predicción
    with st.spinner('Analizando marca...'):
        pred = modelo.predict(img_batch, verbose=0)[0]
    
    with col2:
        st.subheader("Resultados:")
        
        # Ordenar las predicciones de mayor a menor probabilidad
        sorted_indices = pred.argsort()[::-1]
        
        for idx in sorted_indices:
            nombre = idx_to_class[idx].title()
            prob = pred[idx]
            
            # Mostrar nombre y porcentaje
            st.write(f"**{nombre}**: {prob:.1%}")
            # Mostrar barra de progreso
            st.progress(float(prob))
            
        # Resaltar la predicción ganadora
        ganador = idx_to_class[sorted_indices[0]].upper()
        st.success(f"La marca predominante parece ser: **{ganador}**")

st.write("---")
st.caption("Proyecto de Transfer Learning con ResNet50 | Desarrollado como parte del curso de Python.")
