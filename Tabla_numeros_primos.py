def tabla(numero):
    print("\n Esta es la tabla de " + str(numero))

    for i in range(1, 13):
        print("\n" + str(numero) + " por " + str(i) + " es : " + str(numero*i))


def main():

    menu = """ 
    ¡¡  BIENVENIDO  , AQUI LA TABLA DE 
                LOS NÚMEROS PRIMOS !!!
    
    
    ELIGE UN NÚMERO :

    a. Tabla del 3
    b. Tabla del 5
    c. Tabla del 7
    d. Tabla del 11
    e. Tabla del 13
    f. Tabla del 17
    g. Tabla del 19
    h. Tabla del 23
    m. Tabla del 27
    """
    opcion =  str(input(menu))

    if opcion == "a":
        tabla(3)
    elif opcion == "b":
        tabla(5)
    elif opcion == "c":
        tabla(7)
    elif opcion == "d":
        tabla(11)
    elif opcion == "e":
        tabla(13)
    elif opcion == "f":
        tabla(17)
    elif opcion == "g":
        tabla(19)
    elif opcion == "h":
        tabla(23)  
    elif opcion == "m":
        tabla(27)                   
    else:
        print("ERROR 404 : El programador tiene pereza de seguir poniendo opciones.")


if __name__ == '__main__':
    main()
