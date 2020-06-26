import pygame
import random


class Ball:

    radius: int = 10
    x: int = 0
    y: int = 0
    vx: int = 0
    vy: int = 0
    initial_x: int = 0
    initial_y: int = 0
    speed_increment: int = 4
    shape: pygame.Rect = None

    def __init__(self, screen, position=(0, 0), velocity=(0, 0)):
        self.x = self.initial_x = position[0]
        self.y = self.initial_y = position[1]
        self.vx, self.vy = velocity
        self.screen = screen

    def reset(self) -> None:
        self.x = self.initial_x
        self.y = self.initial_y
        self.vx = 0
        self.vy = 0

    def show(self, color=None) -> None:
        if color is None:
            color = self.screen.fg_color
        self.shape = pygame.Rect(
            (self.x - self.radius, self.y - self.radius),
            (self.radius * 2, self.radius * 2)
        )
        pygame.draw.circle(
            self.screen.display,
            color,
            (self.x, self.y),
            self.radius
        )

    def bounce(self) -> None:
        new_direction = random.choice([1, -1])
        self.vx = -self.vx
        self.vy = new_direction * self.vy

    def update(self) -> None:
        new_x = self.x + self.vx
        new_y = self.y + self.vy

        if new_x < self.screen.border + self.radius:
            self.vx = -self.vx
        elif new_y < self.screen.border + self.radius or new_y > self.screen.height - self.screen.border - self.radius:
            self.vy = -self.vy
        else:
            self.show(self.screen.bg_color)
            self.x = new_x
            self.y = new_y
            self.show(self.screen.fg_color)

    def is_colliding_with(self, element) -> bool:
        return self.shape.colliderect(element.shape)

    def is_gone_out(self) -> bool:
        return self.x >= (self.screen.width + self.radius)

    def speed_up(self) -> None:
        if self.vx >= 0:
            self.vx += self.speed_increment
        else:
            self.vx -= self.speed_increment
        if self.vy >= 0:
            self.vy += self.speed_increment
        else:
            self.vy -= self.speed_increment

    def speed_down(self) -> None:
        if self.vx > 0:
            self.vx -= self.speed_increment
        else:
            self.vx += self.speed_increment
        if self.vy > 0:
            self.vy -= self.speed_increment
        else:
            self.vy += self.speed_increment

