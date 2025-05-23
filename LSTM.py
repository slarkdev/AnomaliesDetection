import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from pandas.plotting import register_matplotlib_converters
from sklearn.preprocessing import StandardScaler

from google.colab import drive
drive.mount('/content/drive')

import os
import pandas as pd

# Definir la carpeta principal que contiene las 9 carpetas
directorio_principal = "./drive/MyDrive/3w-dataset-reales/"

# Lista para almacenar nombres de archivos encontrados
archivos_encontrados = []

# Iterar sobre las 9 carpetas dentro del directorio principal
for carpeta in os.listdir(directorio_principal):
    ruta_carpeta = os.path.join(directorio_principal, carpeta)

    if os.path.isdir(ruta_carpeta) and "3" not in carpeta and "4" not in carpeta:
        # Buscar archivos dentro de la carpeta que comiencen con 'WELL-0000' y tengan extensión .csv
        archivos = [f for f in os.listdir(ruta_carpeta) if f.startswith("WELL-00002") and f.endswith(".csv")]

        # Guardar archivos con su ruta completa
        archivos_encontrados.extend([os.path.join(ruta_carpeta, f) for f in archivos])

# Convertir la lista en un DataFrame de Pandas
df_archivos = pd.DataFrame(archivos_encontrados, columns=["Ruta de Archivo"])

df_archivos



