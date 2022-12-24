# This method is used just to remove default welcome message from pygame
from os import environ  
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
pygame.mixer.init()
pygame.init()

def playmusic(): 
    music_list=['Alan Walker  Fade NCS Release.mp3','Alan Walker  Spectre NCS Release.mp3','Tobu  Itro  Sunburst NCS Release.mp3','OnlyMP3.net - Excuses  AP Dhillon  Gurinder Gill  Intense  Banger SZN-vX2cDW8LUWk-192k-1632771183696.mp3']
    music=random.choice(music_list)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()

def stopmusic():
    pygame.mixer.music.stop()

def pausemusic():
    pygame.mixer.music.pause()
    
def resumemusic():
    pygame.mixer.music.unpause()
    

def main():
    while True:
        query=takeCommand().lower()
        if 'play music' in query:
            playmusic()
        elif 'stop music' in query:
            stopmusic()
        elif 'pause music' in query:
            pausemusic()
        elif 'resume music' in query:
            resumemusic()
        elif 'exit' in query:
            exit()
        else:
            pass