import mysql.connector


conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")


"""cursor1=conexion1.cursor()
sql="insert into articulos(descripcion, precio) values (%s,%s)"
datos=("naranjas", 23.50)
cursor1.execute(sql, datos)
conexion1.commit()"""

cursor1=conexion1.cursor()
cursor1.execute("select descripcion from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()  