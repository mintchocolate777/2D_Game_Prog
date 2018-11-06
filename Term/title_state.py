from pico2d import *
import game_framework
import game_state

def enter():
    global image, bgm
    image = load_image('title.png')
    bgm=load_music('title_music.mp3')
    bgm.set_volume(70)
    bgm.repeat_play()


def exit():
    global image, bgm
    del(image)
    del(bgm)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    delay(0.03)
    
def handle_events():
    events=get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key==SDLK_SPACE:
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
