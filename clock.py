import time
import pygame
from math import pi, sin, cos


def getFormatTime(t):
    mins, secs = divmod(t, 60)
    return '{:02d}:{:02d}'.format(mins, secs)


def getRad(angle):
    return angle * pi / 180


# init color
grey_color = (71, 71, 71)
white_color = (255, 255, 255)
black_blue_color = (3, 16, 89)


pygame.init()
window_width = 500
window_height = 500
pygame.display.set_caption('Clock')
screen = pygame.display.set_mode((window_width, window_height))

program_running = True

center = (int(window_width / 2), int(window_height / 2))
radius_clock = int(window_height / 4)

hand_minute = [center[0], center[1] - radius_clock]
hand_sec = [0, 0]

times_set = 77
times = times_set
angle = 0

while program_running:
    if times == 0:
        program_running = False

    angle = 360 - times * 360 / times_set
    angle = getRad(angle)
    hand_minute[0] = int(center[0] + radius_clock * sin(angle))
    hand_minute[1] = int(center[1] - radius_clock * cos(angle))
    format_time = getFormatTime(times)
    # draw user interface
    screen.fill(grey_color)

    # draw clock
    pygame.draw.circle(screen, white_color, center, radius_clock)
    pygame.draw.aaline(screen, black_blue_color, center, hand_minute)

    # draw setting time

    # draw time_count
    font = pygame.font.SysFont(None, 50)
    img = font.render(format_time, True, white_color)
    screen.blit(img, (center[0] - 50, center[1] + radius_clock + 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False

        pass

    time.sleep(1)
    times -= 1

    pygame.display.flip()
