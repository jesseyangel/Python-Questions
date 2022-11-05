lista = [1, 2, 10, 4, 1] 
max = float('-inf') #inf é infinito - um valor que é maior do que qualquer outro value.is, portanto, menor do que qualquer outro valor.-inf
for item in lista: #percorrer os itens na lista
    item = int(item) #declarando como valor inteiro
    if item > max: #Se item for maior que max
        max = item #Trasnformando item no valor max
print(max)