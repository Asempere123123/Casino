import pandas as pd

# Leer los archivos CSV en dataframes
df1 = pd.read_csv("winrateplantarse.csv")
df2 = pd.read_csv("winratepedir.csv")

# Seleccionar solo las celdas a partir de la segunda fila y columna
df1 = df1.iloc[1:, 1:]
df2 = df2.iloc[1:, 1:]

# Crear una nueva tabla con las letras P o Q en función de la comparación
result = df1.where(df1 > df2, "Q").where(df1 <= df2, "P")

# Crear una lista de etiquetas de columna nueva para la tabla resultante
columns = df1.columns
result.columns = columns

# Agregar las etiquetas de fila de la tabla original
result.index = df1.index

# Guardar el resultado en un archivo CSV
result.to_csv("tabla_resultado.csv", index=False)