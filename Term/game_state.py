from pico2d import *
import game_framework

class Map:
    def __init__(self):
        self.image=load_image('보오오드.png')
    def draw(self):
        self.image.draw(400,300)

class Board:
    def __init__(self):
        pass
    def draw(self):
        pass
    def update(self):
        pass

def handle_events():
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.quit()

def enter():
    global map
    map=Map()

def draw():
    global map
    clear_canvas()
    map.draw()
    update_canvas()

def update():
    pass

def exit():
    pass

if __name__=='__main__':
     import sys 
     current_module = sys.modules[__name__]   
     open_canvas() 
     game_framework.run(current_module) 
     close_canvas() 
