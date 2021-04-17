from pygame import surface
import typer
import lupa
from lupa import LuaRuntime
import os
from osw.luaapp import OswLuaApp
import threading
import time
import sys, pygame
from osw.hal import OswHal

def runScript(script, resx, resy, fps):
    lua = LuaRuntime(unpack_returned_tuples=True)

    pygame.init()
    screen = pygame.display.set_mode((resx, resy))

    app = OswLuaApp(script, lua, )
    hal = OswHal(screen)
    app.setup(hal)

    clock = pygame.time.Clock()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        screen.fill((0, 0, 0))

        hal.checkButtons()
        app.loop()
        
        #pygame.display.flip()
        clock.tick(fps)

    app.stop()

def main(luafile: str, resolutionx: int = 240, resolutiony: int = 240, fps: int = 30):
    
    if os.path.exists(luafile):
        script = None
        with open(luafile) as f:
            script = f.read()

        if script:
            runScript(script, resolutionx, resolutiony, fps)
    else:
        print(f"File not found {luafile}")

    pass

if __name__ == "__main__":
    typer.run(main)