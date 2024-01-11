# traffic_lights.py
import pygame

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
        self.line_width = width

        # Set up rectangles for parts A and B
        self.rect_a = pygame.Rect(0, 0, width, self.line_y)
        self.rect_b = pygame.Rect(0, self.line_y, width, height - self.line_y)

        # Set up traffic lights in part A
        self.rectangle_gap = 300
        self.traffic_light_a1 = pygame.Rect(50, 50, 250, 100)
        self.traffic_light_a2 = pygame.Rect(self.traffic_light_a1.right + self.rectangle_gap, 50, 250, 100)
        self.current_state_a1 = self.red
        self.current_state_a2 = self.red
        self.timer_a1 = 15  # Initial red light duration
        # self.timer_a2 = 50  # Initial red light duration

        # Set up traffic lights in part B
        self.traffic_light_b1 = pygame.Rect(50, self.line_y + 50, 250, 100)
        self.traffic_light_b2 = pygame.Rect(self.traffic_light_b1.right + self.rectangle_gap, self.line_y + 50, 250, 100)
        self.current_state_b1 = self.green
        self.current_state_b2 = self.green
        # self.timer_b1 = 90  # Initial red light duration
        self.timer_b2 = self.timer_a2=self.timer_b1=self.timer_a1  # Initial red light duration

        # Traffic light timers
        self.red_light_duration = self.timer_a1
        self.yellow_light_duration = 5  # Set yellow light duration to 5 seconds
        self.green_light_duration = 10

        # Set up the clock for managing frame rate
        self.clock = pygame.time.Clock()

        # Set up the initial time in milliseconds
        self.start_time = pygame.time.get_ticks()

    def update(self):
        elapsed_seconds = self.clock.tick(60) / 1000.0  # Get elapsed time in seconds

        # Update traffic light states in part A based on timers
        self.timer_a1 -= elapsed_seconds
        if self.timer_a1 <= 0:
            self.timer_a1 = self.red_light_duration
            if self.current_state_a1 == self.red:
                self.current_state_a1 = self.green
            elif self.current_state_a1 == self.green:
                self.current_state_a1 = self.yellow
            elif self.current_state_a1 == self.yellow:
                self.current_state_a1 = self.red

        self.timer_a2 -= elapsed_seconds
        if self.timer_a2 <= 0:
            self.timer_a2 = self.red_light_duration
            if self.current_state_a2 == self.red:
                self.current_state_a2 = self.green
            elif self.current_state_a2 == self.green:
                self.current_state_a2 = self.yellow
            elif self.current_state_a2 == self.yellow:
                self.current_state_a2 = self.red

        # Update traffic light states in part B based on timers
        self.timer_b1 -= elapsed_seconds
        if self.timer_b1 <= 0:
            self.timer_b1 = self.red_light_duration
            if self.current_state_a1 == self.red:
                self.current_state_b1 = self.green
            elif self.current_state_a1 == self.green:
                self.current_state_b1 = self.red
            elif self.current_state_a1 == self.yellow:
                self.current_state_b1 = self.yellow

        self.timer_b2 -= elapsed_seconds
        if self.timer_b2 <= 0:
            self.timer_b2 = self.red_light_duration
            if self.current_state_a2 == self.red:
                self.current_state_b2 = self.green
            elif self.current_state_a2 == self.green:
                self.current_state_b2 = self.red
            elif self.current_state_a2 == self.yellow:
                self.current_state_b2 = self.yellow



    def render(self):
        self.screen.fill(self.white)

        pygame.draw.rect(self.screen, self.black, self.rect_a, 2)
        pygame.draw.rect(self.screen, self.black, self.rect_b, 2)

        pygame.draw.rect(self.screen, self.green, self.traffic_light_a1, 2)
        pygame.draw.rect(self.screen, self.black, self.traffic_light_a2, 2)

        self.draw_traffic_light_colors(self.traffic_light_a1, self.current_state_a1)
        self.draw_traffic_light_colors(self.traffic_light_a2, self.current_state_a2)

        self.draw_timer(self.traffic_light_a1, self.timer_a1)
        self.draw_timer(self.traffic_light_a2, self.timer_a2)

        pygame.draw.rect(self.screen, self.green, self.traffic_light_b1, 2)
        pygame.draw.rect(self.screen, self.black, self.traffic_light_b2, 2)

        self.draw_traffic_light_colors(self.traffic_light_b1, self.current_state_b1)
        self.draw_traffic_light_colors(self.traffic_light_b2, self.current_state_b2)

        self.draw_timer(self.traffic_light_b1, self.timer_b1)
        self.draw_timer(self.traffic_light_b2, self.timer_b2)

        pygame.display.flip()

    def draw_traffic_light_colors(self, traffic_light, state):
        pygame.draw.circle(self.screen, self.red if state == self.red else self.black,
                           (traffic_light.left + 50, traffic_light.top + 75), 20)
        pygame.draw.circle(self.screen, self.yellow if state == self.yellow else self.black,
                           (traffic_light.left + 125, traffic_light.top + 75), 20)
        pygame.draw.circle(self.screen, self.green if state == self.green else self.black,
                           (traffic_light.right - 50, traffic_light.top + 75), 20)

    def draw_timer(self, traffic_light, timer_value):
        font = pygame.font.Font(None, 36)
        text = font.render(f"{int(timer_value):02d}", True, self.red)
        text_rect = text.get_rect(center=(traffic_light.right + 50, traffic_light.centery))
        self.screen.blit(text, text_rect)