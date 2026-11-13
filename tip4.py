

#maxino 10 elementos
lista = [1,2,3,4,5]
while(True):
    variable = int(input("ingrese un elemento numerico: \n"))
    if (len(lista) < 10):
        lista.append(variable)
        print(lista)