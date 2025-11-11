import random
import pygame
from utils import wait_for_key

# Quick reflex firewall defense
# Press B to block malicious, A to allow legitimate.

FIREWALL_ENTRIES = [
    ("192.168.1.10", False),
    ("10.0.0.45", False),
    ("203.0.113.5", True),  # external but allowed
    ("198.51.100.7", True),
    ("5.6.7.8", False),
    ("172.16.0.2", False),
]


def firewall_defense(score, shapes, screen, font, small_font):
    # Pick random entry, sometimes label as 'MALICIOUS' or subtle
    ip, legit = random.choice(FIREWALL_ENTRIES)
    label = "LEGIT" if legit else "MALICIOUS"
    # Create a small description to make it trickier sometimes
    desc = "Connection attempt to port 22" if random.random() < 0.5 else "Suspicious traffic pattern"
    instructions = [f"Incoming: {ip}", desc, "Press B to BLOCK, A to ALLOW"]

    key = wait_for_key([pygame.K_b, pygame.K_a], 4, score, instructions, screen, font, small_font, shapes)
    if key is None:
        return False
    if key == pygame.K_b:
        # blocked -> correct if not legit
        return not legit
    else:
        # allowed -> correct if legit
        return legit
