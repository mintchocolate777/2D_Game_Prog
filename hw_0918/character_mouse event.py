from pico2d import *

speed=5

KPU_WIDTH, KPU_HEIGHT=800,600

def handle_events():
    global running
    global x,y
    global nextX, nextY

    events=get_events()
    for e in events:
        if e.type==SDL_QUIT:
            running=False
        elif e.type == SDL_MOUSEMOTION:
            nextX,nextY=e.x,KPU_HEIGHT-1-e.y
        elif e.type == SDL_KEYDOWN and e.key==SDLK_ESCAPE:
            running=False

open_canvas(KPU_WIDTH,KPU_HEIGHT)
grass = load_image('grass.png')
character=load_image('run_animation.png')

running =True
x,y=KPU_WIDTH//2, KPU_HEIGHT//2
nextX, nextY=x,y
frame=0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*100,0,100,100,x,y)
    update_canvas()
    frame=(frame+1)%8
    if(x>nextX):
        x-=speed
    elif(x<nextX):
        x+=speed
    if(y>nextY):
        y-=speed
    elif(y<nextY):
        y+=speed
    delay(0.01)
    handle_events()

