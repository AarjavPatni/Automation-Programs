import pygame
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import os
from re import findall
from time import sleep
from itertools import chain
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

with open(r'C:\Users\Aarjav\Documents\Automation-Programs\songs.txt') as f:
    song_list_from_file = [line for line in f]
    songs, artists = [line.split(', ')[0] for line in song_list_from_file], [
        line.split(', ')[1].strip() for line in song_list_from_file]

files_list = list(
    chain(*[files for root, dirs, files in os.walk(r'C:\Users\Aarjav\Downloads')]))

EdgeService(r'C:\Users\Aarjav\msedgedriver.exe').start()
# Open edge browser and navigate to the website
options = webdriver.EdgeOptions()
options.page_load_strategy = 'eager'
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--headless")
driver = webdriver.Edge(
    service=EdgeService(r'C:\Users\Aarjav\msedgedriver.exe'), options=options)

pygame.init()
pygame.mixer.music.load(
    r"C:\Users\Aarjav\Documents\Automation-Programs\Ring01.wav")

errors = []


def eleInStr(lst, string):
    for elem in lst:
        if elem.lower() in string.lower():
            return True
    return False


mods_list = ['remix', 'reprise', 'dialogue', 'rock',
             'revival', 'revisited', 'pt.', 'return', 'electronic', 'unplugged', 'reverb']

# Loop through each element in the lists
for i in range(len(songs)):
    if any(songs[i] in filename.replace('.mp3', '') for filename in files_list) or any(filename.replace('.mp3', '') in songs[i] for filename in files_list):
        continue

    driver.get(f'https://pagalfree.com/search/{songs[i]}')

    try:
        for j in range(2):
            try:
                song_target = []
                song_details = driver.find_elements(
                    By.XPATH, "//div[contains(@id, 'category_content')]")
                for k in song_details:
                    source_code = k.get_attribute("outerHTML")
                    if (all((eleInStr([songs[i]], source_code), eleInStr([artists[i]], source_code)))) and not (eleInStr(mods_list, source_code)):
                        song_target.append(k)
                if len(song_target):
                    song_target = song_target[0]
                else:
                    raise Exception

                break

            except Exception:
                if j:
                    for counter, k in enumerate(song_details):
                        details = findall(
                            r'(?<=>)[^<]+?(?=<)', k.get_attribute("outerHTML"))
                        song_list = []
                        for m in details:
                            song_list.append(
                                m.strip()) if m.strip() != '' else None

                        if any(eleInStr(mods_list, metadata) for metadata in song_list):
                            continue
                        print(f'{counter+1}. {song_list[0]} - {song_list[1]}')

                    if song_details == []:
                        raise Exception

                    pygame.mixer.music.play()
                    next = input(
                        'Press y to skip or enter the number: ')
                    if next.lower() in ('y', ''):
                        print()
                        raise Exception
                    else:
                        song_target = song_details[int(next)-1]
                else:
                    sleep(1)

        song_target.click()
        dlButton = driver.find_elements(By.CLASS_NAME, 'btn-download')
        dlButton[len(dlButton)-2].click()
    except Exception:
        errors.append(f'ERROR: {songs[i]}, {artists[i]}')
        pass

print(*[error for error in errors], sep='\n')
input('Press enter to quit after downloads are complete ')
