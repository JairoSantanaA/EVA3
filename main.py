import mysql.connector as mysql
import bcrypt
import time

def conexion():
    try:    
        conexion = mysql.connect(
            host="127.0.0.1",
            user="root",
            password="Inacap.2024",
            database="banco"
        )

        if conexion.is_connected():
            print("Conectado a la base de datos.")
            return conexion  
        else:
            print("No se pudo conectar a la base de datos.")
            return None
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

conexion()

def main():
    password = input("Ingrese una contraseña: ").encode('utf-8')
    print("contraseña registrada:", password.decode('utf-8'))

    salto = bcrypt.gensalt()
    secured_password = bcrypt.hashpw(password, salto)

    print("contraseña segura:", secured_password.decode('utf-8'))
    
    validation_password = input("Ingrese la contraseña a validar: ").encode('utf-8')

    if bcrypt.checkpw(validation_password, secured_password):
        print("Contraseña correcta")
    else:
        print("Error de contraseña")

    confirmacion = input("¿Desea volver a probar? (s/n): ")
    time.sleep(1)

    if confirmacion == "s":
        print("Recargando...")
        time.sleep(2)
        print("-------------------------------")
        main()
    else:
        time.sleep(1)
        print("Adios")

