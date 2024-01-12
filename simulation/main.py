# main.py
import pygame
import sys
from traffic_lights import *
from values import *

# Initialize Pygame
pygame.init()

# Set up window dimensions
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Lights")

# Set up TrafficLights object
traffic_lights = TrafficLights(screen, width, height)

# Set up BoxValues object
box_values = BoxValues(traffic_lights.traffic_light_a1, traffic_lights.traffic_light_a2,
                      traffic_lights.traffic_light_b1, traffic_lights.traffic_light_b2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update and render traffic lights
    traffic_lights.update()
    traffic_lights.render()

    # Draw boxes below traffic lights
    box_values.draw_boxes(screen)

    # Control the frames per second
    pygame.time.Clock().tick(60)

    # Update the display
    pygame.display.flip()
