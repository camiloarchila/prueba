"""
Created on Mon Jul  6 08:59:36 2020

@author: Camilo
"""
def quetipo():
    a = input("Digite valor: ")
    if type(a) == int:
        print("la variable es", type(a))
    elif type(a) == str:
        print("la variable es", type(a))
    elif type(a) == float:
        print("la variable es", type(a))
    else:
        print("la variable es", type(a))
        
def prueba():
    while True:
        entrada = input("Digite un valor entero")
        try:
            entrada = int(entrada)
        except ValueError:
            print("el valor digitado no es un entero")
        else:
            break
    print("exito")