from pygame import Surface, Rect
from pygame import draw
import math
import pygame

def toRGB888(color):
    r = ((((color >> 11) & 0x1F) * 527) + 23) >> 6;
    g = ((((color >> 5) & 0x3F) * 259) + 33) >> 6;
    b = (((color & 0x1F) * 527) + 23) >> 6;

    return (r, g, b)

class Print:
    def __init__(self, screen: Surface):
        pygame.font.init()
        self.surface = screen
        self.cursorX = 0
        self.cursorY = 0
        self.color = (255, 255, 255)
        self.font = pygame.font.SysFont('Verdana', 10)

    def print(self, str):
        text = self.font.render(f"{str}", False, self.color)
        self.surface.blit(text, (self.cursorX, self.cursorY))
        w, h = self.font.size(f"{str}")
        self.cursorX = self.cursorX + w

    def println(self, str):
        w, h = self.font.size(f"TEST")
        self.cursorX = 0
        self.cursorY = self.cursorY + h
        self.print(self, str)

    def setCursor(self, x, y):
        self.cursorX = x
        self.cursorY = y

    def setTextColor(self, color):
        self.color = toRGB888(color)

    def setTextSize(self, s):
        self.font = pygame.font.SysFont('Verdana', s * 10)

class Canvas(Print):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.surface = screen

    def drawPixel(self, x, y, color):
        self.surface.set_at((x, y), toRGB888(color))

    def drawFastVLine(self, x, y, h, ucolor):
        draw.line(self.surface, toRGB888(ucolor), (x, y), (x, y + h))

    def drawFastHLine(self, x, y, w, ucolor):
        draw.line(self.surface, toRGB888(ucolor), (x, y), (x + w, y))

    def fillRect(self, x, y, w, h, ucolor):
        draw.rect(self.surface, toRGB888(ucolor), Rect(x, y, w, h))
        
    def fillScreen(self, ucolor):
        self.surface.fill(toRGB888(ucolor))

    def drawLine(self, x0, y0, x1, y1, ucolor):
        draw.line(self.surface, toRGB888(ucolor), (x0, y0), (x1, y1))

    def drawRect(self, x, y, w, h, ucolor):
        draw.rect(self.surface, toRGB888(ucolor), Rect(x, y, w, h), width=1)

    def drawCircle(self, x0, y0, r, ucolor):
        draw.circle(self.surface, toRGB888(ucolor), (x0, y0), r, width=1)

    def fillCircle(self, x0, y0, r, ucolor):
        draw.circle(self.surface, toRGB888(ucolor), (x0, y0), r)
        
    def drawTriangle(self, x0, y0, x1, y1, x2, y2, ucolor):
        draw.polygon(self.surface, toRGB888(ucolor), ((x0, y0), (x1, y1), (x2, y2)), width=1)

    def fillTriangle(self, x0, y0, x1, y1, x2, y2, ucolor):
        draw.polygon(self.surface, toRGB888(ucolor), ((x0, y0), (x1, y1), (x2, y2)))
        

    def drawRoundRect(self, x0, y0, w, h, radius, ucolor):
        draw.rect(self.surface, toRGB888(ucolor), Rect(x0, y0, w, h), border_radius=radius, width=1)

    def fillRoundRect(self, x0, y0, w, h, radius, ucolor):
        draw.rect(self.surface, toRGB888(ucolor), Rect(x0, y0, w, h), border_radius=radius)

    def drawBitmap(self, x, y, bitmap, w, h, ucolor):
        pass
    def drawBitmap(self, x, y, bitmap, w, h, ucolor):
        pass
    def drawXBitmap(self, x, y, bitmap, w, h, ucolor):
        pass
    def drawGrayscaleBitmap(self, x, y, bitmap, mask, w, h):
        pass
    def drawGrayscaleBitmap(self, x, y, bitmap, mask, w, h):
        pass
    def draw16bitRGBBitmap(self, x, y, ubitmap, mask, w, h):
        pass
    def draw16bitRGBBitmap(self, x, y, ubitmap, mask, w, h):
        pass
    def draw24bitRGBBitmap(self, x, y, bitmap, mask, w, h):
        pass
    def draw24bitRGBBitmap(self, x, y, bitmap, mask, w, h):
        pass
    def getTextBounds(self, string, x, y, x1, y1, uw, uh):
        pass
    def getTextBounds(self, s, x, y, x1, y1, uw, uh):
        pass
    def getTextBounds(self, str, x, y, x1, y1, uw, uh):
        pass
    #def setFont(self, const GFXfont f = NULL):
    #    pass

    def drawEllipse(self, x, y, rx, ry, ucolor):
        draw.ellipse(self.surface, toRGB888(ucolor), Rect(x, y, rx, ry), width=1)

    def drawEllipseHelper(self, x, y, rx, ry, cornername, ucolor):
        pass

    def fillEllipse(self, x, y, rx, ry, ucolor):
        draw.ellipse(self.surface, toRGB888(ucolor), Rect(x, y, rx, ry))

    def fillEllipseHelper(self, x, y, rx, ry, cornername, delta, ucolor):
        pass
    
    def drawArc(self, x, y, r1, r2, start, end, ucolor):
        draw.arc(self.surface, toRGB888(ucolor), Rect(x, y, r1, r2), math.degrees(start), math.degrees(end), width=1)

    def fillArc(self, x, y, r1, r2, start, end, ucolor):
        draw.arc(self.surface, toRGB888(ucolor), Rect(x, y, r1, r2), math.degrees(start), math.degrees(end))

    def fillArcHelper(self, cx, cy, oradius, iradius, start, end, ucolor):
        pass


