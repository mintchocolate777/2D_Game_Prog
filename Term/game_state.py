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

button1=0
button2=0
button3=0

beanHp=10000
chickHp=10000

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
    global nowTurn, board, gameStatus, button1, button2, button3, mode
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                if gameStatus=='Run':
                    gameStatus='Pause'
                elif gameStatus=='End':
                    game_framework.quit()
        elif e.type == SDL_MOUSEMOTION:
            if gameStatus=='Pause':
                tx, ty= e.x, 600-e.y
                if tx>330 and tx<470 and ty>310 and ty<350 and button1==0:
                    button1=1
                    button.play()
                elif tx<=330 or tx>=470 or ty<=310 or ty>=350:
                    button1=0
                if tx>340 and tx<460 and ty>255 and ty<295 and button2==0:
                    button2 = 1
                    button.play()
                elif tx<=340 or tx>=460 or ty<=255 or ty>=295:
                    button2 = 0
                if tx > 363 and tx < 437 and ty > 200 and ty < 240 and button3==0:
                    button3 = 1
                    button.play()
                elif tx <= 363 or tx >= 437 or ty <= 200 or ty >= 240:
                    button3 = 0
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT and gameStatus=='Pause':
                tx, ty = e.x, 600 - e.y
                if tx>330 and tx<470 and ty>310 and ty<350:
                    gameStatus='Run'
                    loadtimer.timer.cancel()
                    loadtimer.ttimer.cancel()
                    loadtimer.ktimer.cancel()
                    loadtimer.gtimer.cancel()
                    loadtimer.startTimer()
                    loadtimer.totalTimer()
                    loadtimer.kittyTimer()
                    loadtimer.guideTimer()
                if tx>340 and tx<460 and ty>255 and ty<295:
                    initAll()
                if tx > 363 and tx < 437 and ty > 200 and ty < 240:
                    game_framework.quit()
            elif e.button == SDL_BUTTON_LEFT and gameStatus=='Run':
                tx, ty = e.x, 600 - e.y
                x, y= -1, -1
                for i in range(8):
                    if tx>=(i-1)*58+195+29 and tx<i*58+195+29:
                        x=i
                for j in range(8):
                    if ty>=(j-1)*58+55+29 and ty<j*58+55+29:
                        y=j
                if (mode=='AI' and nowTurn == 'bean') or mode=='PVP':
                    if x<=7 and x>=0 and y<=7 and y>=0 and board[y][x]=='None':
                        if reverse.checkReverse(x,y)!=0:
                            game_world.add_object(Horse(x, y),game_world.layer_horse)
                            reverse.reverse(x, y)
                            reverse.hpSystem()
                            loadtimer.hitstate=0
                            loadtimer.hitTimer()
                            loadtimer.timer.cancel()
                            loadtimer.time = 16
                            loadtimer.startTimer()
                            if checkover.checkOver()==False:
                                gameStatus = 'End'
                            loadtimer.gtimer.cancel()
                            game_world.clear_layer(game_world.layer_guide)
                            guide.guidefunc()
                            loadtimer.guideTimer()

def randompos():
    ranNum = random.randint(0,len(game_world.objects[game_world.layer_guide])-1)
    randX = game_world.objects[game_world.layer_guide][ranNum].x
    randY = game_world.objects[game_world.layer_guide][ranNum].y
    game_world.add_object(Horse(randX, randY), game_world.layer_horse)
    reverse.reverse(randX, randY)

def enter():
    global bgm2, nowTurn, button

    bgm2 = load_music('game_music.mp3')
    bgm2.set_volume(10)
    bgm2.repeat_play()
    button = load_wav('button.wav')
    button.set_volume(100)
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
    loadtimer.reverseTimer()

def draw():
    clear_canvas()
    game_world.draw()
    imageloader.draw()
    update_canvas()

def update():
    if mode=='AI':
        loadtimer.AI()
    imageloader.update()
    game_world.update()

def exit():
    pass

def initAll():
    global nowTurn, board, gameStatus, beanHp, chickHp
    beanHp = 10000
    chickHp = 10000
    loadtimer.hitstate=12
    imageloader.beanAnimHp = 10000
    imageloader.chickAnimHp = 10000
    loadtimer.ttimer.cancel()
    loadtimer.ktimer.cancel()
    loadtimer.readytimer.cancel()
    loadtimer.timer.cancel()
    loadtimer.gtimer.cancel()
    game_world.clear_layer(game_world.layer_guide)
    game_world.clear_layer(game_world.layer_horse)
    game_world.clear_layer(game_world.layer_hurdle)
    bgm2.repeat_play()
    gameStatus='Ready'
    loadtimer.time = 16
    loadtimer.ttime = 900
    loadtimer.rtime = 4
    loadtimer.kittystate = 0
    loadtimer.readyTimer()
    for i in range(8):
        for j in range(8):
            board[i][j] = 'None'  # 돌 중복해서 놓지 못하게
    # 장애물 생성
    for i in range(5):
        game_world.add_object(Hurdle(ran_list[random.randint(0, 5)], ran_list[random.randint(0, 5)]),
                              game_world.layer_hurdle)
    # 말 중앙 좌표에 놓기
    nowTurn = 'chick'
    game_world.add_object(Horse(3, 4), game_world.layer_horse)
    game_world.add_object(Horse(4, 3), game_world.layer_horse)
    nowTurn = 'bean'
    game_world.add_object(Horse(3, 3), game_world.layer_horse)
    game_world.add_object(Horse(4, 4), game_world.layer_horse)
    guide.guidefunc()

if __name__=='__main__':
     import sys 
     current_module = sys.modules[__name__]   
     open_canvas() 
     game_framework.run(current_module) 
     close_canvas() 
