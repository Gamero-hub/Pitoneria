diccionario = {
    "nombre": "Pablo",
    "Apellido": "Segui",
    "subs": 19
}

# Devuelve las claves (también nos sirve para iterar)
claves_keys = diccionario.keys()

# Obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_nombre = diccionario.get("nombre")

# Eliminando todo de un diccionario
# diccionario.pop("nombre")

# obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
