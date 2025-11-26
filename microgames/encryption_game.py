# encryption_game.py
import random
import pygame
from utils import wait_for_key

ENCRYPTION_SCENARIOS = [
    (["Which is a secure encryption method?", "1. MD5", "2. SHA-256", "3. ROT13"], pygame.K_2),
    (["Which is a secure encryption method?", "1. DES", "2. AES-256", "3. Caesar Cipher"], pygame.K_2),
    (["Which is the strongest encryption?", "1. Base64", "2. RSA-2048", "3. XOR"], pygame.K_2),
    (["Which is a secure encryption method?", "1. SHA-512", "2. AES", "3. Base64"], pygame.K_2),
]


def encryption_match(score, shapes, screen, font, small_font):
    scenario, correct = random.choice(ENCRYPTION_SCENARIOS)
    instructions = scenario + ["(Press 1/2/3)"]
    key = wait_for_key([pygame.K_1, pygame.K_2, pygame.K_3], 11, score, instructions, screen, font, small_font, shapes)
    return key == correct
