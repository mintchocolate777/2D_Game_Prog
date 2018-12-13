from pico2d import *
import game_state
import loadtimer
import checkover

beanAnimHp=10000
chickAnimHp=10000

def exit():
    global timeImage, timeImage2, timeImage3, beanImage, chickImage, winImage, loseImage, kittyImage, kittyImage2
    global pauseImage, quitImage, restartImage, continueImage, timebarImage, hpImage, hitImage
    del(timeImage)
    del(timeImage2)
    del(timeImage3)
    del(beanImage)
    del(chickImage)
    del(winImage)
    del(loseImage)
    del(kittyImage)
    del(kittyImage2)
    del(pauseImage)
    del(quitImage)
    del(restartImage)
    del(continueImage)
    del(timebarImage)
    del(hpImage)
    del(hitImage)

def loadImage():
    global timeImage, timeImage2, timeImage3, beanImage, chickImage, winImage, loseImage, kittyImage, kittyImage2
    global pauseImage, quitImage, restartImage, continueImage, timebarImage, hpImage, hitImage
    timeImage=[]
    timeImage.append(load_image('image/콩0.png'))
    timeImage.append(load_image('image/콩1.png'))
    timeImage.append(load_image('image/콩2.png'))
    timeImage.append(load_image('image/콩3.png'))
    timeImage.append(load_image('image/콩4.png'))
    timeImage.append(load_image('image/콩5.png'))
    timeImage.append(load_image('image/콩6.png'))
    timeImage.append(load_image('image/콩7.png'))
    timeImage.append(load_image('image/콩8.png'))
    timeImage.append(load_image('image/콩9.png'))
    timeImage2=[]
    timeImage2.append(load_image('image/닭0.png'))
    timeImage2.append(load_image('image/닭1.png'))
    timeImage2.append(load_image('image/닭2.png'))
    timeImage2.append(load_image('image/닭3.png'))
    timeImage2.append(load_image('image/닭4.png'))
    timeImage2.append(load_image('image/닭5.png'))
    timeImage2.append(load_image('image/닭6.png'))
    timeImage2.append(load_image('image/닭7.png'))
    timeImage2.append(load_image('image/닭8.png'))
    timeImage2.append(load_image('image/닭9.png'))
    timeImage3=[]
    timeImage3.append(load_image('image/start.png'))
    timeImage3.append(load_image('image/1.png'))
    timeImage3.append(load_image('image/2.png'))
    timeImage3.append(load_image('image/3.png'))

    beanImage = load_image('image/bean.png')
    chickImage=load_image('image/chick.png')
    winImage = load_image('image/win.png')
    loseImage = load_image('image/lose.png')
    kittyImage=load_image('image/leftkitty.png')
    kittyImage2 = load_image('image/rightkitty.png')

    pauseImage = load_image('image/pause.png')
    quitImage=[]
    quitImage.append(load_image('image/quit.png'))
    quitImage.append(load_image('image/quit2.png'))
    restartImage=[]
    restartImage.append(load_image('image/restart.png'))
    restartImage.append(load_image('image/restart2.png'))
    continueImage=[]
    continueImage.append(load_image('image/continue.png'))
    continueImage.append(load_image('image/continue2.png'))

    timebarImage=[]
    timebarImage.append(load_image('image/콩 체력바.png'))
    timebarImage.append(load_image('image/닭 체력바.png'))

    hpImage=[]
    hpImage.append(load_image('image/hp0.png'))
    hpImage.append(load_image('image/hp1.png'))
    hpImage.append(load_image('image/hp2.png'))
    hpImage.append(load_image('image/hp3.png'))
    hpImage.append(load_image('image/hp4.png'))
    hpImage.append(load_image('image/hp5.png'))
    hpImage.append(load_image('image/hp6.png'))
    hpImage.append(load_image('image/hp7.png'))
    hpImage.append(load_image('image/hp8.png'))
    hpImage.append(load_image('image/hp9.png'))

    hitImage=load_image('image/hit.png')

def update():
    global beanAnimHp, chickAnimHp
    if game_state.beanHp<beanAnimHp:
        beanAnimHp-=1
    if game_state.chickHp<chickAnimHp:
        chickAnimHp-=1

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
        timebarImage[0].clip_draw_to_origin(0,0, (int)(328*beanAnimHp/10000), 27, 26+(int)(328*(10000-beanAnimHp)/10000), 529)
        timebarImage[1].clip_draw_to_origin(0,0,(int)(328*chickAnimHp/10000),27,445,529)
        if game_state.beanHp>=10000:
            hpImage[1].draw(43,467)
        if game_state.beanHp>=1000:
            hpImage[(int)((game_state.beanHp%10000)/1000)].draw(63,467)
        if game_state.beanHp>=100:
            hpImage[(int)((game_state.beanHp%1000)/100)].draw(83,467)
        if game_state.beanHp >= 100:
            hpImage[(int)((game_state.beanHp % 100) / 10)].draw(103, 467)
        hpImage[game_state.beanHp % 10].draw(123, 467)

        if game_state.chickHp >= 10000:
            hpImage[1].draw(677, 467)
        if game_state.chickHp >= 1000:
            hpImage[(int)((game_state.chickHp % 10000) / 1000)].draw(697, 467)
        if game_state.chickHp >= 100:
            hpImage[(int)((game_state.chickHp % 1000) / 100)].draw(717, 467)
        if game_state.chickHp >= 10:
            hpImage[(int)((game_state.chickHp % 100) / 10)].draw(737, 467)
        hpImage[game_state.chickHp % 10].draw(757, 467)
        if loadtimer.hitstate!=12:
            if game_state.nowTurn=='chick':
                hitImage.clip_draw(loadtimer.hitstate*170,0,170,170, 710, 350)
            else:
                hitImage.clip_draw(loadtimer.hitstate * 170, 0, 170, 170, 90, 350)

    if loadtimer.rtime>-1:
        timeImage3[loadtimer.rtime].draw(400,300)
    if game_state.gameStatus=='End':
        if game_state.mode=='PVP':
            winImage.draw(400,260)
            if checkover.outcome()=='bean':
                beanImage.draw(400,200)
            else:
                chickImage.draw(400,200)
        elif game_state.mode=='AI':
            if checkover.outcome()=='bean':
                winImage.draw(400,300)
            else:
                loseImage.draw(400,300)
    if game_state.gameStatus=='Pause':
        pauseImage.draw(400,300)
        continueImage[game_state.button1].draw(400,330)
        restartImage[game_state.button2].draw(400, 275)
        quitImage[game_state.button3].draw(400,220)
