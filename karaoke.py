import time
import os
from colorama import Fore, Style, init
import pygame
init(autoreset=True)
AUDIO_FILE = "Sahiba.mp3"
pygame.mixer.init()
timestamps = []
lyrics = []
with open("lyrics.txt", "r", encoding="utf-8") as f:
    for line in f:
        if " - " in line:
            ts, text = line.split(" - ", 1)
            timestamps.append(ts.strip())
            lyrics.append(text.strip())
def timestamp_to_seconds(ts):
    mm, ss = ts.split(":")
    return int(mm) * 60 + float(ss)
ts_seconds = [timestamp_to_seconds(t) for t in timestamps]
pygame.mixer.music.load(AUDIO_FILE)
pygame.mixer.music.play()
start = time.time()

for i, line in enumerate(lyrics):
    while time.time() - start < ts_seconds[i]:
        time.sleep(0.005)

    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.BLUE + Style.BRIGHT + line.center(80))

print(Fore.RED + "\n--- SONG FINISHED ---\n")

while pygame.mixer.music.get_busy():
    time.sleep(0.1)

pygame.mixer.quit()