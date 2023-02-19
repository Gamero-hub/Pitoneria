# creamos una lista con list()
lista = list(["hola", "pablo", 34])

# devuelve la cantidad de elementos de una lista
cantidad_elementos = len(lista)

# agrega elemento a una lista
# agregando_con_append = lista.append("JAJAJAJ")
# agrega elemento a la lista en un índice en específico
# lista.insert(2,"Pepe")
# agregando varios elementos a la lista
# lista.extend(["como", "estas"])

# eliminando un elemento de la lista (por su índice)
# lista.pop()  # -1 para eliminar el ultimo sucesivamente
# removiendo un elemento de la lista por su valor
# lista.remove("pablo")
# eliminando todos los elementos de la lista
# .clear()

# ordenando la lista ascendente - a +  (si usamos el parametro reverse=True lo ordena en descendente)
# lista.sort()
# invirtiendo los elmentos de una lista
# lista.reverse()

# verificando si un elemento se encuentra en la lista
lista.index(34)

print(lista)
