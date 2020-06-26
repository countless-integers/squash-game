import pygame


class Paddle:

    def __init__(self, screen, y=None, width=20, height=100):
        self.screen = screen
        if y is None:
            y = screen.height // 2
        self.y = y
        self.width = width
        self.height = height
        self.shape = None

    def show(self, color=None) -> None:
        if color is None:
            color = self.screen.fg_color
        self.shape = pygame.Rect(
            (self.screen.width - self.width, self.y - self.height // 2),
            (self.width, self.height)
        )
        pygame.draw.rect(self.screen.display, color, self.shape)

    def hide(self) -> None:
        self.show(self.screen.bg_color)

    def update(self) -> None:
        self.hide()
        self.y = pygame.mouse.get_pos()[1]
        self.show()
