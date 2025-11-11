import pygame
import os

# Initialize mixer with a safe pre-init
try:
    pygame.mixer.pre_init(44100, -16, 2, 512)
except Exception:
    pass
pygame.init()

SOUNDS_LOADED = False
sound_success = None
sound_fail = None
sound_select = None
sound_tick = None

try:
    base = os.path.join(os.path.dirname(__file__), 'sounds')
    # Background music (optional)
    music_path = os.path.join(base, 'background_music.mp3')
    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def _s(path):
        p = os.path.join(base, path)
        return pygame.mixer.Sound(p) if os.path.exists(p) else None

    sound_success = _s('success.wav')
    sound_fail = _s('fail.wav')
    sound_select = _s('select.wav')
    sound_tick = _s('tick.wav')

    # Set volumes if sounds exist
    if sound_success: sound_success.set_volume(0.6)
    if sound_fail: sound_fail.set_volume(0.6)
    if sound_select: sound_select.set_volume(0.4)
    if sound_tick: sound_tick.set_volume(0.25)

    # Only mark loaded if at least one effect loaded
    SOUNDS_LOADED = any([sound_success, sound_fail, sound_select, sound_tick])
    if not SOUNDS_LOADED:
        print("⚠ SOUND FILES NOT FOUND IN 'sounds' FOLDER. Game will run without effects.")
except Exception as e:
    print("Error initializing sounds:", e)


def play_sound(sound):
    try:
        if sound:
            sound.play()
    except Exception:
        pass
