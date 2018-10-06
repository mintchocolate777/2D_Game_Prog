from pico2d import *
import game_framework
import random
import title_state

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400,30)

class Boy:
    image=None
    def __init__(self):
        print("Creating..")
        self.x,self.y=random.randint(0,200),random.randint(90,550)
        self.speed=random.uniform(1.0,3.0)
        self.frame=random.randint(0,7)
        self.waypoints=[]
        self.wp=load_image('wp.png')
        self.state=3
        if Boy.image==None:
            Boy.image=load_image('animation_sheet.png')


    def draw(self):
        for wp in self.waypoints:
            self.wp.draw(wp[0],wp[1])
        Boy.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)

    def update(self):
        self.frame = (self.frame+1)%8
        if len(self.waypoints)>0:
            (tx,ty)=self.waypoints[0]
            dx,dy=tx-self.x,ty-self.y
            dist = math.sqrt(dx**2+dy**2)
            if dx>0: self.state=1
            elif dx<0: self.state=0
            if dist>0:
                self.x+=self.speed*dx/dist
                self.y+=self.speed*dy/dist
                if dx<0 and self.x<tx: self.x=tx
                if dx>0 and self.x>tx: self.x=tx
                if dy<0 and self.y<ty: self.y=ty
                if dy>0 and self.y>ty: self.y=ty
                if(self.x,self.y)==(tx,ty):
                    del self.waypoints[0]
                    self.state+=2

span=50
def handle_events():
    global boys
    global span
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif e.key in range(SDLK_1,SDLK_9+1):
                span = 20*(e.key-SDLK_0)
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button ==SDL_BUTTON_LEFT:
                tx,ty=e.x,600-e.y
                for b in boys:
                    bx=tx+random.randint(-span,span)
                    by=ty+random.randint(-span,span)
                    b.waypoints+=[(bx,by)]
            else:
                for b in boys:
                    b.waypoints = []
                    b.state+=2

def enter():
    global boys, grass
    boys=[Boy() for i in range(1000)]
    grass=Grass()

def draw():
    global grass, boys
    clear_canvas()
    grass.draw()
    for b in boys:
        b.draw()
    update_canvas()

def update():
    global boys
    for b in boys:
        b.update()
    delay(0.01)

#fill here


def exit():
    pass

if __name__=='__main__':
   import sys
   current_module=sys.modules[__name__]
   open_canvas()
   game_framework.run(current_module)
   close_canvas()