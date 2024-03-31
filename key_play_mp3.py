#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module docstring
"""

import threading
import os
import keyboard
from playsound import playsound


def play_sound(mp3_path):
    print(mp3_path)
    playsound(mp3_path)

def key_press(key_event):
    if key_event.event_type == 'down':
        match key_event.name:
            case 'f12':
                mp3_path = os.path.abspath('E:\\my_desktop\\py_work\\key-play-mp3\\mp3\\bark.mp3')
                threading.Thread(target=play_sound, args=(mp3_path,)).start()
            case 'f11':
                mp3_path = os.path.abspath('E:\\my_desktop\\py_work\\key-play-mp3\\mp3\\howl.mp3')
                threading.Thread(target=play_sound, args=(mp3_path,)).start()

if __name__ == '__main__':
    print('[START] hook keyboard')
    keyboard.hook(key_press)
    keyboard.wait()
    print('[stop] hook keyboard')

