from pico2d import *
import game_framework
import game_state

def enter():
    global image, bgm, button, buttonwav, bt1state, bt2state, explain, explainstate, bt, bt1, bt2, bt3, bt4, start, startstate
    image = load_image('title.png')
    button = load_image('titlebutton.png')
    bgm=load_music('title_music.mp3')
    bgm.set_volume(70)
    bgm.repeat_play()
    buttonwav = load_wav('button.wav')
    buttonwav.set_volume(100)
    bt1state=0
    bt2state=0
    explain=[]
    explain.append(load_image('설명1.png'))
    explain.append(load_image('설명2.png'))
    explain.append(load_image('설명3.png'))
    explain.append(load_image('설명4.png'))
    explain.append(load_image('설명5.png'))
    explain.append(load_image('설명6.png'))
    explain.append(load_image('설명7.png'))
    explain.append(load_image('설명8.png'))
    explain.append(load_image('설명9.png'))
    explain.append(load_image('설명10.png'))
    explain.append(load_image('설명11.png'))
    explain.append(load_image('설명12.png'))
    explainstate=-1
    bt=[]
    bt.append(load_image('bt1.png'))
    bt.append(load_image('bt2.png'))
    bt.append(load_image('bt3.png'))
    bt.append(load_image('bt4.png'))
    start=[]
    start.append(load_image('시작1.png'))
    start.append(load_image('시작2.png'))
    startstate=-1
    bt1=False
    bt2=False
    bt3=False
    bt4=False


def exit():
    global image, bgm
    del(image)
    del(bgm)

def draw():
    clear_canvas()
    image.draw(400,300)
    button.clip_draw(bt1state*223,0,222,64,243,65)
    button.clip_draw(bt2state*223,64,222,64,563,65)
    if explainstate>-1 and explainstate<12:
        explain[explainstate].draw(400,300)
        if bt1==True:
            bt[0].draw(195,221)
        if bt2==True:
            bt[1].draw(632,221)
        if bt3==True and explainstate>0:
            bt[2].draw(432,254)
        if bt4==True and explainstate<11:
            bt[3].draw(483,254)
    if startstate >= 0:
        start[startstate].draw(400,300)
        if bt1 == True:
            bt[0].draw(195, 221)
        if bt2 == True:
            bt[1].draw(632, 221)
        if bt4 == True:
            bt[3].draw(483, 254)
    update_canvas()

def update():
    delay(0.03)
    
def handle_events():
    global bt1state, bt2state, explainstate, bt1, bt2, bt3, bt4, startstate
    events=get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            if event.key == SDLK_SPACE and startstate>=0:
                if startstate == 0:
                    game_state.mode = 'AI'
                elif startstate == 1:
                    game_state.mode = 'PVP'
                game_framework.push_state(game_state)
            elif event.key == SDLK_UP:
                startstate = 0
            elif event.key ==SDLK_DOWN:
                startstate = 1
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            tx, ty = event.x, 600 - event.y
            if tx>=131 and tx<=354 and ty>=32 and ty<=98 and bt1state==0:
                bt1state=1
                buttonwav.play()
            elif tx<131 or tx>354 or ty<32 or ty>98:
                bt1state=0
            if tx>=452 and tx<=674 and ty>=32 and ty<=98 and bt2state==0:
                bt2state=1
                buttonwav.play()
            elif tx<452 or tx>674 or ty<32 or ty>98:
                bt2state=0
            if (explainstate>=0 and explainstate<=11) or startstate>=0:
                if tx > 147 and tx < 243 and ty > 211 and ty < 231 and bt1==False:
                    bt1=True
                    buttonwav.play()
                elif tx<=147 or tx>=243 or ty<=211 or ty>=231:
                    bt1=False
                if tx > 610 and tx < 654 and ty > 211 and ty < 231 and bt2==False:
                    bt2=True
                    buttonwav.play()
                elif tx<=610 or tx>=654 or ty<=211 or ty>=231:
                    bt2=False
                if explainstate>0 and tx>411 and tx<455 and ty>244 and ty<264 and bt3==False:
                    bt3=True
                    buttonwav.play()
                elif tx<=411 or tx>=455 or ty<=244 or ty>=264:
                    bt3=False
                if explainstate<11 and tx>461 and tx<505 and ty>244 and ty<264 and bt4==False:
                    bt4=True
                    buttonwav.play()
                elif tx<=461 or tx>=505 or ty<=244 or ty>=264:
                    bt4=False
            if startstate>=0:
                if tx>177 and tx<273 and ty>290 and ty<310:
                    startstate=1
                elif tx>177 and tx<273 and ty>310 and ty<330:
                    startstate=0


        elif event.type == SDL_MOUSEBUTTONDOWN:
            tx, ty = event.x, 600 - event.y
            if event.button == SDL_BUTTON_LEFT:
                if tx >= 131 and tx <= 354 and ty >= 32 and ty <= 98:
                    startstate=0
                if tx>=452 and tx<=674 and ty>=32 and ty<=98:
                    explainstate=0
                if explainstate>=0 and explainstate<=11:
                    if tx>147 and tx<243 and ty>211 and ty<231:
                        explainstate=-1
                    if tx>610 and tx<654 and ty>211 and ty<231:
                        explainstate=-1
                    if explainstate > 0 and tx > 411 and tx < 455 and ty > 244 and ty < 264:
                        explainstate-=1
                    if explainstate < 11 and tx > 461 and tx < 505 and ty > 244 and ty < 264:
                        explainstate+=1
                if startstate>=0:
                    if tx>147 and tx<243 and ty>211 and ty<231:
                        startstate=-1
                    if tx>610 and tx<654 and ty>211 and ty<231:
                        if startstate==0:
                            game_state.mode = 'AI'
                        elif startstate==1:
                            game_state.mode = 'PVP'
                        game_framework.push_state(game_state)
                    if explainstate < 11 and tx > 461 and tx < 505 and ty > 244 and ty < 264:
                        if startstate==0:
                            game_state.mode = 'AI'
                        elif startstate==1:
                            game_state.mode = 'PVP'
                        game_framework.push_state(game_state)
                    if tx > 177 and tx < 273 and ty > 290 and ty < 310:
                        game_state.mode = 'PVP'
                        game_framework.push_state(game_state)
                    elif tx > 177 and tx < 273 and ty > 310 and ty < 330:
                        game_state.mode = 'AI'
                        game_framework.push_state(game_state)

def pause():
    pass

def resume():
    pass

if __name__=='__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
