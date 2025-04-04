import pandas as pd

# Leemos los archivos CSV *********************
df_ventas1 = pd.read_csv('Datos_Ventas_Tienda.csv')
df_ventas2 = pd.read_csv('Datos_Ventas_Tienda2.csv')

# Concatenamos los DF *********************
df_ventas = pd.concat([df_ventas1, df_ventas2], ignore_index=True)

# Convertimos el texto a fecha
df_ventas['Fecha'] = pd.to_datetime(df_ventas['Fecha'], errors='coerce')
# print('Hay valores NAT?:', df_ventas.isna().any())

# Analizamos su estructura *********************
# df_ventas.info()
# print(df_ventas.isnull().sum())
# print(df_ventas.head(1))

# Agrupar por categoria de productos *********************
df_categoria  = df_ventas.groupby(['Producto'])[['Cantidad', 'Total Venta']].sum().reset_index()
df_categoria = df_categoria.rename(columns={'Cantidad': 'Cantidad'}).sort_values(by='Cantidad', ascending=False)

# Analizamos las ventas *********************
print(f'Cantidad de productos por categoria: \n {df_categoria}\n')

# Cual es el producto mas vendido? *********************
producto_mas_vendido = df_categoria.head(1)
print(f'El producto mas vendido es:\n {producto_mas_vendido}\n')

# Cual es el mes con mas ventas? *********************
mes_mas_ventas = df_ventas.groupby(df_ventas['Fecha'].dt.to_period('M'))['Total Venta'].sum().reset_index()
mes_mas_ventas = mes_mas_ventas.rename(columns={'Total Venta': 'Total $'})
mes_mas_ventas = mes_mas_ventas.sort_values(by='Total $', ascending=False).head(1)
print(f'El mes con mas ventas es:\n {mes_mas_ventas}\n')

# Agregamos el mes con mas ventas al DF y lo almacenamos en un .csv *********************
df_ventas['Meses'] = df_ventas['Fecha'].dt.month
df_ventas.to_csv('proyecto_dos.csv')
# print(df_ventas)

