from pico2d import *
from math import sin, cos

open_canvas()

grass=load_image('grass.png')
character = load_image('run_animation.png')

frame = 0

x=400
y=315
rad=225
angle=270
nowx=400
nowy=90

while(1):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,nowx,nowy)
    frame=(frame+1)%8
    update_canvas()
    angle=angle%360
    nowx=cos(angle)*rad+x
    nowy=sin(angle)*rad+y
    angle=angle+1
    delay(0.05)
    get_events()
    
close_canvas()
                       
