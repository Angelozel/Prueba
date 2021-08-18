#### CONVERSOR DE MONEDAS PYTHON #####
def conversor(tipo_pesos , valor_dolar):
    pesos = input("¿Cuantos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares =  pesos  / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")

menu = """

¡¡¡¡¡ BIENVENIDO AL CONVERSOR DE MONEDAS !!!!

1   -  Soles
2   -  Pesos Argentinos
3   -  Pesos Colombianos 

Elige una opción :  """

opcion = int(input(menu))

if opcion == 1:
    conversor("Soles", 4.1)

elif opcion == 2:
    conversor("Pesos argentinos", 97 )

elif opcion == 3:
    conversor("Pesos colombianos",3879)
else :
    print("Ingresa una opcion correcta porfavor") 