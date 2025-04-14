import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# Cargar el archivo GeoJSON
file_path = r"C:\Users\user\OneDrive - Corporacion Universitaria Iberoamericana\Documentos\Inteligencia Artifical\trasmilenio-clustering\Estaciones_Troncales_de_TRANSMILENIO.geojson"
gdf = gpd.read_file(file_path)

# Imprimir las columnas para ver la estructura de datos
print(gdf.columns)

# Crear un diccionario con los nombres de las estaciones y sus coordenadas
coordenadas_estaciones = {
    row['nombre_estacion']: (row['latitud_estacion'], row['longitud_estacion'])
    for _, row in gdf.iterrows()
}

# Verificar las coordenadas
print(coordenadas_estaciones)

# Crear un DataFrame de ejemplo con los nombres de las estaciones
df = pd.DataFrame({
    'Origen': ['Portal 20 de Julio', 'Portal Américas']  # Cambia esto por tus estaciones reales
})

# Asignar las coordenadas al DataFrame
df["origen_coord"] = df["Origen"].map(coordenadas_estaciones)

# Mostrar el DataFrame con las coordenadas
print(df)

# Crear un DataFrame con combinaciones de rutas entre orígenes y destinos
orígenes = df['Origen'].tolist()
destinos = df['Origen'].tolist()

rutas = []
for origen in orígenes:
    for destino in destinos:
        if origen != destino:
            rutas.append({"Origen": origen, "Destino": destino})

df_rutas = pd.DataFrame(rutas)

# Asignar coordenadas a las rutas
df_rutas["origen_coord"] = df_rutas["Origen"].map(coordenadas_estaciones)
df_rutas["destino_coord"] = df_rutas["Destino"].map(coordenadas_estaciones)

# Eliminar filas sin coordenadas válidas
df_rutas = df_rutas.dropna(subset=["origen_coord", "destino_coord"])
print(f"Datos válidos después de asignar coordenadas: {len(df_rutas)}")

# Calcular el punto medio entre origen y destino
df_rutas["centro_lat"] = df_rutas.apply(lambda row: (row["origen_coord"][0] + row["destino_coord"][0]) / 2, axis=1)
df_rutas["centro_lon"] = df_rutas.apply(lambda row: (row["origen_coord"][1] + row["destino_coord"][1]) / 2, axis=1)

# Crear dataset para clustering
X = df_rutas[["centro_lat", "centro_lon"]].values

# Determinar el número óptimo de clusters (entre 2 y 5)
n_clusters = min(len(df_rutas) // 2, 5) if len(df_rutas) >= 4 else min(len(df_rutas), 2)

# 1. MÉTODO K-MEANS
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
df_rutas["cluster"] = kmeans.fit_predict(X)

# Visualizar resultados de K-Means
plt.figure(figsize=(10, 8))
colors = ["red", "blue", "green", "orange", "purple"]
for cluster in df_rutas["cluster"].unique():
    cluster_data = df_rutas[df_rutas["cluster"] == cluster]
    plt.scatter(cluster_data["centro_lon"], cluster_data["centro_lat"], 
                label=f"Grupo {cluster}", color=colors[cluster % len(colors)])

# Añadir todas las estaciones al mapa para referencia
for nombre, (lat, lon) in coordenadas_estaciones.items():
    plt.plot(lon, lat, 'ko', markersize=3)
    if len(nombre) < 15:  # Solo mostrar nombres cortos para no sobrecargar el gráfico
        plt.text(lon, lat, nombre, fontsize=7)

plt.title("Clustering K-Means de Rutas TransMilenio")
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("kmeans_clustering_estaciones.png")
plt.show()

# 2. MÉTODO DEL CODO Y ANÁLISIS DE SILUETA
# Determinar número óptimo de clusters usando el método del codo
distortions = []
silhouette_scores = []
range_n_clusters = range(2, min(11, len(X)))

for n_clusters in range_n_clusters:
    if len(X) > n_clusters:  # Verificar que hay suficientes datos
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)

        # Calcular coeficiente de silueta
        if n_clusters > 1 and n_clusters < len(X):
            labels = kmeans.labels_
            silhouette_avg = silhouette_score(X, labels)
            silhouette_scores.append(silhouette_avg)
            print(f"Para n_clusters = {n_clusters}, el coeficiente de silueta es: {silhouette_avg:.3f}")

# Gráfico del método del codo
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(range_n_clusters, distortions, 'bo-')
plt.xlabel('Número de clusters')
plt.ylabel('Distorsión (Inercia)')
plt.title('Método del Codo')
plt.grid(True)

# Gráfico del coeficiente de silueta
if len(silhouette_scores) > 0:
    plt.subplot(1, 2, 2)
    plt.plot(range_n_clusters[1:len(silhouette_scores)+1], silhouette_scores, 'ro-')
    plt.xlabel('Número de clusters')
    plt.ylabel('Coeficiente de silueta')
    plt.title('Análisis de Silueta')
    plt.grid(True)

plt.tight_layout()
plt.savefig("evaluacion_clustering_estaciones.png")
plt.show()
