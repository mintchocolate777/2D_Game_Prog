from pico2d import *

speed=2

def handle_events():
    global running
    global dir

    events=get_events()
    for e in events:
        if e.type==SDL_QUIT:
            running=False
        elif e.type == SDL_KEYDOWN:
            if e.key==SDLK_ESCAPE:
                running=False
            elif e.key == SDLK_LEFT:
                dir-=1
            elif e.key == SDLK_RIGHT:
                dir+=1
        elif e.type == SDL_KEYUP:
            if e.key==SDLK_RIGHT:
                dir-=1
            elif e.key==SDLK_LEFT:
                dir+=1


open_canvas()

grass=load_image('grass.png')
character=load_image('run_animation.png')

running =True
x=800//2
frame=0
dir=0

while running:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,90)
    update_canvas()
    handle_events()
    frame=(frame+1)%8
    x+=dir*5
    delay(0.01)

