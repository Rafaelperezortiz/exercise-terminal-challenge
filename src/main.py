# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV
import os
import time
import pandas as pd

tabla = "/workspaces/exercise-terminal-challenge"

#columnas
nombre =[]
tamaño = []
fecha = []

for root, dirs, files in os.walk(tabla):
   for archivo in files:
      ruta_completa = os.path.join(root, archivo)
      nombre.append(archivo)
      tamaño.append(os.path.getsize(ruta_completa))  # Cambio de "pesos" a "peso_archivo"
      fecha.append(os.path.getmtime(ruta_completa)) 

data = {
   "Nombre:": nombre,
   "Tamaño:": tamaño,
   "Última modificación:": fecha,
}
df = pd.DataFrame(data)
#comando to_datetime para convertir el getmtime que nos lo da en segundos convertirlo a fecha,.
df["Última modificación:"] = pd.to_datetime(df["Última modificación:"], unit='s')
print(df)