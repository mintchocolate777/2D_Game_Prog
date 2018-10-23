from pico2d import *
import game_framework
import random
import threading

nowTurn='bean'

board=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        board[i][j]='None'  # 돌 중복해서 놓지 못하게

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
        if board[self.y][self.x]=='bean':
            self.frame=0
        else:
            self.frame=3

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

class Guide:
    image=None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if Guide.image == None:
            Guide.image = load_image('guide.png')
    def draw(self):
        Guide.image.draw(self.x * 58 + 195, self.y * 58 + 55)
    def update(self):
        pass

def handle_events():
    global horses, nowTurn, board, time, timer, guide
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
                if x<=7 and x>=0 and y<=7 and y>=0 and board[y][x]=='None':
                    if checkReverse(x,y)!=0:
                        horses.append(Horse(x, y))
                        reverse(x, y)
                        guide=[]
                        timer.cancel()
                        time = 15
                        startTimer()
                        guidefunc()


def enter():
    global map, hurdles, horses, nowTurn, board, guide
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

    guide=[]
    startTimer()
    guidefunc()

def draw():
    global map, hurdles, horses, nowTurn, timeImage, timeImage2, guide
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
    for g in guide:
        g.draw()
    update_canvas()

def startTimer():
    global time, nowTurn, timer, guide
    time-=1
    timer = threading.Timer(1, startTimer)
    timer.start()
    if time==-1:
        timer.cancel()
        guide =[]
        time=15
        if nowTurn=='bean':
            nowTurn='chick'
        else:
            nowTurn='bean'
        startTimer()
        guidefunc()

def reverse(x,y):
    global nowTurn, board
    reversed =0
    reversible = checkReverse(x,y)
    if reversible==0:
        if nowTurn == 'bean':
            nowTurn = 'chick'
        else:
            nowTurn = 'bean'
        return 0
    board[y][x]=nowTurn
    if reversible&1:
        j=y-1
        while board[j][x]!=nowTurn and board[j][x]!='None' and board[j][x]!='hurdle':
            board[j][x]=nowTurn
            reversed+=1
            j-=1
    reversible>>=1

    if reversible&1:
        j=y+1
        while board[j][x] != nowTurn and board[j][x] != 'None' and board[j][x] != 'hurdle':
            board[j][x]=nowTurn
            reversed+=1
            j+=1
    reversible>>=1

    if reversible&1:
        i=x-1
        while board[y][i] != nowTurn and board[y][i] != 'None' and board[y][i] != 'hurdle':
            board[y][i]=nowTurn
            reversed+=1
            i-=1
    reversible>>=1

    if reversible & 1:
        i = x + 1
        while board[y][i] != nowTurn and board[y][i] != 'None' and board[y][i] != 'hurdle':
            board[y][i] = nowTurn
            reversed += 1
            i += 1
    reversible >>= 1

    if reversible&1:
        i=x-1
        j=y-1
        while board[j][i] != nowTurn and board[j][i] != 'None' and board[j][i] != 'hurdle':
            board[j][i] = nowTurn
            reversed += 1
            i -= 1
            j-=1
    reversible>>=1

    if reversible&1:
        i=x+1
        j=y-1
        while board[j][i] != nowTurn and board[j][i] != 'None' and board[j][i] != 'hurdle':
            board[j][i] = nowTurn
            reversed += 1
            i += 1
            j-=1
    reversible>>=1

    if reversible&1:
        i=x-1
        j=y+1
        while board[j][i] != nowTurn and board[j][i] != 'None' and board[j][i] != 'hurdle':
            board[j][i] = nowTurn
            reversed += 1
            i -= 1
            j+=1
    reversible>>=1

    if reversible&1:
        i=x+1
        j=y+1
        while board[j][i] != nowTurn and board[j][i] != 'None' and board[j][i] != 'hurdle':
            board[j][i] = nowTurn
            reversed += 1
            i += 1
            j+=1
    reversible>>=1

    if nowTurn=='bean':
        nowTurn='chick'
    else:
        nowTurn='bean'
    for i in range(0,8,1):
        for j in range(0,8,1):
            if checkReverse(i,j):
                return reversed
    return -1

