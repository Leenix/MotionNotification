#!/usr/bin/env python

import pygame
import os
import random
import re
import sys
import time

DETECTION_NOISES_PATH = "/detection_start/"
DETECTION_END_NOISES_PATH = "/detection_end/"
path = os.path.dirname(os.path.abspath(__file__))


def play_random_file(file_path):
    randomfile = random.choice(os.listdir(file_path))
    filename = file_path + randomfile
    play_song(filename)


def build_file_list(file_path):
    file_list = []
    for root, folders, files in os.walk(file_path):
        folders.sort()
        files.sort()
        for filename in files:
            if re.search(".(aac|mp3|wav|flac|m4a|pls|m3u)$", filename) is not None:
                file_list.append(os.path.join(root, filename))
    return file_list


def play_song(file):
    print "Playing sound: {}".format(file)
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(3)
    while pygame.mixer.music.get_busy:
        continue

if __name__ == '__main__':
    if sys.argv[1] == 'start':
        play_random_file(path + DETECTION_NOISES_PATH)

    elif sys.argv[1] == 'end':
        play_random_file(path + DETECTION_END_NOISES_PATH)
