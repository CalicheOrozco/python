while True:
    objetivo = int(input('Dame un numero: '))
    respuesta=0
    while respuesta**2 <objetivo:
        respuesta += 1
    if  respuesta**2 == objetivo:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')