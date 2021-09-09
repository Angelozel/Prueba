def run():
#-----------------------------------------------------------    
# Break con el ciclo while : 

    L = 1000
    numero = 0
    potencia_5 = 5**numero
    while potencia_5 < L:
        print(potencia_5)
        numero += 1
        potencia_5 = 5**numero
        if potencia_5 > 100:
            print("El numero sobrepasa 100 sorry :c ")
            break

# ---------------------------------------------------------   
# Continue con el ciclo while :                           
                                                          
    L = 1000
    numero = 0
    potencia_5 = 5**numero
    while potencia_5 < L:
        print(potencia_5)
        numero += 1
        potencia_5 = 5**numero
        if potencia_5 > 100:
            continue

#------------------------------------------------------------            

if __name__ == "__main__":
    run()
    