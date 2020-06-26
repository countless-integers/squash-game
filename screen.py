import pygame


class Screen:

    def __init__(
        self,
        width=1200,
        height=600,
        border=20,
        fg_color="white",
        bg_color="black"
    ):
        self.width = width
        self.height = height
        self.border = border
        self.fg_color = pygame.Color(fg_color)
        self.bg_color = pygame.Color(bg_color)

        self.display = pygame.display.set_mode((width, height))

    def show_borders(self) -> None:
        pygame.draw.rect(self.display, self.fg_color, pygame.Rect(0, 0, self.width, self.border))
        pygame.draw.rect(self.display, self.fg_color, pygame.Rect(0, 0, self.border, self.height))
        pygame.draw.rect(self.display, self.fg_color, pygame.Rect(0, self.height - self.border, self.width, self.border))

    def refresh(self) -> None:
        pygame.display.flip()
