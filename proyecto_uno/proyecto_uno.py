import pandas as pd

df_medals = pd.read_csv('medallas.csv')

# Analizamos el DF ****************
# df_medallas.info()
# print(df_medallas.isnull().sum())

# Remplazamos NaN by 0 ****************
df_medals.fillna(0, inplace=True)

# Convertimos a int ****************
cols = ['Oro', 'Plata', 'Bronce']
df_medals[cols] = df_medals[cols].astype(int)

# Obtenemos el top3 de Medallas de Oro ****************
df_top3_gold = df_medals.sort_values(by='Oro', ascending=False).head(3)
print(f'Lo 3 pasise con mas medallas de Oro fueron:\n {df_top3_gold}\n')

# Obtenemos todos los paises con mas de 10 medallas de oro ****************
condition = df_medals['Oro'] > 10
more_10_gold_medals =  df_medals[condition].sort_values('Total', ascending=False)
print(f'Los paises con mas de 10 medallas de Oro son:\n {more_10_gold_medals}\n')

# Analizamos variables y parametros ****************
print(df_medals.describe())