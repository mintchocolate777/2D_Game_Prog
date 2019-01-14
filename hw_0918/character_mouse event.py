from pico2d import *

speed=5

KPU_WIDTH, KPU_HEIGHT=800,600

def handle_events():
    global running
    global x,y
    global tx, ty

    events=get_events()
    for e in events:
        if e.type==SDL_QUIT:
            running=False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button==1:
                tx,ty=e.x,KPU_HEIGHT-1-e.y
                waypoints+=[(tx,ty)]
            else:

        elif e.type == SDL_KEYDOWN and e.key==SDLK_ESCAPE:
            running=False

open_canvas(KPU_WIDTH,KPU_HEIGHT)
grass = load_image('grass.png')
character=load_image('run_animation.png')
wp=load_image('wp.png')

running =True
x,y=KPU_WIDTH//2, KPU_HEIGHT//2
tx,ty=x,y
frame=0

while running:
    clear_canvas()
    grass.draw(400, 30)
    for loc in waypoints:
        wp.draw(loc[0],loc[1])
    character.clip_draw(frame*100,0,100,100,x,y)
    update_canvas()
    handle_events()
    frame=(frame+1)%8
    if len(waypoints)>0:
        (tx,ty)=
    dx, dy=tx-x,ty-y
    dist = math.sqrt(dx**2+dy**2)
    if dist!=0:
        x+=speed*dx/dist
        y+=speed*dy/dist
    if dx<0 and x<tx: x=tx
    if dx>0 and x>tx: x=tx
    if dy<0 and y<ty: y=ty
    if dy>0 and y>ty: y=ty

    
        
    if(x,y)==(tx,ty):
        del waypoints[0]

    delay(0.01)
 

