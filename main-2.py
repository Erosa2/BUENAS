# Definir la contraseña
contrasena_correcta = "mi_contrasena_secreta"

while True:
    # Solicitar la contraseña al usuario
    contrasena_ingresada = input("Ingresa la contraseña: ")

    # Comprobar si la contraseña ingresada es correcta
    if contrasena_ingresada == contrasena_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
