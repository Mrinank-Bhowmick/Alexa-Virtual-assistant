# This method is used just to remove default welcome message from pygame
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

pygame.mixer.init()
pygame.init()


def play_music():

    music_list = [
        "Alan Walker  Fade NCS Release.mp3",
        "Duncan Laurence - Arcade (Lyric Video) ft. FLETCHER.mp3",
    ]
    music = random.choice(music_list)

    # load music file from another directory (music)
    music = "music_files/" + music

    pygame.mixer.music.load(music)
    pygame.mixer.music.play()


def stopmusic():
    pygame.mixer.music.stop()


def pausemusic():
    pygame.mixer.music.pause()


def resumemusic():
    pygame.mixer.music.unpause()
