frase = input("Dime una frase y te dire cuanto tardarias en decirla ")

frase_contada = len(frase.split(" "))

print(f"Dijiste {frase_contada} palabras Tardarias {frase_contada / 2} segundos en decir la frase")
print(f"Dalto lo diria en {frase_contada * 100 // 2 * 1.3 / 100}")
