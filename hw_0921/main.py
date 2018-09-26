from pico2d import *
import random

def handle_events():
    global waypoints
    global running
    events = get_events()
    for event in events:
        
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running=False
        elif event.type ==SDL_MOUSEBUTTONDOWN:
            if event.button==1:
                tx,ty=event.x,600-1-event.y
                waypoints+=[(tx,ty)]
            else:
                waypoints=[]
            
class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        print("Creating..")
        self.x,self.y=random.randint(0,750),random.randint(90,550)
        self.speed=random.uniform(1.0,5.0)
        self.frame=random.randint(0,7)
        self.image=load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

    def update(self):
        if len(waypoints)>0:
            (tx,ty)=waypoints[0]
            self.frame=(self.frame + 1) % 8
            dx,dy=tx-self.x,ty-self.y
            dist = math.sqrt(dx**2+dy**2)
            if dist!=0:
                self.x+=self.speed*dx/dist
                self.y+=self.speed*dy/dist
                if dx<0 and self.x<tx: self.x=tx
                if dx>0 and self.x>tx: self.x=tx
                if dy<0 and self.y<ty: self.y=ty
                if dy>0 and self.y>ty: self.y=ty
            if(self.x,self.y)==(tx,ty):
                del waypoints[0]

open_canvas()

g=Grass()
boys=[Boy() for i in range (20)]
waypoints=[]    
running=True

while running:
    handle_events()
    
    for b in boys:
        b.update()
        
    clear_canvas()
    g.draw()
    
    for b in boys:
        b.draw()
    update_canvas()

    delay(0.03)

close_canvas()
