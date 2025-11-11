import pygame
import sys
import random
import time
import math

from background import create_shapes, FloatingShape
from sound import SOUNDS_LOADED, play_sound, sound_select, sound_tick, sound_success, sound_fail
from utils import draw_screen, wait_for_key, show_result

# Import microgames
from microgames.password_game import password_picker
from microgames.phishing_game import phishing_detector
from microgames.port_game import port_panic
from microgames.encryption_game import encryption_match
from microgames.twofa_game import two_factor_frenzy
from microgames.firewall_game import firewall_defense

# Initialize pygame (safety: already initialized in sound.py but keep local references)
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CyberDefender Microgame Suite")
font = pygame.font.SysFont("consolas", 28)
small_font = pygame.font.SysFont("consolas", 24)
clock = pygame.time.Clock()

# Create floating shapes
shapes = create_shapes(30, WIDTH, HEIGHT)

# Title screen with pulsating dynamic title
def title_screen():
    pulse_time = 0
    title_lines = [
        "Welcome to CyberDefender Microgames!",
        "Test your cybersecurity reflexes!",
        "",
        "Press SPACE or ENTER to start."
    ]
    if SOUNDS_LOADED:
        title_lines.insert(3, "♪ Sound: ON ♪")
    else:
        title_lines.insert(3, "⚠ Sound: OFF (No sound files found)")

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                play_sound(sound_select)
                waiting = False

        # Animate pulse
        pulse_time += clock.get_time() / 1000.0
        scale = 1 + 0.08 * math.sin(pulse_time * 3)
        title_color = (100 + int(155 * abs(math.sin(pulse_time * 2))), 255, 255)

        screen.fill((0, 0, 0))
        for shape in shapes:
            shape.update()
            shape.draw(screen)

        dynamic_font = pygame.font.SysFont("consolas", max(28, int(48 * scale)))
        title_surface = dynamic_font.render("CYBERDEFENDER", True, title_color)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(title_surface, title_rect)

        y_offset = 0
        for line in title_lines:
            rendered = small_font.render(line, True, (255, 255, 255))
            rect = rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50 + y_offset))
            screen.blit(rendered, rect)
            y_offset += 40

        pygame.display.flip()
        clock.tick(60)


def main():
    score = 0
    microgames = [
        password_picker,
        phishing_detector,
        port_panic,
        encryption_match,
        two_factor_frenzy,
        firewall_defense,
    ]

    title_screen()

    rounds = 10
    available_games = microgames.copy()

    for i in range(rounds):
        if not available_games:
            available_games = microgames.copy()
        game = random.choice(available_games)
        available_games.remove(game)

        result = game(score, shapes, screen, font, small_font)
        if result:
            score += 10
        show_result(result, score, screen, font)

    draw_screen(["GAME OVER!", f"Final Score: {score} / {rounds * 10}", "", "Press ESC to exit."], score=score, screen=screen, font=font, small_font=small_font, shapes=shapes)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        clock.tick(30)


if __name__ == "__main__":
    main()
