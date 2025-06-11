import  mysql. connector

conexion = mysql. connector.connect(
    host="bdjew5xlyifck9roeblc-mysql.services.clever-cloud.com",
    user="u8nhux30tduyteyh",
    password="CDg9llSM5my9q06yAfJd",
    database="bdjew5xlyifck9roeblc"
)

if conexion.is_connected():
    print("Conexión exitosa")