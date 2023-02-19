print("Hola, bienvenido a este conversor de palabras")
texto = input("Primero, ponga un texto a convertir ")
print(f"Tu texto es: {texto}")
print("Opcines a tu texto: \n"
      "A - Convertir todo a mayusculas\n"
      "B - Convertir todo a minusculas\n"
      "C - Poner primera letra en mayuscula\n"
      "D - Contar cuantas palabras tiene \n"
      "E - Cambiar letra por letra a desear \n")

opcion = input("Dime una opcion: ")

if opcion == "A" or opcion == "a":
    print(f"Escogiste opcion: {texto}")
    print(f"Aqui esta tu texto: {texto.upper()}")

if opcion == "B" or opcion == "b":
    print(f"Escogiste opcion: {texto}")
    print(f"Aqui esta tu texto: {texto.lower()}")

if opcion == "C" or opcion == "c":
    print(f"Escogiste opcion: {texto}")
    print(f"Aqui esta tu texto: {texto.capitalize()}")

if opcion == "D" or opcion == "d":
    print(f"Escogiste opcion: {texto}")
    print(f"Aqui esta tu texto: {len(texto)}")

if opcion == "E" or opcion == "e":
    print(f"Escogiste opcion: {texto}")
    letra_cambiar = input("Dime la letra a cambiar: ")
    letra_ = input("Dime la letra por la que quieres cambiar la otra letra: ")
    print(f"Aqui esta tu texto: {texto.replace(letra_cambiar, letra_)}")
