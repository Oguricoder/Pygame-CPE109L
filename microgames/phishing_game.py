import random
import pygame
from utils import wait_for_key

PHISHING_SCENARIOS = [
    (["Is this email safe?", "From: support@paypa1.com", "Click to verify your account!", "Y = Safe, N = Phishing"], pygame.K_n),
    (["Is this email safe?", "From: security@amaz0n.com", "Urgent: Confirm your order!", "Y = Safe, N = Phishing"], pygame.K_n),
    (["Is this email safe?", "From: team@company.com", "Meeting notes from today", "Y = Safe, N = Phishing"], pygame.K_y),
    (["Is this email safe?", "From: ceo@company.com", "Please buy 10 gift cards urgently!", "Y = Safe, N = Phishing"], pygame.K_n),
]


def phishing_detector(score, shapes, screen, font, small_font):
    scenario, correct = random.choice(PHISHING_SCENARIOS)
    key = wait_for_key([pygame.K_y, pygame.K_n], 11, score, scenario, screen, font, small_font, shapes)
    return key == correct
