# traffic_lights.py
import pygame
from values import BoxValues

class TrafficLight:
    def __init__(self, rect, is_rectangle_a=True):
        self.rect = rect
        if is_rectangle_a:
            self.timer_red = 1
            self.timer_yellow = 1
            self.timer_green = 1
        else:
            # Adjust the timings for rectangle B
            self.timer_red =5
            self.timer_yellow = 5
            self.timer_green = 5

        self.timer_cycle = self.timer_red + self.timer_yellow + self.timer_green
        self.current_state = "red"

class TrafficLights:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        # Set up colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.green = (0, 255, 0)

        # Set up line position and dimensions
        self.line_y = height // 2

        # Set up rectangles for parts A and B
        self.rect_a = pygame.Rect(0, 0, width, self.line_y)
        self.rect_b = pygame.Rect(0, self.line_y, width, height - self.line_y)

        # Set up traffic lights in part A
        self.rectangle_gap = 300
        self.traffic_light_a1 = TrafficLight(pygame.Rect(50, 50, 250, 100), is_rectangle_a=True)
        self.traffic_light_a2 = TrafficLight(pygame.Rect(self.traffic_light_a1.rect.right + self.rectangle_gap, 50, 250, 100), is_rectangle_a=True)

        # Set up traffic lights in part B
        self.traffic_light_b1 = TrafficLight(pygame.Rect(50, self.line_y + 50, 250, 100), is_rectangle_a=False)
        self.traffic_light_b2 = TrafficLight(pygame.Rect(self.traffic_light_b1.rect.right + self.rectangle_gap, self.line_y + 50, 250, 100), is_rectangle_a=False)

        # Set up additional boxes next to traffic lights using BoxValues
        self.box_values = BoxValues(self.traffic_light_a1, self.traffic_light_a2, self.traffic_light_b1, self.traffic_light_b2)

        # Set up the clock for managing frame rate
        self.clock = pygame.time.Clock()

    def update(self):
        elapsed_seconds = self.clock.tick(60) / 1000.0  # Get elapsed time in seconds

        # Update traffic light states in part A based on timers
        self.update_traffic_light(self.traffic_light_a1, elapsed_seconds)
        self.update_traffic_light(self.traffic_light_a2, elapsed_seconds)

        # Update traffic light states in part B based on timers
        self.update_traffic_light(self.traffic_light_b1, elapsed_seconds)
        self.update_traffic_light(self.traffic_light_b2, elapsed_seconds)

    def update_traffic_light(self, traffic_light, elapsed_seconds):
        # Update the timer for the entire cycle
        traffic_light.timer_cycle -= elapsed_seconds

        # Check which state should be active based on the timers
        if 0 <= traffic_light.timer_cycle < traffic_light.timer_green:
            traffic_light.current_state = "green"
        elif traffic_light.timer_green <= traffic_light.timer_cycle < traffic_light.timer_green + traffic_light.timer_yellow:
            traffic_light.current_state = "yellow"
        else:
            traffic_light.current_state = "red"

        # Reset the timers when they reach zero
        if traffic_light.timer_cycle <= 0:
            traffic_light.timer_cycle = traffic_light.timer_red + traffic_light.timer_yellow + traffic_light.timer_green

    def render(self):
        self.screen.fill(self.white)

        pygame.draw.rect(self.screen, self.black, self.rect_a, 2)
        pygame.draw.rect(self.screen, self.black, self.rect_b, 2)

        pygame.draw.rect(self.screen, self.red if self.traffic_light_a1.current_state == "red" else self.black, self.traffic_light_a1.rect, 2)
        pygame.draw.rect(self.screen, self.red if self.traffic_light_a2.current_state == "red" else self.black, self.traffic_light_a2.rect, 2)

        self.draw_traffic_light_colors(self.traffic_light_a1.rect, self.traffic_light_a1.current_state)
        self.draw_traffic_light_colors(self.traffic_light_a2.rect, self.traffic_light_a2.current_state)

        pygame.draw.rect(self.screen, self.red if self.traffic_light_b1.current_state == "red" else self.black, self.traffic_light_b1.rect, 2)
        pygame.draw.rect(self.screen, self.red if self.traffic_light_b2.current_state == "red" else self.black, self.traffic_light_b2.rect, 2)

        self.draw_traffic_light_colors(self.traffic_light_b1.rect, self.traffic_light_b1.current_state)
        self.draw_traffic_light_colors(self.traffic_light_b2.rect, self.traffic_light_b2.current_state)

        pygame.draw.rect(self.screen, self.black, self.box_values.box_a1, 2)
        pygame.draw.rect(self.screen, self.black, self.box_values.box_a2, 2)
        pygame.draw.rect(self.screen, self.black, self.box_values.box_b1, 2)
        pygame.draw.rect(self.screen, self.black, self.box_values.box_b2, 2)

        pygame.display.flip()

    def draw_traffic_light_colors(self, traffic_light, state):
        pygame.draw.circle(self.screen, self.red if state == "red" else self.black,
                           (traffic_light.left + 50, traffic_light.top + 75), 20)
        pygame.draw.circle(self.screen, self.yellow if state == "yellow" else self.black,
                           (traffic_light.left + 125, traffic_light.top + 75), 20)
        pygame.draw.circle(self.screen, self.green if state == "green" else self.black,
                           (traffic_light.right - 50, traffic_light.top + 75), 20)

if __name__ == "__main__":
    pygame.init()

    # Set up the display
    width, height = 800, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Traffic Lights Simulation")

    traffic_lights = TrafficLights(screen, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        traffic_lights.update()
        traffic_lights.render()

    pygame.quit()
