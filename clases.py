import numpy as np

# Implementamos la clase
class Tablero():
   
    # Atributos de la clase
    tablero = np.full(10, 10)
    num_barcos = {
            "barco_1_1": 1,
            "barco_1_2": 1,
            "barco_1_3": 1,
            "barco_1_4": 1,
            "barco_2_1": 2,
            "barco_2_2": 2,
            "barco_2_3": 2,
            "barco_3_1": 3,
            "barco_3_2": 3,
            "barco_4_1": 4,
            }

    # Se define constructor
    def __init__(self, barcos:list, dimensiones:int=10):
        # parametros comunes

        self.barcos = barcos
        self.dimensiones = dimensiones
        self.inicializar_tablero(dimensiones)
        self.colocar_barcos(self.barcos)
       
       

    # se define metodo inicializar_tablero
    def inicializar_tablero(self, dimensiones):
        self.dimensiones = dimensiones
        self.tablero = np.full((self.dimensiones,self.dimensiones), " ")

    # se define metodo colocar_barco
    def colocar_barco(self, barco:list):
       
        for coordenada in barco:
            self.tablero[coordenada] = "O"

    # se define metodo colocar_barcos
    def colocar_barcos(self, lista_barcos:list):
        
        for barco in lista_barcos:
            self.colocar_barco(barco)

    # se define metodo disparar
    def disparar(self, casilla:list):
        if self.tablero[casilla] == "O":
            self.tablero[casilla] = "X"
            return "Tocado"
        elif self.tablero[casilla] == " ":
            self.tablero[casilla] = "-"
            return "Agua"
        elif self.tablero[casilla] == "-":
            self.tablero[casilla] = "-"
            return "Agua"


Informacion = "\n Vas a disponer de 10 barcos con distinta eslora: " \
        "\n     4 barcos con eslora 1 \n     3 barcos con eslora 2 \n     2 barcos con eslora 3 \n     1 barco con eslora 4" \
        "\n\n Si quieres salir del juego tienes que escribir 00 en cualquier input que te pidan." \

barcos_maquina = [[(0,1)], [(4,3)], [(3,1)], [(6,7)], 
                    [(3,7), (3,8)], [(8,4), (8,5)], [(6,4), (6,5)],
                    [(9,8), (9,7), (9,6)], [(7,2), (7,1), (7,0)],
                    [(3,5), (2,5), (1,5), (0,5)]
                ]

barcos = [[(0,8)], [(0,3)], [(6,9)], [(6,7)], 
            [(3,7), (3,8)], [(8,4), (8,5)], [(6,4), (6,5)],
            [(9,8), (9,7), (9,6)], [(7,2), (7,1), (7,0)],
            [(3,1), (2,1), (1,1), (0,1)]
        ]

