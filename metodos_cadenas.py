cadena1 = "Hola soy Pablo"

# convierte a mayúsculas
matysc = cadena1.upper()
# convierte a minusculas
minusc = cadena1.lower()
# primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()

# buscamos una cadena en otra cadena, si no hay coincidencia da -1
busqueda_find = cadena1.find("o")
# buscamos una cadena en otra cadena, da excepcion si no se encuentra la coincidencia
busqueda_index = cadena1.index("o")

# si es numerico devuelve True. sino devuelve False
es_numerico = cadena1.isnumeric()
# si es alfanumerico nos devuelve true, sino nos devuelve false
es_alfanumerico = cadena1.isalpha()

# buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")
# contamos cuentos caracteres tiene una cadena
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empiza_con = cadena1.startswith("Ho")
# verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("Ho")

# remplaza o anade algo por otro algo en una cadena
cadena_nueva = cadena1.replace(" ", "|")
# separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split()

print(cadena_separada[2])
