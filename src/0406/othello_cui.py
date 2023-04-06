class Othello:
    def __init__(self):
        self.board = [['.' for j in range(8)] for i in range(8)]
        self.board[3][3] = 'W'
        self.board[4][4] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.current_player = 'B'

    def print_board(self):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            row_str = str(i) + " "
            for j in range(8):
                row_str += self.board[i][j] + " "
            print(row_str)
        print()

    def is_on_board(self, x, y):
        return x >= 0 and x <= 7 and y >= 0 and y <= 7

    def is_legal_move(self, xstart, ystart):
        if not self.is_on_board(xstart, ystart) or self.board[xstart][ystart] != '.':
            return False
        if self.current_player == 'W':
            other_player = 'B'
        else:
            other_player = 'W'
        self.board[xstart][ystart] = self.current_player
        tiles_to_flip = []
        for xdir, ydir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x, y = xstart, ystart
            x += xdir
            y += ydir
            if self.is_on_board(x, y) and self.board[x][y] == other_player:
                x += xdir
                y += ydir
                if not self.is_on_board(x, y):
                    continue
                while self.board[x][y] == other_player:
                    x += xdir
                    y += ydir
                    if not self.is_on_board(x, y):
                        break
                if not self.is_on_board(x, y):
                    continue
                if self.board[x][y] == self.current_player:
                    while True:
                        x -= xdir
                        y -= ydir
                        if x == xstart and y == ystart:
                            break
                        tiles_to_flip.append([x, y])

        self.board[xstart][ystart] = '.'
        if len(tiles_to_flip) == 0:
            return False
        return tiles_to_flip

    def make_move(self, xstart, ystart):
        tiles_to_flip = self.is_legal_move(xstart, ystart)
        if not tiles_to_flip:
            return False
        self.board[xstart][ystart] = self.current_player
        for x, y in tiles_to_flip:
            self.board[x][y] = self.current_player
        if self.current_player == 'W':
            self.current_player = 'B'
        else:
            self.current_player = 'W'
        return True

    def get_valid_moves(self):
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if self.is_legal_move(i, j):
                    valid_moves.append((i, j))
        return valid_moves

    def count_tiles(self):
        black_tiles = 0
        white_tiles = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'B':
                    black_tiles += 1
                elif self.board[i][j] == 'W':
                    white_tiles += 1
        return {'B': black_tiles, 'W': white_tiles}

    def play(self):
        while True:
            valid_moves = self.get_valid_moves()
            if valid_moves:
                self.print_board()
                print('B: %d  W: %d' % (self.count_tiles()['B'], self.count_tiles()['W']))
                if self.current_player == 'B':
                    print('Black player plays:')
                else:
                    print('White player plays:')
                x, y = input('Enter your move (row col): ').split()
                x = int(x)
                y = int(y)
                if (x, y) in valid_moves:
                    self.make_move(x, y)
                elif x == 'skip':
                    if len(valid_moves) == 0:
                        break
                else:
                    print('Invalid move.')
            else:
                break

        self.print_board()
        scores = self.count_tiles()
        print('B: %d  W: %d' % (scores['B'], scores['W']))
        if scores['B'] > scores['W']:
            print('Black wins!')
        elif scores['W'] > scores['B']:
            print('White wins!')
        else:
            print('Tie game!') 


if __name__ == '__main__':
    game = Othello()
    game.play()