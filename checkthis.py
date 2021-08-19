print( """

¡¡¡¡ BIENVENIDO : 

AQUI PODRAS REGISTRARTE Y SABER SI ERES MAYOR
             O MENOR DE EDAD.  !!!!
""")


nombre = input("Cual es tu nombre?: ")

print("Hola tu nombre es : " +nombre)


edad = int(input("Ingresa tu edad : "))

if edad > 18 :
    print("Eres mayor de edad")

elif edad < 18 :
   print("Eres menor de edad")

elif edad == 18:
    print("Tienes la edad exacta")

else:
    print("Por favor ingresa tu edad correspondiente.")        