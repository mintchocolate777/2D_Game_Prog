from pico2d import *
from math import sin, cos

open_canvas()

grass=load_image('grass.png')
character = load_image('run_animation.png')

frame = 0

x=400
y=315
rad=225
angle=-70
nowx=400
nowy=90

while(1):
    while(nowx<800):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,nowx,nowy)
        frame=(frame+1)%8
        update_canvas()
        nowx=nowx+2
        delay(0.01)
        get_events()
        
    while(nowy<600):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,nowx,nowy)
        frame=(frame+1)%8
        update_canvas()
        nowy=nowy+2
        delay(0.01)
        get_events()

    while(nowx>0):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,nowx,nowy)
        frame=(frame+1)%8
        update_canvas()
        nowx=nowx-2
        delay(0.01)
        get_events()

    while(nowy>90):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,nowx,nowy)
        frame=(frame+1)%8
        update_canvas()
        nowy=nowy-2
        delay(0.01)
        get_events()

    while(nowx<400):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,nowx,nowy)
        frame=(frame+1)%8
        update_canvas()
        nowx=nowx+2
        delay(0.01)
        get_events()

   
    while(angle<220):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,nowx,nowy)
        frame=(frame+1)%8
        update_canvas()
        nowx=cos(angle/45)*rad+x
        nowy=sin(angle/45)*rad+y
        angle=angle+1
        delay(0.01)
        get_events()
    angle=-70
    
close_canvas()

                       
