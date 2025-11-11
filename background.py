import random
import math
import pygame

class FloatingShape:
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(20, 60)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.shape_type = random.choice(['circle', 'square', 'triangle', 'line'])
        self.color = random.choice([
            (0, 100, 200),
            (0, 150, 100),
            (150, 0, 200),
            (200, 100, 0),
            (200, 0, 150),
            (0, 200, 200),
        ])
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-5, 5)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rotation += self.rotation_speed

        if self.x < -100: self.x = self.WIDTH + 100
        if self.x > self.WIDTH + 100: self.x = -100
        if self.y < -100: self.y = self.HEIGHT + 100
        if self.y > self.HEIGHT + 100: self.y = -100

    def draw(self, surface):
        if self.shape_type == 'circle':
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size, 2)
        elif self.shape_type == 'square':
            rect = pygame.Rect(0, 0, self.size * 2, self.size * 2)
            rect.center = (int(self.x), int(self.y))
            pygame.draw.rect(surface, self.color, rect, 2)
        elif self.shape_type == 'triangle':
            angle_rad = math.radians(self.rotation)
            points = []
            for angle in [0, 120, 240]:
                rad = math.radians(angle) + angle_rad
                px = self.x + self.size * math.cos(rad)
                py = self.y + self.size * math.sin(rad)
                points.append((int(px), int(py)))
            pygame.draw.polygon(surface, self.color, points, 2)
        elif self.shape_type == 'line':
            angle_rad = math.radians(self.rotation)
            x1 = self.x + self.size * math.cos(angle_rad)
            y1 = self.y + self.size * math.sin(angle_rad)
            x2 = self.x - self.size * math.cos(angle_rad)
            y2 = self.y - self.size * math.sin(angle_rad)
            pygame.draw.line(surface, self.color, (int(x1), int(y1)), (int(x2), int(y2)), 2)


def create_shapes(n, WIDTH, HEIGHT):
    return [FloatingShape(WIDTH, HEIGHT) for _ in range(n)]