def guidefunc():
    global nowTurn, board, guide
    for y in range(8):
        for x in range(8):
            reversible = checkReverse(x, y)
            if reversible & 1:
                j = y - 1
                while board[j][x] != nowTurn and board[j][x] != 'None' and board[j][x] != 'hurdle':
                    j -= 1
                if board[y][x]=='None':
                    guide.append(Guide(x, y))
            reversible >>= 1

            if reversible & 1:
                j = y + 1
                while board[j][x] != nowTurn and board[j][x] != 'None' and board[j][x] != 'hurdle':
                    j += 1
                if board[y][x] == 'None':
                    guide.append(Guide(x, y))
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                while board[y][i] != nowTurn and board[y][i] != 'None' and board[y][i] != 'hurdle':
                    i -= 1
                if board[y][x]=='None':
                    guide.append(Guide(x,y))
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                while board[y][i] != nowTurn and board[y][i] != 'None' and board[y][i] != 'hurdle':
                    i += 1
                if board[y][x] == 'None':
                    guide.append(Guide(x, y))
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                j = y - 1
                while board[j][i] != nowTurn and board[j][i] != 'None' and board[j][i] != 'hurdle':
                    i -= 1
                    j -= 1
                if board[y][x] == 'None':
                    guide.append(Guide(x, y))
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                j = y - 1
                while board[j][i] != nowTurn and board[j][i] != 'None' and board[j][i] != 'hurdle':
                    i += 1
                    j -= 1
                if board[y][x] == 'None':
                    guide.append(Guide(x, y))
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                j = y + 1
                while board[j][i] != nowTurn and board[j][i] != 'None' and board[j][i] != 'hurdle':
                    i -= 1
                    j += 1
                if board[y][x] == 'None':
                    guide.append(Guide(x, y))
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                j = y + 1
                while board[j][i] != nowTurn and board[j][i] != 'None' and board[j][i] != 'hurdle':
                    i += 1
                    j += 1
                if board[y][x] == 'None':
                    guide.append(Guide(x, y))
            reversible >>= 1


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

def checkReverse(x, y):
    global board, nowTurn
    result=0
    #남쪽 체크
    if y>1 and board[y-1][x]!=nowTurn and board[y-1][x]!='hurdle' and board[y-1][x]!='None':
        for j in range(y-2,-1,-1):
            if board[j][x]==nowTurn:
                result+=1
                break
            if board[j][x]=='None' or board[j][x]=='hurdle':
                break
    #북쪽 체크
    if y<6 and board[y+1][x]!=nowTurn and board[y+1][x]!='hurdle' and board[y+1][x]!='None':
        for j in range(y+2,8,1):
            if board[j][x]==nowTurn:
                result+=2
                break
            if board[j][x] == 'None' or board[j][x] == 'hurdle':
                break
    #서쪽 체크
    if x>1 and board[y][x-1]!=nowTurn and board[y][x-1]!='hurdle'and board[y][x-1]!='None':
        for i in range(x-2,-1,-1):
            if board[y][i]==nowTurn:
                result+=4
                break
            if board[y][i]=='None' or board[y][i] =='hurdle':
                break
    #동쪽 체크
    if x<6 and board[y][x+1]!=nowTurn and board[y][x+1]!='hurdle'and board[y][x+1]!='None':
        for i in range(x+2, 8, 1):
            if board[y][i]==nowTurn:
                result+=8
                break
            if board[y][i]=='None' or board[y][i]=='hurdle':
                break
    #
    if x>1 and y>1 and board[y-1][x-1]!=nowTurn and board[y-1][x-1]!='hurdle'and board[y-1][x-1]!='None':
        i=x-2
        j=y-2
        while i>=0 and j>=0:
            if board[j][i]==nowTurn:
                result+=16
                break
            if board[j][i]=='None' or board[j][i]=='hurdle':
                break
            i-=1
            j-=1
    #
    if x<6 and y>1 and board[y-1][x+1]!=nowTurn and board[y-1][x+1]!='hurdle'and board[y-1][x+1]!='None':
        i=x+2
        j=y-2
        while i<8 and j>=0:
            if board[j][i]==nowTurn:
                result+=32
                break
            if board[j][i]=='None' or board[j][i]=='hurdle':
                break
            i+=1
            j-=1
    #
    if x>1 and y<6 and board[y+1][x-1]!=nowTurn and board[y+1][x-1]!='hurdle'and board[y+1][x-1]!='None':
        i=x-2
        j=y+2
        while i>=0 and j<8:
            if board[j][i]==nowTurn:
                result+=64
                break
            if board[j][i]=='None' or board[j][i]=='hurdle':
                break
            i-=1
            j+=1
    #
    if x<6 and y<6 and board[y+1][x+1]!=nowTurn and board[y+1][x+1]!='hurdle'and board[y+1][x+1]!='None':
        i=x+2
        j=y+2
        while i<8 and j<8:
            if board[j][i]==nowTurn:
                result+=128
                break
            if board[j][i]=='None' or board[j][i]=='hurdle':
                break
            i+=1
            j+=1
    return result

def update():
    global horses
    for i in horses:
        i.update()

def exit():
    pass

if __name__=='__main__':
     import sys 
     current_module = sys.modules[__name__]   
     open_canvas() 
     game_framework.run(current_module) 
     close_canvas() 
