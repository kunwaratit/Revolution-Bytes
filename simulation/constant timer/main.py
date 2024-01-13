# main.py
import pygame
import sys
from traffic_lights import *
from values import *


pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Constant Timer")

traffic_lights = TrafficLights(screen, width, height)

box_values = BoxValues(traffic_lights.traffic_light_a1, traffic_lights.traffic_light_a2,
                      traffic_lights.traffic_light_b1, traffic_lights.traffic_light_b2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    traffic_lights.update()
    traffic_lights.render()

    box_values.draw_boxes(screen)

    pygame.time.Clock().tick(60)

    pygame.display.flip()
