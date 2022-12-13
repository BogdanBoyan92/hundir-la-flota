import random
from clases import *

def separador_horizontal(columna):
    
    for i in range(columna+1):
        print("+---", end="")
    print("+")


def disparar(tablero, turno:int, num_aciertos:int):
    respuesta_disparo = []
    if turno == 1: # Turno del jugador
        num_filas = int(input("\n Introduce la fila:"))
        num_columnas = int(input("\n Introduce la columna:"))

        if num_filas == 00 | num_columnas == 00:
            respuesta_disparo = ["SALIR", num_aciertos]
            return respuesta_disparo

    else: # Turno de la maquina
        num_filas = random.randint(0,9)
        num_columnas = random.randint(0,9)

    respuesta_otra = tablero.disparar((num_filas,num_columnas))

    if respuesta_otra == "Agua":
        respuesta_disparo = ["Agua", num_aciertos]
        return respuesta_disparo
    elif respuesta_otra == "Tocado":
        print("\n Tocado:",(num_filas,num_columnas))
        num_aciertos = num_aciertos - 1

        if num_aciertos == 0:
            respuesta_disparo = ["FIN", num_aciertos]
            return respuesta_disparo
        else:
            respuesta_disparo = ["Tocado", num_aciertos]
            return respuesta_disparo
