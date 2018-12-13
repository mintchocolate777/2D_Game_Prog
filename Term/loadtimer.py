import threading
import game_world
import guide
import game_state
import checkover
import reverse

time=16
ttime=900
rtime=4
kittystate = 0
hitstate=12

def exit():
    global ttimer, ktimer, readytimer, gtimer, hittimer, timer, revtimer
    ttimer.cancel()
    ktimer.cancel()
    readytimer.cancel()
    gtimer.cancel()
    hittimer.cancel()
    timer.cancel()
    revtimer.cancel()

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
        guideTimer()
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
                game_state.gameStatus = 'End'
            gtimer.cancel()
            guide.guidefunc()
            guideTimer()

def hitTimer():
    global hitstate, hittimer
    hitstate+=1
    hittimer=threading.Timer(0.05,hitTimer)
    hittimer.start()
    if hitstate>=12:
        hittimer.cancel()

def guideTimer():
    global gtimer
    if game_state.gameStatus == 'Run':
        for i in range(0,len(game_world.objects[game_world.layer_guide])):
            game_world.objects[game_world.layer_guide][i].frame += 1
            game_world.objects[game_world.layer_guide][i].frame = game_world.objects[game_world.layer_guide][i].frame % 9
        gtimer=threading.Timer(0.1, guideTimer)
        gtimer.start()

def reverseTimer():
    global revtimer
    #if game_state.gameStatus=='Run':
    for i in range(0,len(game_world.objects[game_world.layer_horse])):
        if game_state.board[game_world.objects[game_world.layer_horse][i].y][game_world.objects[game_world.layer_horse][i].x]=='bean'and game_world.objects[game_world.layer_horse][i].frame!=0:
            if game_world.objects[game_world.layer_horse][i].frame==3:
                game_world.objects[game_world.layer_horse][i].rev_sound.play()
            game_world.objects[game_world.layer_horse][i].frame+=1
            game_world.objects[game_world.layer_horse][i].frame=game_world.objects[game_world.layer_horse][i].frame%6
        elif game_state.board[game_world.objects[game_world.layer_horse][i].y][game_world.objects[game_world.layer_horse][i].x]=='chick' and game_world.objects[game_world.layer_horse][i].frame!=3:
            if game_world.objects[game_world.layer_horse][i].frame == 0:
                game_world.objects[game_world.layer_horse][i].rev_sound.play()
            game_world.objects[game_world.layer_horse][i].frame+=1
            game_world.objects[game_world.layer_horse][i].frame=game_world.objects[game_world.layer_horse][i].frame%6
    revtimer=threading.Timer(0.1,reverseTimer)
    revtimer.start()

def AI():
    global time, hitstate
    if game_state.nowTurn == 'chick' and game_state.gameStatus != 'End' and time == 12:
        game_state.randompos()
        reverse.hpSystem()
        hitstate = 0
        hitTimer()
        timer.cancel()
        time = 16
        startTimer()
        if checkover.checkOver() == False:
            game_state.gameStatus = 'End'
        gtimer.cancel()
        game_world.clear_layer(game_world.layer_guide)
        guide.guidefunc()
        guideTimer()