import tkinter as tk

class Othello:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2

    def legal_moves(self, player):
        moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0:
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                        x, y = i + di, j + dj
                        if 0 <= x < 8 and 0 <= y < 8 and self.board[x][y] == 3 - player:
                            while 0 <= x < 8 and 0 <= y < 8 and self.board[x][y] == 3 - player:
                                x, y = x + di, y + dj
                            if 0 <= x < 8 and 0 <= y < 8 and self.board[x][y] == player:
                                moves.append((i, j))
                                break
        return moves
    
    
class OthelloGUI:
    def __init__(self):
        self.othello = Othello()
        self.player = 1
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.draw_pieces()
        self.canvas.bind("<Button-1>", self.on_click)
        self.root.mainloop()

    def draw_board(self):
        for i in range(80):
            for j in range(8):
                x0, y0 = 50 + j * 50, 50 + i * 50
                x1, y1 = x0 + 50, y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="green", outline="white")
                
    def draw_pieces(self):
        self.canvas.delete("piece")
        for i in range(8):
            for j in range(8):
                if self.othello.board[i][j] == 1:
                    x, y = 50 + j * 50, 50 + i * 50
                    self.canvas.create_oval(x+5, y+5, x+45, y+45, fill="black", outline="black", tags="piece")
                elif self.othello.board[i][j] == 2:
                    x, y = 50 + j * 50, 50 + i * 50
                    self.canvas.create_oval(x+5, y+5, x+45, y+45, fill="white", outline="white", tags="piece")

    def on_click(self, event):
        i, j = (event.y - 50) // 50, (event.x - 50) // 50
        if (i, j) in self.othello.legal_moves(self.player):
            self.othello.board[i][j] = self.player
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                x, y = i + di, j + dj
                while 0 <= x < 8 and 0 <= y < 8 and self.othello.board[x][y] == 3 - self.player:
                    x, y = x + di, y + dj
                if 0 <= x < 8 and 0 <= y < 8 and self.othello.board[x][y] == self.player:
                    x, y = i + di, j + dj
                    while 0 <= x < 8 and 0 <= y < 8 and self.othello.board[x][y] == 3 - self.player:
                        self.othello.board[x][y] = self.player
                        x, y = x + di, y + dj
            self.draw_pieces()
            self.player = 3 - self.player
            
            
if __name__ == "__main__":
    gui = OthelloGUI()
