import pygame
from ball import Ball
from screen import Screen
from paddle import Paddle


pygame.init()

screen = Screen()
screen.show_borders()


paddle = Paddle(screen)
paddle.show()

velocity = 4
ball = Ball(
    screen,
    position=(screen.width - Ball.radius - paddle.width * 2, screen.height // 2)
)
ball.show()

framerate = 60
clock = pygame.time.Clock()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            ball.speed_up()
        if event.button == 3:
            ball.slow_down()

    clock.tick(framerate)

    if ball.is_colliding_with(paddle):
        ball.bounce()
    elif ball.is_gone_out():
        ball.reset()
        ball.show()

    screen.refresh()
    ball.update()
    paddle.update()

pygame.quit()
