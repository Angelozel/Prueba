print("""
   ¡¡¡¡ BIENVENIDO A LA EMPRESA PANDIPANDA !!!!
""")

nombre = input("Ingrese su nombre: ")


años = int(input("Cuantos años va trabajando en la empresa?: "))

opcion = 43

if años > opcion :
    print("Usted tiene un bono de 5000$ ....Felicidades!!")
elif años < opcion :
    print("Usted no tiene ningún bono aún ")
elif años == opcion:
    print("Usted tiene un bono de 5000$ ....Felicidades!!")     
   
else:
    print("Por favor escriba cuantos años va trabajando")

