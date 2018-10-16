from pico2d import *
import game_framework
import random
import threading

nowTurn='bean'

board=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        board[i][j]='none'  # 돌 중복해서 놓지 못하게

ran_list = [0,1,2,5,6,7]
time=15

class Map:
    image=None
    def __init__(self):
        if Map.image==None:
            Map.image=load_image('보오오드.png')
    def draw(self):
        Map.image.draw(400,300)

class Horse:
    global board
    image=None
    def __init__(self,x,y):
        if nowTurn=='bean':
            self.frame=0
        else:
            self.frame=3
        if Horse.image==None:
            Horse.image=load_image('콩닭애니메이션.png')
        self.x=x
        self.y=y
        board[self.y][self.x]=nowTurn

    def draw(self):
        Horse.image.clip_draw(self.frame*57,0,57,57,self.x*58+195,self.y*58+55)

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
        Hurdle.image.draw(self.x*58+195,self.y*58+55)
    def update(self):
        pass

def handle_events():
    global horses, nowTurn, board, time, timer
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.quit()
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                tx, ty = e.x, 600 - e.y
                x, y= -1, -1
                for i in range(8):
                    if tx>=(i-1)*58+195+29 and tx<i*58+195+29:
                        x=i
                for j in range(8):
                    if ty>=(j-1)*58+55+29 and ty<j*58+55+29:
                        y=j
                if x<=7 and x>=0 and y<=7 and y>=0 and board[y][x]=='none':
                    horses.append(Horse(x, y))
                    timer.cancel()
                    time=15
                    startTimer()
                    if nowTurn=='bean':
                        nowTurn='chick'
                    else:
                        nowTurn='bean'



def enter():
    global map, hurdles, horses, nowTurn, board
    loadTimeImage()
    map=Map()
    #장애물 생성
    hurdles = []
    hurdles.append(Hurdle(ran_list[random.randint(0,5)], ran_list[random.randint(0,5)]))
    hurdles.append(Hurdle(ran_list[random.randint(0,5)], ran_list[random.randint(0,5)]))
    hurdles.append(Hurdle(ran_list[random.randint(0,5)], ran_list[random.randint(0,5)]))
    hurdles.append(Hurdle(ran_list[random.randint(0,5)], ran_list[random.randint(0,5)]))
    hurdles.append(Hurdle(ran_list[random.randint(0,5)], ran_list[random.randint(0,5)]))

    #말 중앙 좌표에 놓기
    horses = []
    horses.append(Horse(3, 3))
    horses.append(Horse(4, 4))
    nowTurn='chick'
    horses.append(Horse(3, 4))
    horses.append(Horse(4, 3))
    nowTurn='bean'
    startTimer()

def draw():
    global map, hurdles, horses, nowTurn, timeImage, timeImage2
    clear_canvas()
    map.draw()
    for h in hurdles:
        h.draw()
    for i in horses:
        i.draw()
    if nowTurn=='bean':
        timeImage[time%10].draw(413,542)
        if time>=10:
            timeImage[1].draw(383,542)
        else:
            timeImage[0].draw(383,542)
    else:
        timeImage2[time % 10].draw(413, 542)
        if time >= 10:
            timeImage2[1].draw(383, 542)
        else:
            timeImage2[0].draw(383, 542)
    update_canvas()

def startTimer():
    global time, nowTurn, timer
    time-=1
    timer = threading.Timer(1, startTimer)
    timer.start()
    if time==-1:
        timer.cancel()
        time=15
        if nowTurn=='bean':
            nowTurn='chick'
        else:
            nowTurn='bean'
        startTimer()

def loadTimeImage():
    global timeImage, timeImage2
    timeImage=[]
    timeImage.append(load_image('콩0.png'))
    timeImage.append(load_image('콩1.png'))
    timeImage.append(load_image('콩2.png'))
    timeImage.append(load_image('콩3.png'))
    timeImage.append(load_image('콩4.png'))
    timeImage.append(load_image('콩5.png'))
    timeImage.append(load_image('콩6.png'))
    timeImage.append(load_image('콩7.png'))
    timeImage.append(load_image('콩8.png'))
    timeImage.append(load_image('콩9.png'))
    timeImage2=[]
    timeImage2.append(load_image('닭0.png'))
    timeImage2.append(load_image('닭1.png'))
    timeImage2.append(load_image('닭2.png'))
    timeImage2.append(load_image('닭3.png'))
    timeImage2.append(load_image('닭4.png'))
    timeImage2.append(load_image('닭5.png'))
    timeImage2.append(load_image('닭6.png'))
    timeImage2.append(load_image('닭7.png'))
    timeImage2.append(load_image('닭8.png'))
    timeImage2.append(load_image('닭9.png'))


def update():
    pass

def exit():
    pass

if __name__=='__main__':
     import sys 
     current_module = sys.modules[__name__]   
     open_canvas() 
     game_framework.run(current_module) 
     close_canvas() 
