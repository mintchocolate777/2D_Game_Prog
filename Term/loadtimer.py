import threading
import game_world
import guide
import game_state
import checkover

time=16
ttime=900
rtime=4
kittystate = 0

def totalTimer():
    global ttime, timer, ttimer
    if game_state.gameStatus=='Run':
        ttime-=1
        ttimer = threading.Timer(1, totalTimer)
        ttimer.start()
        if ttime==0:
            game_state.gameStatus='End'
            ttimer.cancel()

def kittyTimer():
    global kittystate, ktimer
    if game_state.gameStatus=='Run':
        kittystate+=1
        kittystate=kittystate%4
        ktimer=threading.Timer(0.5,kittyTimer)
        ktimer.start()

def readyTimer():
    global rtime, readytimer
    rtime-=1
    readytimer = threading.Timer(1,readyTimer)
    readytimer.start()
    if rtime==0:
        game_state.gameStatus = 'Run'
        totalTimer()
        startTimer()
        kittyTimer()
        if rtime==-1:
            readytimer.cancel()

def startTimer():
    global time, timer
    if game_state.gameStatus=='Run':
        time-=1
        timer = threading.Timer(1, startTimer)
        timer.start()
        if time==0:
            timer.cancel()
            game_state.randompos()
            game_world.clear_layer(game_world.layer_guide)
            time=16
            startTimer()
            if checkover.checkOver() == False:
                gameStatus = 'End'
            guide.guidefunc()
