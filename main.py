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

def register_password(secured_passwords):
    password = input("Ingrese una contraseña: ").encode('utf-8')
    print("Contraseña registrada:", password.decode('utf-8'))
    time.sleep(1)
    salto = bcrypt.gensalt()
    secured_password = bcrypt.hashpw(password, salto)
    secured_passwords.append(secured_password)
    print("Contraseña segura almacenada.")
    time.sleep(1)

def validate_password(secured_passwords):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        validation_password = input("Ingrese la contraseña a validar: ").encode('utf-8')
        time.sleep(1)
        for secured_password in secured_passwords:
            if bcrypt.checkpw(validation_password, secured_password):
                print("Contraseña correcta")
                return True
        attempts += 1
        print("Error de contraseña. Intentos restantes:", max_attempts - attempts)
    print("Número máximo de intentos alcanzado. Acceso denegado.")
    time.sleep(2)
    return False

def verificar_usuarios(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        print("\nLista de usuarios:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, RUT: {usuario[1]}, Nombre: {usuario[2]} {usuario[3]}")
        cursor.close()
        time.sleep(3)
    except Exception as e:
        print(f"Error al verificar usuarios: {e}")
        time.sleep(1)

def borrar_tabla(conexion):
    try:
        tabla = input("Ingrese el nombre de la tabla a borrar: ")
        time.sleep(1)
        cursor = conexion.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {tabla}")
        conexion.commit()
        print(f"Tabla {tabla} eliminada correctamente")
        cursor.close()
        time.sleep(1)
    except Exception as e:
        print(f"Error al borrar tabla: {e}")
        time.sleep(1)

def añadir_tabla(conexion):
    try:
        cursor = conexion.cursor()
        nombre_tabla = input("Ingrese el nombre de la nueva tabla: ")
        sql = f"""CREATE TABLE {nombre_tabla} (
            id INT NOT NULL AUTO_INCREMENT,
            nombre VARCHAR(50) NOT NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB"""
        cursor.execute(sql)
        conexion.commit()
        print(f"Tabla {nombre_tabla} creada correctamente")
        cursor.close()
        time.sleep(3)
    except Exception as e:
        print(f"Error al crear tabla: {e}")
        time.sleep(1)

def revisar_tablas(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        print("\nTablas en la base de datos:")
        for tabla in tablas:
            print(tabla[0])
        cursor.close()
        time.sleep(3)
    except Exception as e:
        print(f"Error al revisar tablas: {e}")
        time.sleep(1)

def eliminar_usuario(conexion):
    try:
        cursor = conexion.cursor()
        id_usuario = input("Ingrese el ID del usuario a eliminar: ")
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        conexion.commit()
        print(f"Usuario con ID {id_usuario} eliminado correctamente")
        cursor.close()
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")

def main():
    secured_passwords = []
    admin_password = bcrypt.hashpw("Inacap.2024".encode('utf-8'), bcrypt.gensalt())
    is_admin = False
    db_connection = conexion()

    while True:
        print("\nMenu de Inicio:")
        print("1. Iniciar sesión como Administrador")
        print("2. Iniciar sesión como Usuario")
        print("3. Salir")
        choice = input("Seleccione una opción (1-3): ")
        time.sleep(1)

        if choice == '1':
            password_input = input("Ingrese la contraseña de administrador: ").encode('utf-8')
            if bcrypt.checkpw(password_input, admin_password):
                is_admin = True
                print("Acceso de administrador concedido.")
            else:
                print("Contraseña de administrador incorrecta.")
        
        elif choice == '2':
            while True:
                print("\nMenu de Usuario:")
                print("1. Registrar nueva contraseña")
                print("2. Validar contraseñas registradas")
                print("3. Volver al menú principal")
                user_option = input("Seleccione una opción (1-3): ")

                if user_option == '1':
                    register_password(secured_passwords)
                elif user_option == '2':
                    if validate_password(secured_passwords):
                        print("Acceso de usuario concedido.")
                        while True:
                            print("\nNuevo Menu de Usuario:")
                            print("1. Verificar saldo")
                            print("2. Revisar cuentas")
                            print("3. Enviar dinero")
                            print("4. Recibir dinero")
                            print("5. Volver al menú principal")
                            user_action = input("Seleccione una opción (1-5): ")
                            if user_action == '1':
                                print("Función de verificación de saldo (implementación pendiente).")
                                time.sleep(3)
                            elif user_action == '2':
                                print("Función de revisión de cuentas (implementación pendiente).")
                                time.sleep(3)
                            elif user_action == '3':
                                print("Función de envío de dinero (implementación pendiente).")
                                time.sleep(3)
                            elif user_action == '4':
                                print("Función de recepción de dinero (implementación pendiente).")
                                time.sleep(3)
                            elif user_action == '5':
                                break
                            else:
                                print("Opción no válida. Intente de nuevo.")
                                time.sleep(1)
                    else:
                        print("Acceso denegado.")
                elif user_option == '3':
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        while is_admin:
            print("\nMenu de Administrador:")
            print("1. Verificar usuarios")
            print("2. Borrar tablas")
            print("3. Añadir tablas")
            print("4. Revisar tablas")
            print("5. Eliminar usuarios")
            print("6. Volver al menú principal")
            option = input("Seleccione una opción (1-6): ")
            if option == '1':
                verificar_usuarios(db_connection)
            elif option == '2':
                borrar_tabla(db_connection)
            elif option == '3':
                añadir_tabla(db_connection)
            elif option == '4':
                revisar_tablas(db_connection)
            elif option == '5':
                eliminar_usuario(db_connection)
            elif option == '6':
                is_admin = False
                break
            else:
                print("Opción no válida. Intente de nuevo.")
conexion()
main()