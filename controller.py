from settings import *


class Game:
    def __init__(self):
        self.canvas = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.win = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)

    def run(self):
        self.get_event()
        self.update()
        self.draw()

    def update(self):
        pass

    def draw(self):
        self.canvas.fill(BG)
        self.win.blit(self.canvas, (0, 0))
        pg.display.flip()

    def get_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
