from pico2d import *
import random
import threading
import game_framework
import game_world
from Horse import Horse
import guide
import imageloader
import loadtimer
import reverse
import checkover

nowTurn='bean'
gameStatus = 'Ready'

board=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        board[i][j]='None'  # 돌 중복해서 놓지 못하게

ran_list = [0,1,2,5,6,7]

class Map:
    image=None
    def __init__(self):
        if Map.image==None:
            Map.image=load_image('보오오드.png')
    def draw(self):
        Map.image.draw(400,300)
    def update(self):
        pass

class Hurdle:
    global board
    image=None
    def __init__(self, x, y):
        self.x, self.y=x,y
        board[self.y][self.x]='hurdle'
        if Hurdle.image==None:
            Hurdle.image=load_image('장애물.png')
    def draw(self):
        if gameStatus != 'Ready':
            Hurdle.image.draw(self.x*58+195,self.y*58+55)
    def update(self):
        pass

def handle_events():
    global nowTurn, board, gameStatus
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.quit()
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT and gameStatus=='Run':
                tx, ty = e.x, 600 - e.y
                x, y= -1, -1
                for i in range(8):
                    if tx>=(i-1)*58+195+29 and tx<i*58+195+29:
                        x=i
                for j in range(8):
                    if ty>=(j-1)*58+55+29 and ty<j*58+55+29:
                        y=j
                if x<=7 and x>=0 and y<=7 and y>=0 and board[y][x]=='None':
                    if reverse.checkReverse(x,y)!=0:
                        game_world.add_object(Horse(x, y),game_world.layer_horse)
                        reverse.reverse(x, y)
                        loadtimer.timer.cancel()
                        loadtimer.time = 16
                        loadtimer.startTimer()
                        if checkover.checkOver()==False:
                            gameStatus = 'End'
                        game_world.clear_layer(game_world.layer_guide)
                        guide.guidefunc()

def enter():
    global bgm2, nowTurn

    bgm2 = load_music('game_music.mp3')
    bgm2.set_volume(10)
    bgm2.repeat_play()
    imageloader.loadImage()
    loadtimer.readyTimer()
    # 보드 그리기
    map=Map()
    game_world.add_object(map,game_world.layer_bg)
    # 장애물 생성
    for i in range(5):
        game_world.add_object(Hurdle(ran_list[random.randint(0, 5)], ran_list[random.randint(0, 5)]), game_world.layer_hurdle)

    # 말 중앙 좌표에 놓기
    game_world.add_object(Horse(3,3),game_world.layer_horse)
    game_world.add_object(Horse(4,4),game_world.layer_horse)
    nowTurn = 'chick'
    game_world.add_object(Horse(3,4),game_world.layer_horse)
    game_world.add_object(Horse(4,3),game_world.layer_horse)
    nowTurn = 'bean'
    guide.guidefunc()

def draw():
    clear_canvas()
    game_world.draw()
    imageloader.draw()
    update_canvas()

def update():
    game_world.update()

def exit():
    pass

if __name__=='__main__':
     import sys 
     current_module = sys.modules[__name__]   
     open_canvas() 
     game_framework.run(current_module) 
     close_canvas() 
