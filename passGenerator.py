from werkzeug.security import generate_password_hash, check_password_hash
#Empezamos declarando el final el bucle como falso
end = False
#Mientras no sea el final se ejecuta el bucle
while not end:
    #Si pulsamos 1 generamos una contraseña, si pulsamos 2 vemos si una contraseña coincide, si pulsamos otro boton salimos
    option = input("1. Generar contraseña \n2. Ver si una contraseña coincide\n3. Pulsa cualquier opcion que no sea 1 ni 2 para salir\nOpción: ")
    match option:
        case "1":
            password = input("Ingresa tu contraseña: ")
            hashed = generate_password_hash(password)
            print(f"Contraseña hasheada: {hashed}")
        case "2":
            password = input("Ingresa tu contraseña: ")
            hashed = input("Ingresa la contraseña hasheada: ")
            if check_password_hash(hashed, password):
                print("¡Las contraseñas coinciden!")
            else:
                print("Las contraseñas no coinciden")
        case _:
            end = True
            print("¡Hasta luego!")