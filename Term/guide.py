from pico2d import *
import game_state
import game_world
import reverse

class Guide:
    image=None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame=0
        if Guide.image == None:
            Guide.image = load_image('guide.png')
    def draw(self):
        if game_state.gameStatus != 'Ready':
            Guide.image.clip_draw(self.frame*57,0,57,57,self.x * 58 + 195, self.y * 58 + 55)
    def update(self):
        if game_state.gameStatus=='Run':
            self.frame += 1
            self.frame = self.frame % 4


def guidefunc():
    for y in range(8):
        for x in range(8):
            reversible = reverse.checkReverse(x, y)
            if reversible & 1:
                j = y - 1
                while game_state.board[j][x] != game_state.nowTurn and game_state.board[j][x] != 'None' and game_state.board[j][x] != 'hurdle':
                    j -= 1
                if game_state.board[y][x]=='None':
                    game_world.add_object(Guide(x, y), game_world.layer_guide)
            reversible >>= 1

            if reversible & 1:
                j = y + 1
                while game_state.board[j][x] != game_state.nowTurn and game_state.board[j][x] != 'None' and game_state.board[j][x] != 'hurdle':
                    j += 1
                if game_state.board[y][x] == 'None':
                    game_world.add_object(Guide(x, y), game_world.layer_guide)
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                while game_state.board[y][i] != game_state.nowTurn and game_state.board[y][i] != 'None' and game_state.board[y][i] != 'hurdle':
                    i -= 1
                if game_state.board[y][x]=='None':
                    game_world.add_object(Guide(x, y), game_world.layer_guide)
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                while game_state.board[y][i] != game_state.nowTurn and game_state.board[y][i] != 'None' and game_state.board[y][i] != 'hurdle':
                    i += 1
                if game_state.board[y][x] == 'None':
                    game_world.add_object(Guide(x, y), game_world.layer_guide)
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                j = y - 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i -= 1
                    j -= 1
                if game_state.board[y][x] == 'None':
                    game_world.add_object(Guide(x, y), game_world.layer_guide)
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                j = y - 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i += 1
                    j -= 1
                if game_state.board[y][x] == 'None':
                    game_world.add_object(Guide(x, y), game_world.layer_guide)
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                j = y + 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i -= 1
                    j += 1
                if game_state.board[y][x] == 'None':
                    game_world.add_object(Guide(x, y), game_world.layer_guide)
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                j = y + 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i += 1
                    j += 1
                if game_state.board[y][x] == 'None':
                    game_world.add_object(Guide(x, y), game_world.layer_guide)
            reversible >>= 1