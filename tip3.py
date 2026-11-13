variable = 0
while(variable == 0):
    try:
        variable = int(input("ingrese una opcion: \n"))
    except:
        print("ha ocurrido un error")
        variable = 0