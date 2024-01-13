import pygame
from values import BoxValues
from timer import Timer

class TrafficLight:
    def __init__(self, rect, is_rectangle_a=True, initial_state="red"):
        self.rect = rect
        if is_rectangle_a:
            self.timer_red = Timer(initial_time=60)
            self.timer_yellow = Timer(initial_time=10)
            self.timer_green = Timer(initial_time=60)
        else:
            self.timer_red = Timer(initial_time=60)
            self.timer_yellow = Timer(initial_time=10)
            self.timer_green = Timer(initial_time=60)

        self.timer_cycle = self.timer_red.get_current_time() + self.timer_yellow.get_current_time() + self.timer_green.get_current_time()

        if initial_state == "red":
            self.timer_cycle -= self.timer_yellow.get_current_time() + self.timer_green.get_current_time()
        elif initial_state == "yellow":
            self.timer_cycle -= self.timer_green.get_current_time()

        self.current_state = initial_state
        self.current_timer = self.get_current_timer()

    def get_current_timer(self):
        if self.current_state == "red":
            return self.timer_red.get_current_time()
        elif self.current_state == "yellow":
            return self.timer_yellow.get_current_time()
        elif self.current_state == "green":
            return self.timer_green.get_current_time()

class TrafficLights:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.red = (0, 255, 0)

        self.line_y = height // 2

        self.rect_a = pygame.Rect(0, 0, width, self.line_y)
        self.rect_b = pygame.Rect(0, self.line_y, width, height - self.line_y)

        self.rectangle_gap = 300
        self.traffic_light_a1 = TrafficLight(pygame.Rect(50, 50, 250, 100), is_rectangle_a=True, initial_state="green")
        self.traffic_light_a2 = TrafficLight(pygame.Rect(self.traffic_light_a1.rect.right + self.rectangle_gap, 50, 250, 100), is_rectangle_a=True, initial_state="green")

        self.traffic_light_b1 = TrafficLight(pygame.Rect(50, self.line_y + 50, 250, 100), is_rectangle_a=False, initial_state="red")
        self.traffic_light_b2 = TrafficLight(pygame.Rect(self.traffic_light_b1.rect.right + self.rectangle_gap, self.line_y + 50, 250, 100), is_rectangle_a=False, initial_state="red")

        self.box_values = BoxValues(self.traffic_light_a1, self.traffic_light_a2, self.traffic_light_b1, self.traffic_light_b2)

        self.clock = pygame.time.Clock()

        self.emergency_state = False

    def set_emergency_state(self, is_emergency):
        if is_emergency:
            # Turning all traffic lights to green during emergency
            self.traffic_light_a1.current_state = "green"
            self.traffic_light_a2.current_state = "green"
            self.traffic_light_b1.current_state = "green"
            self.traffic_light_b2.current_state = "green"

    def update(self):
        elapsed_seconds = self.clock.tick(60) / 1000.0  

        self.update_traffic_light(self.traffic_light_a1, elapsed_seconds)
        self.update_traffic_light(self.traffic_light_a2, elapsed_seconds)

        self.update_traffic_light(self.traffic_light_b1, elapsed_seconds)
        self.update_traffic_light(self.traffic_light_b2, elapsed_seconds)

    def update_traffic_light(self, traffic_light, elapsed_seconds):
        if not self.emergency_state:
            traffic_light.current_timer -= elapsed_seconds

            if traffic_light.current_timer <= 0:
                traffic_light.current_state = self.get_next_state(traffic_light.current_state)
                traffic_light.current_timer = traffic_light.get_current_timer()
        else:
            traffic_light.current_state = "green"  # Set the light to red during emergency

    def get_next_state(self, current_state):
        states = ["red", "yellow", "green"]
        current_index = states.index(current_state)
        next_index = (current_index + 1) % len(states)
        return states[next_index]

    def render(self):
        self.screen.fill(self.white)

        pygame.draw.rect(self.screen, self.black, self.rect_a, 2)
        pygame.draw.rect(self.screen, self.black, self.rect_b, 2)

        pygame.draw.rect(self.screen, self.red if self.traffic_light_a1.current_state == "red" else self.black, self.traffic_light_a1.rect, 2)
        pygame.draw.rect(self.screen, self.red if self.traffic_light_a2.current_state == "red" else self.black, self.traffic_light_a2.rect, 2)

        self.draw_traffic_light_colors(self.traffic_light_a1, self.traffic_light_a1.current_state)
        self.draw_traffic_light_colors(self.traffic_light_a2, self.traffic_light_a2.current_state)

        pygame.draw.rect(self.screen, self.red if self.traffic_light_b1.current_state == "red" else self.black, self.traffic_light_b1.rect, 2)
        pygame.draw.rect(self.screen, self.red if self.traffic_light_b2.current_state == "red" else self.black, self.traffic_light_b2.rect, 2)

        self.draw_traffic_light_colors(self.traffic_light_b1, self.traffic_light_b1.current_state)
        self.draw_traffic_light_colors(self.traffic_light_b2, self.traffic_light_b2.current_state)

        self.box_values.draw_boxes(self.screen)

        pygame.display.flip()

    def draw_traffic_light_colors(self, traffic_light, state):
        pygame.draw.circle(self.screen, self.red if state == "red" else self.black,
                        (traffic_light.rect.left + 50, traffic_light.rect.top + 75), 20)
        pygame.draw.circle(self.screen, self.yellow if state == "yellow" else self.black,
                        (traffic_light.rect.left + 125, traffic_light.rect.top + 75), 20)
        pygame.draw.circle(self.screen, self.green if state == "green" else self.black,
                        (traffic_light.rect.right - 50, traffic_light.rect.top + 75), 20)

        timer_font = pygame.font.Font(None, 36)
        timer_color = self.red if state == "red" else self.black

        timer_text = timer_font.render(f"{int(traffic_light.current_timer)}s", True, timer_color)
        self.screen.blit(timer_text, (traffic_light.rect.right + 10, traffic_light.rect.top + 50))

if __name__ == "__main__":
    pygame.init()

    width, height = 800, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Traffic Lights Simulation")

    traffic_lights = TrafficLights(screen, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    traffic_lights.set_emergency_state(not traffic_lights.emergency_state)

        traffic_lights.update()
        traffic_lights.render()

    pygame.quit()
