import pygame
import sys
import time
from sound import play_sound, sound_tick, sound_select

clock = pygame.time.Clock()


def draw_screen(lines, score=None, timer=None, screen=None, font=None, small_font=None, shapes=None):
    screen.fill((0, 0, 0))
    if shapes:
        for shape in shapes:
            shape.draw(screen)
    if score is not None:
        score_text = font.render(f"Score: {score}", True, (0, 255, 0))
        screen.blit(score_text, (20, 20))
    if timer is not None:
        timer_text = font.render(f"Time: {timer}s", True, (255, 0, 0))
        screen.blit(timer_text, (screen.get_width() - 150, 20))
    start_y = screen.get_height() // 2 - (len(lines) * 20)
    for i, line in enumerate(lines):
        rendered = font.render(line, True, (255, 255, 255))
        rect = rendered.get_rect(center=(screen.get_width() // 2, start_y + i * 40))
        screen.blit(rendered, rect)
    pygame.display.flip()


def wait_for_key(valid_keys, duration, score, instructions, screen, font, small_font, shapes=None):
    start_time = time.time()
    last_second = int(duration)

    while True:
        elapsed = time.time() - start_time
        remaining = max(0, duration - elapsed)
        current_second = int(remaining)

        if current_second != last_second and current_second <= 3 and current_second > 0:
            play_sound(sound_tick)
        last_second = current_second

        # 💫 Update background animation
        if shapes:
            for shape in shapes:
                shape.update()  # <-- FIXED HERE

        draw_screen(
            instructions,
            score=score,
            timer=int(remaining),
            screen=screen,
            font=font,
            small_font=small_font,
            shapes=shapes
        )

        if remaining <= 0:
            return None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in valid_keys:
                    play_sound(sound_select)
                    return event.key

        clock.tick(30)


def show_result(success, score, screen, font):
    from sound import play_sound, sound_success, sound_fail
    if success:
        play_sound(sound_success)
        draw_screen(["SUCCESS! +10 points"], score=score, timer=None, screen=screen, font=font, small_font=font, shapes=None)
    else:
        play_sound(sound_fail)
        draw_screen(["FAILED! No points"], score=score, timer=None, screen=screen, font=font, small_font=font, shapes=None)
    pygame.display.flip()
    time.sleep(1.2)
