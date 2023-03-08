# BUSCA MINAS
import random
import numpy as np

board = []

class Cell:
    def __init__(self, is_mine, is_revealed, adjacent_mines):
        self.is_mine = is_mine
        self.is_revealed = is_revealed
        self.adjacent_mines = adjacent_mines
    


class Minesweeper():
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = board
        self.c = 0
        self.contador = 0
        self.lista_m = [random.randint(1, self.cols )]
        self.lista_n = [random.randint(1, self.rows )]
        self.c_2 = True
        self.contador = 0
     
    

    def iniciar_board(self):
        self.board = np.chararray((self.rows, self.cols), itemsize=1, unicode=True)
        self.board[:] = '-'
        self.board_zero = np.chararray((self.rows + 2, self.cols + 2), itemsize=1, unicode=True)
        self.board_zero[:] = 'N'
        
        while self.c <= self.num_mines:
            for m,n in zip(self.lista_m, self.lista_n):
                self.lista_m[0] = random.randint(1, self.cols)
                self.lista_n[0] = random.randint(1, self.rows)
                if self.board_zero[n][m] == 'N':
                    self.board_zero[n][m] = 'M'
                    self.c += 1
                else:
                    continue
        print(self.board)
        print(self.board_zero)
    
    def analisis_cell(self, row, col):
        self.contador = 0
        if self.board_zero[col][row - 1] == 'M':
            self.contador += 1
        if self.board_zero[col - 1][row - 1] == 'M':
            self.contador += 1
        if self.board_zero[col - 1][row] == 'M':
            self.contador += 1
        if self.board_zero[col][row + 1] == 'M':
            self.contador += 1
        if self.board_zero[col + 1][row + 1] == 'M':
            self.contador += 1
        if self.board_zero[col + 1][row] == 'M':
            self.contador += 1
        if self.board_zero[col + 1][row - 1] == 'M':
            self.contador += 1

    def reveal_cell(self):
        while self.c_2 == True:
            row_pregunta = int(input("¿Qué fila desea seleccionar? "))
            col_pregunta = int(input("¿Qué columna desea seleccionar? "))
            cavar_bandera = input("¿Desea Cavar (C) o Bandera (B)?: ")
            if cavar_bandera == "C":    
                if self.board_zero[row_pregunta + 1][col_pregunta + 1] != 'M':
                    self.analisis_cell(row_pregunta, col_pregunta)
                    self.board[row_pregunta][col_pregunta] = self.contador
                else:
                    print("¡Game Over!")
                    quit()
            else:
                self.board[row_pregunta][col_pregunta] = 'B'
            print(self.board)          
    

obj_1 = Minesweeper(5,5,25)
obj_1.iniciar_board()
obj_1.reveal_cell()