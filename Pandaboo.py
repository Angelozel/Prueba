#### Convirtiendo soles a doláres #####
soles = input ("¿Cuantos soles tienes?: ")

soles = float(soles)   
valor_dolar = 4.10
dolares = soles / valor_dolar
dolares = round (dolares,2)
dolares = str(dolares)

print("Tienes $" + dolares + " dólares")
