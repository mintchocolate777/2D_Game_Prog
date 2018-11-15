from pico2d import *
import game_state
import loadtimer
import checkover

def loadImage():
    global timeImage, timeImage2, timeImage3, beanImage, chickImage, winImage, kittyImage, kittyImage2
    global pauseImage, quitImage, restartImage, continueImage
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
    timeImage3=[]
    timeImage3.append(load_image('start.png'))
    timeImage3.append(load_image('1.png'))
    timeImage3.append(load_image('2.png'))
    timeImage3.append(load_image('3.png'))

    beanImage = load_image('bean.png')
    chickImage=load_image('chick.png')
    winImage = load_image('win.png')
    kittyImage=load_image('leftkitty.png')
    kittyImage2 = load_image('rightkitty.png')

    pauseImage = load_image('pause.png')
    quitImage=[]
    quitImage.append(load_image('quit.png'))
    quitImage.append(load_image('quit2.png'))
    restartImage=[]
    restartImage.append(load_image('restart.png'))
    restartImage.append(load_image('restart2.png'))
    continueImage=[]
    continueImage.append(load_image('continue.png'))
    continueImage.append(load_image('continue2.png'))

def draw():
    if game_state.gameStatus!='Ready':
        if game_state.nowTurn=='bean':
            timeImage[loadtimer.time%10].draw(413,542)
            if loadtimer.time>=10:
                timeImage[1].draw(383,542)
            else:
                timeImage[0].draw(383,542)
        else:
            timeImage2[loadtimer.time % 10].draw(413, 542)
            if loadtimer.time >= 10:
                timeImage2[1].draw(383, 542)
            else:
                timeImage2[0].draw(383, 542)
        kittyImage.clip_draw(loadtimer.kittystate*56,0,56,71,80,150)
        kittyImage2.clip_draw(loadtimer.kittystate * 56, 0, 56, 71, 720, 150)
    if loadtimer.rtime>-1:
        timeImage3[loadtimer.rtime].draw(400,300)
    if game_state.gameStatus=='End':
        winImage.draw(400,260)
        if checkover.outcome()=='bean':
            beanImage.draw(400,200)
        else:
            chickImage.draw(400,200)
    if game_state.gameStatus=='Pause':
        pauseImage.draw(400,300)
        continueImage[game_state.button1].draw(400,330)
        restartImage[game_state.button2].draw(400, 275)
        quitImage[game_state.button3].draw(400,220)
