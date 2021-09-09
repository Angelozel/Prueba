import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input(' Que número crees que estoy pensando del 1 al 100: '))
    vidas = 5
    while numero_elegido != numero_aleatorio:
    
        if numero_elegido < numero_aleatorio:
            print('\n Busca un número más grande')
            vidas -= 1

        elif numero_elegido > numero_aleatorio:
            print('\n Busca un número más pequeño')
            vidas -= 1
     
        if vidas == 0:
            print("\n ¡ OOPS TE QUEDASTE SIN VIDAS ---- ¡ GAME OVER ! ")    
            break
        
        print("\n Tienes " + str(vidas) + " vidas")
        numero_elegido = int(input('\n Elige otro número: '))
    
    if numero_elegido == numero_aleatorio:
        print("\n ¡GANASTE !") 

# -----------------------------------------------------> TRUCOS <-------------------------------------------------------

#-------------------------------------------------------------------------------------------
# UTILIZAMOS BREAK EN EL PRIMER IF SI QUEREMOS GANAR AL PRIMER INTENTO CON CUALQUIER NÚMERO-
#-------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------
# UTILIZAMOS BREAK EN ELIF  SI QUEREMOS GANAR AL SEGUNDO INTENTO Y NO DAR POR PERCIBIDO EL TRUCO.(SOLO SE PUEDE CON EL NÚMERO 100)-
#----------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    run()