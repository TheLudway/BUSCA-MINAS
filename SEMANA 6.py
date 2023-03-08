"""BUSCA MINAS
Ludwig Alvarado Becerra
Maria Camila Guaqueta
"""

import random
import numpy as np

board = []

class Cell:
    def __init__(self, is_mine, is_revealed, adjacent_mines):
        """Clase cell, se establecen los parametros de la celda"""
        self.is_mine = is_mine
        self.is_revealed = is_revealed
        self.adjacent_mines = adjacent_mines    


class Minesweeper():
    def __init__(self, rows, cols, num_mines):
        """Se establecen todos los parametros a usar al momento de jugar"""
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = board
        self.c = 0
        self.contador = 0
        self.lista_m = [random.randint(1, self.cols )] # Se establece un número entre 1 al número de columnas deseadas para seleccionar
        self.lista_n = [random.randint(1, self.rows )] # Se establece un número entre 1 al número de filas deseadas para seleccionar
        self.c_2 = True
        self.contador = 0
     
    

    def iniciar_board(self):
        """Crea dos matrices, una que es visible (La que se llena con guiones) y la segunda que es la oculta y en la que se opera todo (La que se llena con N)"""
        self.board = np.chararray((self.rows, self.cols), itemsize=1, unicode=True)
        self.board[:] = '-'
        self.board_zero = np.chararray((self.rows + 2, self.cols + 2), itemsize=1, unicode=True)
        self.board_zero[:] = 'N'
        
        while self.c < self.num_mines:
            """Inserta las minas al azar"""
            for m,n in zip(self.lista_m, self.lista_n):
                self.lista_m[0] = random.randint(1, self.cols)
                self.lista_n[0] = random.randint(1, self.rows)
                if self.board_zero[n][m] == 'N':
                    self.board_zero[n][m] = 'M'
                    self.c += 1
                else:
                    continue
        print(self.board)

        
    
    def analisis_cell(self, row, col):
        """Analiza las celdas que están alrededor de la celda que seleccionó el usuario"""
        self.contador = 0
        if self.board_zero[row, col-1] == 'M':
            self.contador += 1
        if self.board_zero[row - 1, col - 1] == 'M':
            self.contador += 1
        if self.board_zero[row - 1, col] == 'M':
            self.contador += 1
        if self.board_zero[row, col + 1] == 'M':
            self.contador += 1
        if self.board_zero[row + 1, col + 1] == 'M':
            self.contador += 1
        if self.board_zero[row + 1, col] == 'M':
            self.contador += 1
        if self.board_zero[row + 1, col - 1] == 'M':
            self.contador += 1

        
    def reveal_cell(self):
        """Pregunta qué fila y columna tomar. Para luego cavar o poner bandera"""
        while self.c_2 == True:
            row_pregunta = int(input("¿Qué fila desea seleccionar? "))
            col_pregunta = int(input("¿Qué columna desea seleccionar? "))
            cavar_bandera = input("¿Desea Cavar (C) o Bandera (B)?: ").upper()
            if cavar_bandera == "C":    
                if self.board_zero[row_pregunta + 1][col_pregunta + 1] != 'M':
                    self.analisis_cell(row_pregunta + 1, col_pregunta + 1)
                    self.board[row_pregunta][col_pregunta] = self.contador
                else:
                    print("¡Game Over!")
                    quit()
            else:
                self.board[row_pregunta][col_pregunta] = 'B'
            print(self.board)   

filas = int(input("Ingrese la cantidad de filas que quiera su tablero: "))
columnas = int(input("Ingrese la cantidad de columnas que quiera en su tablero: "))
minas = int(input("Ingrese la cantidad de minas que desee en el tablero: "))


obj_1 = Minesweeper(filas,columnas,minas)
obj_1.iniciar_board()
obj_1.reveal_cell()
