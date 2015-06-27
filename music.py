import pygame
from pygame.locals import *
import os
import sys
import random
import re

play_stereo = True
songNumber = 0
x = 0
SONG_END = pygame.USEREVENT + 1
path = os.path.dirname(os.path.abspath(__file__))
DETECTION_NOISES_PATH = "\detection_start\\"
DETECTION_END_NOISES_PATH = "\detection_end\\"

path += DETECTION_NOISES_PATH

pygame.display.set_caption("Pygame Audio player")
screen = pygame.display.set_mode((800, 800), 0, 32)
pygame.init()

def build_file_list():
    file_list = []
    for root, folders, files in os.walk(path):
        folders.sort()
        files.sort()
        for filename in files:
            if re.search(".(aac|mp3|wav|flac|m4a|pls|m3u)$", filename) != None: 
                file_list.append(os.path.join(root, filename))
    return file_list

def play_songs(file_list):
    random.shuffle(file_list)
    pygame.mixer.music.load(file_list[songNumber])
    print file_list[songNumber]
    pygame.mixer.music.play(1)

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                files = build_file_list()
                play_songs(files)

            if event.key == K_ESCAPE:
                sys.exit()
                break