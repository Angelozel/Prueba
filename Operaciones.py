def run():
    
    menu = """

    ¡¡¡ BIENVENIDO A LAS 3 OPERACIONES BÁSICAS !!!

1  -  Suma
2  -  Resta
3  -  Multiplicación


Elige una opción :  """

    opcion = int(input(menu))

    if opcion == 1:
        valor_1 = input("Digite el primer valor: ")
        valor_2 = input("Digite el segundo valor: ")    
        suma = int(valor_1)+int(valor_2)
        print("La suma de los dos valores es igual a : " + str(suma))
    elif opcion == 2:
        valor_1 = input("Digite el primer valor: ")        
        valor_2 = input("Digite el segundo valor: ")
        resta = int(valor_1)-int(valor_2)
        print("La resta de los 2 valores es : " + str(resta))
    elif opcion == 3:
        valor_1 = input("Digite el primer valor: ")
        valor_2 = input("Digite el segundo valor: ")
        multiplicación = int(valor_1)*int(valor_2)
        print("La multiplicación de los dos valores es igual a : " + str(multiplicación))
    else:
        print(" !!! Por favor escoja una opción !!!")

if __name__ == "__main__":
    run()
    