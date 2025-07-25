import pygame

def play_music():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("assets/music.mp3")
        pygame.mixer.music.play(-1)
    except Exception as e:
        print("🎵 Music couldn't be loaded:", e)
