import random
import pygame
from utils import wait_for_key

TWO_FA_SCENARIOS = [
    (["Enable 2FA?", "Your account was accessed from a new device.", "E = Enable, S = Skip"], pygame.K_e),
    (["Enable 2FA?", "Someone tried to log in from China.", "E = Enable, S = Skip"], pygame.K_e),
    (["Enable 2FA?", "Security recommendation for your account.", "E = Enable, S = Skip"], pygame.K_e),
    (["Enable 2FA?", "You got an email login attempt.", "E = Enable, S = Skip"], pygame.K_e),
]


def two_factor_frenzy(score, shapes, screen, font, small_font):
    scenario, correct = random.choice(TWO_FA_SCENARIOS)
    key = wait_for_key([pygame.K_e, pygame.K_s], 7, score, scenario, screen, font, small_font, shapes)
    return key == correct
