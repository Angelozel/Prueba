### Ejercisio de Panda sobre una empresa ####
def run():
        
    menu = """
   ¡¡¡¡ BIENVENIDO A LA EMPRESA PANDIPANDA !!!!
"""
    opcion = print(menu)
    nombre = input("Ingrese su nombre: ")
    nombre = nombre.capitalize()


    años = int(input("Cuantos años va trabajando en la empresa?: "))

    opcion = 30

    if años > opcion :
        print("Usted tiene un bono de 5000$ ....Felicidades!!")
    elif años < opcion :
        print("Usted no tiene ningún bono aún ")
    elif años == opcion:
        print("Usted tiene un bono de 5000$ ....Felicidades!!")     
   
    else:
        print("Por favor escriba cuantos años va trabajando")

    print("¡¡¡ESO ES TODO ESTIMADO " + str(nombre)+"!!!") 
    

if __name__== "__main__":
    run()
      