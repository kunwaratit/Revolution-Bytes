import pygame

box_width = 300
box_height = 150
box_color = (200, 200, 200)
box_gap = 10

class BoxValues:
    def __init__(self, traffic_light_a1, traffic_light_a2, traffic_light_b1, traffic_light_b2):
        self.box_a1 = pygame.Rect(traffic_light_a1.left, traffic_light_a1.bottom + box_gap, box_width, box_height)
        self.box_a2 = pygame.Rect(traffic_light_a2.left, traffic_light_a2.bottom + box_gap, box_width, box_height)
        self.box_b1 = pygame.Rect(traffic_light_b1.left, traffic_light_b1.bottom + box_gap, box_width, box_height)
        self.box_b2 = pygame.Rect(traffic_light_b2.left, traffic_light_b2.bottom + box_gap, box_width, box_height)

        # Set up font
        self.font = pygame.font.Font(None, 24)

        # Initialize vehicle count for each lane
        self.vehicle_count_a1 = 70
        self.vehicle_count_a2 = 25
        self.vehicle_count_b1 = 53
        self.vehicle_count_b2 = 33

    def draw_boxes(self, screen):
        # Draw boxes directly onto the main screen
        pygame.draw.rect(screen, box_color, self.box_a1, 2)
        pygame.draw.rect(screen, box_color, self.box_a2, 2)
        pygame.draw.rect(screen, box_color, self.box_b1, 2)
        pygame.draw.rect(screen, box_color, self.box_b2, 2)

        # Render and blit text below each box
        self.render_and_blit_text(screen, "Lane Left", self.vehicle_count_a1, self.box_a1)
        self.render_and_blit_text(screen, "Lane Right", self.vehicle_count_a2, self.box_a2)
        self.render_and_blit_text(screen, "Lane Top", self.vehicle_count_b1, self.box_b1)
        self.render_and_blit_text(screen, "Lane Bottom", self.vehicle_count_b2, self.box_b2)

    def render_and_blit_text(self, screen, lane_name, vehicle_count, box):
        lane_text = self.font.render(lane_name, True, (0, 0, 0))
        count_text = self.font.render(f"Vehicles: {vehicle_count}", True, (0, 0, 0))
        
        # Blit lane name
        screen.blit(lane_text, (box.left + 5, box.top + 5))
        
        # Blit vehicle count with a line break
        screen.blit(count_text, (box.left + 5, box.top + 5 + lane_text.get_height() + 5))
