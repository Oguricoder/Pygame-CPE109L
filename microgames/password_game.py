import random
import pygame
from utils import wait_for_key

PASSWORD_SCENARIOS = [
    (["Choose the strongest password!", "1. 123456", "2. P@ssw0rd!", "3. qwerty"], pygame.K_2),
    (["Pick the secure password!", "1. password", "2. Tr0ub4dor&3", "3. 12345678"], pygame.K_2),
    (["Which password is best?", "1. admin", "2. MyD0g@2024!", "3. qwerty123"], pygame.K_2),
    (["Choose the strongest password!", "1. letmein123", "2. CorrectHorseBatteryStaple!", "3. welcome1"], pygame.K_2),
]


def password_picker(score, shapes, screen, font, small_font):
    scenario, correct = random.choice(PASSWORD_SCENARIOS)
    instructions = scenario + ["(Press 1/2/3)"]
    key = wait_for_key([pygame.K_1, pygame.K_2, pygame.K_3], 7, score, instructions, screen, font, small_font, shapes)
    return key == correct
