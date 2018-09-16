from pico2d import *

open_canvas()

grass=load_image('grass.png')
character = load_image('run_animation.png')

frame = 0

x=0
y=90

while(1):
    while(x<800):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x,y)
        frame=(frame+1)%8
        update_canvas()
        x=x+2
        delay(0.05)
        get_events()

    while(y<600):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x,y)
        frame=(frame+1)%8
        update_canvas()
        y=y+2
        delay(0.05)
        get_events()

    while(x>0):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x,y)
        frame=(frame+1)%8
        update_canvas()
        x=x-2
        delay(0.05)
        get_events()

    while(y>90):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x,y)
        frame=(frame+1)%8
        update_canvas()
        y=y-2
        delay(0.05)
        get_events()
    
close_canvas()
                       
