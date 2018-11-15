from pico2d import *
import game_world
import game_state

class Horse:
    image=None
    rev_sound=None

    def __init__(self,x,y):
        if game_state.nowTurn=='bean':
            self.frame=0
        else:
            self.frame=3
        self.x=x
        self.y=y
        game_state.board[self.y][self.x]=game_state.nowTurn
        if Horse.image==None:
            Horse.image=load_image('콩닭애니메이션.png')
        if Horse.rev_sound==None:
            Horse.rev_sound=load_wav('reverse.wav')
            Horse.rev_sound.set_volume(100)

    def draw(self):
        if game_state.gameStatus != 'Ready':
            Horse.image.clip_draw(self.frame*57,0,57,57,self.x*58+195,self.y*58+55)

    def update(self):
        if game_state.board[self.y][self.x]=='bean'and self.frame!=0:
            if self.frame==3:
                self.rev_sound.play()
            self.frame+=1
            self.frame=self.frame%6
            delay(0.03)
        elif game_state.board[self.y][self.x]=='chick' and self.frame!=3:
            if self.frame == 0:
                self.rev_sound.play()
            self.frame+=1
            self.frame=self.frame%6
            delay(0.03)