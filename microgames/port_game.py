import random
import pygame
from utils import wait_for_key

PORT_SCENARIOS = [
    (["Close the risky port!", "Port 23 (Telnet) is open!", "Type 2 then 3 to close"], [pygame.K_2, pygame.K_3]),
    (["Close the risky port!", "Port 21 (FTP) is open!", "Type 2 then 1 to close"], [pygame.K_2, pygame.K_1]),
    (["Close the risky port!", "Port 69 (TFTP) is open!", "Type 6 then 9 to close"], [pygame.K_6, pygame.K_9]),
    (["Close the risky port!", "Port 3389 (RDP) is open!", "Type 3 then 8 to close"], [pygame.K_3, pygame.K_8]),
]


def port_panic(score, shapes, screen, font, small_font):
    scenario, keys = random.choice(PORT_SCENARIOS)
    key1 = wait_for_key([keys[0]], 3, score, scenario, screen, font, small_font, shapes)
    if key1 != keys[0]:
        return False
    key2 = wait_for_key([keys[1]], 3, score, scenario, screen, font, small_font, shapes)
    return key2 == keys[1]
