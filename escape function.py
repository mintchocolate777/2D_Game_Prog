def handle_events():
    global running

    events=get_events()
    for e in events:
        if e.type==SDL_QUIT:
            running=False
        elif e.type == SDL_KEYDOWN and e.key==SDLK_ESCAPE:
            running=False
