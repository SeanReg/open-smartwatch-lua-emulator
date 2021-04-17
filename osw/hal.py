from osw.canvas import Canvas
from pygame import Surface
from pygame import key
import pygame
from datetime import datetime

class OswHal:
    def __init__(self, screen: Surface):
        self.canvas = Canvas(screen)
        
        self.buttonState = {
            pygame.K_1: 0,
            pygame.K_2: 1,
            pygame.K_3: 2
        }

        self.lastButtonState = self.buttonState.copy()

    def getCanvas(self):
        return self.canvas

    def btn1Down(self):
        return self.buttonState[pygame.K_1]

    def btn2Down(self):
        return self.buttonState[pygame.K_2]

    def btn3Down(self):
        return self.buttonState[pygame.K_3]

    def getLocalTime(self):
        return datetime.now().timestamp()

    def flushCanvas(self):
        pygame.display.flip()

    def checkButtons(self):
        for k in self.buttonState.keys():
            if key.get_pressed()[k] != self.lastButtonState[k]:
                self.buttonState[k] = key.get_pressed()[k]
            else:
                self.buttonState[k] = 0
            
            self.lastButtonState[k] = key.get_pressed()[k]

        
        
