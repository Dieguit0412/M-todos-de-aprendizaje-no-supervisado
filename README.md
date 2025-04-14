🚌 Proyecto de Agrupamiento de Estaciones de TransMilenio
Este proyecto aplica técnicas de aprendizaje automático no supervisado para analizar y agrupar las estaciones del sistema de transporte masivo TransMilenio en Bogotá, Colombia, usando sus coordenadas geográficas.

📚 Objetivos
Identificar y estructurar fuentes de datos relevantes al transporte masivo.

Aplicar técnicas de clustering (agrupamiento) como K-Means y DBSCAN.

Visualizar los resultados usando reducción de dimensionalidad con PCA.

Mostrar el análisis mediante un notebook interactivo en Python.

🗂️ Estructura del repositorio
bash
Copiar
Editar
transmilenio-clustering/
│
├── Estaciones_Troncales_de_TRANSMILENIO.geojson   # Fuente de datos
├── transmilenio_clustering.ipynb                  # Notebook con el análisis completo
├── README.md                                      # Descripción del proyecto
💾 Fuente de datos
Nombre: Estaciones_Troncales_de_TRANSMILENIO.geojson

Formato: GeoJSON

Contenido: Información geográfica de las estaciones, incluyendo nombre, latitud y longitud.

🧪 Librerías necesarias
Para ejecutar el proyecto, necesitas instalar las siguientes librerías de Python:

bash
Copiar
Editar
pip install pandas geopandas matplotlib scikit-learn
▶️ Cómo ejecutar
Asegúrate de tener el archivo GeoJSON en la misma carpeta que el notebook.

Abre y ejecuta el notebook transmilenio_clustering.ipynb en Jupyter Notebook o Google Colab.

El código cargará los datos, extraerá las coordenadas y aplicará los modelos de agrupamiento.

Se mostrarán gráficos con los resultados obtenidos.

📊 Resultados obtenidos
Se aplicaron dos algoritmos de clustering:

K-Means: agrupó las estaciones en clústeres definidos por cercanía.

DBSCAN: detectó agrupaciones de estaciones sin necesidad de indicar el número de clústeres.

PCA: permitió proyectar los datos a 2 dimensiones para visualización.
