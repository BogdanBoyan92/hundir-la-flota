import numpy as np

from funciones import *
from clases import *


print("\n ¡¡Bienvenido al juego de Hundir la Flota!!")
print(Informacion)
print("\n Compienza el juego \n")
separador_horizontal(20)
tablero_jugador = Tablero(barcos) # empieza el juego_jugador
tablero_maquina = Tablero(barcos_maquina) # empieza el juego_maquina

print("\n Tu Tablero:\n")
print(tablero_jugador.tablero)

num_aciertos_jugador = 2
num_aciertos_maquina = 2

respuesta_disparo = []

while True:
    print("\n Es tu turno")
    respuesta_disparo = ["Tocado", 0]
    while respuesta_disparo[0] == "Tocado":
        respuesta_disparo = disparar(tablero_maquina, 1, num_aciertos_jugador)
        num_aciertos_jugador = respuesta_disparo[1]
        if respuesta_disparo[0] == "FIN":
            print("\n ¡¡HAS GANADO!!")
            break
        elif respuesta_disparo[0] == "SALIR":
            print("\n ¡¡HAS SALIDO DEL JUEGO!!")
            break

    if respuesta_disparo[0] == "FIN" or respuesta_disparo[0] == "SALIR":
        print("\n Tu Tablero:\n")
        print(tablero_jugador.tablero)

        print("\n Tablero Máquina:\n")
        print(tablero_maquina.tablero)
        break
        

    print("\n TURNO DE LA MAQUINA")
    respuesta_disparo = ["Tocado", 0]
    while respuesta_disparo[0] == "Tocado":
        respuesta_disparo = disparar(tablero_jugador, 2, num_aciertos_maquina)
        num_aciertos_maquina = respuesta_disparo[1]
        if respuesta_disparo[0] == "FIN":
            print("\n ¡¡HAS PERDIDO!!")
            break

    if respuesta_disparo[0] == "FIN":
        print("\nTu Tablero:\n")
        print(tablero_jugador.tablero)

        print("\nTablero Máquina:\n")
        print(tablero_maquina.tablero)
        break
