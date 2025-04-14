# 🚌 Proyecto de Agrupamiento de Estaciones de TransMilenio

Este proyecto aplica técnicas de **aprendizaje automático no supervisado** para analizar y agrupar las estaciones del sistema de transporte masivo **TransMilenio** en Bogotá, Colombia, usando sus coordenadas geográficas.

---

## 📚 Objetivos

- Identificar y estructurar fuentes de datos relevantes al transporte masivo.
- Aplicar técnicas de **clustering** (agrupamiento) como **K-Means** y **DBSCAN**.
- Visualizar los resultados usando reducción de dimensionalidad con **PCA**.
- Mostrar el análisis mediante un **notebook interactivo** en Python.

---

## 🗂️ Estructura del repositorio


---

## 💾 Fuente de datos

- **Nombre:** `Estaciones_Troncales_de_TRANSMILENIO.geojson`
- **Formato:** GeoJSON
- **Contenido:** Información geográfica de las estaciones, incluyendo nombre, latitud y longitud.

---

## 🧪 Librerías necesarias

Para ejecutar el proyecto, necesitas instalar las siguientes librerías de Python:

```bash
pip install pandas geopandas matplotlib scikit-learn
▶️ Cómo ejecutar
Asegúrate de tener el archivo GeoJSON en la misma carpeta que el notebook.

Abre y ejecuta el notebook transmilenio_clustering.ipynb en Jupyter Notebook o Google Colab.

El código cargará los datos, extraerá las coordenadas y aplicará los modelos de agrupamiento.

Se mostrarán gráficos con los resultados obtenidos.
