from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from winsound import PlaySound as play
from winsound import SND_FILENAME
from time import sleep

with open('songs.txt') as f:
    list = [line for line in f]
    songs, artists = [line.split(', ')[0] for line in list], [
        line.split(', ')[1].strip() for line in list]


# Open edge browser and navigate to the website
options = webdriver.EdgeOptions()
options.page_load_strategy = 'eager'
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--headless")
driver = webdriver.Edge(executable_path=r'C:\Users\Aarjav\msedgedriver.exe', options=options)


# Loop through each element in the lists
for i in range(len(songs)):
    driver.get('https://pagalfree.com/')

    try:
        song_target = ''
        # Click the input element
        search_input = driver.find_element(
            By.CSS_SELECTOR, 'input[type="text"][id="searchtextval"][class="form-control"]')
        search_input.click()

        # Type in the first element of the first list and press enter
        search_input.send_keys(songs[i] + Keys.RETURN)
        sleep(1)

        for j in range(5):
            try:
                song_details = driver.find_elements(
                    By.XPATH, "//div[contains(@class, 'main_page_category_music_txt')]")
                for k in song_details:
                    if (songs[i] in k.get_attribute("outerHTML")) and (artists[i] in k.get_attribute("outerHTML")):
                        song_target = k
                if song_target == '':
                    raise Exception
            except Exception:
                if j == 4:
                    play(r"C:\Windows\Media\Ring01.wav", SND_FILENAME)
                    next = input(
                        'Would you like to skip this song? (y/n) ')
                    if next.lower() == 'y':
                        break
                else:
                    sleep(1)

        song_target.click()
        dlButton = driver.find_elements(By.CLASS_NAME, 'btn-download')[1]
        dlButton.click()
        sleep(1)
        print(f'Downloaded {songs[i]} - {artists[i]}')
    except Exception:
        print(f'ERROR: {songs[i]}, {artists[i]}')
        pass

    driver.execute_script("window.open('about:blank', 'blank');")
    driver.switch_to.window(driver.window_handles[1])
