from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from time import sleep
from pyautogui import click as c
import sys

# Use the first argument as the URL
url = sys.argv[1]
url = url.split(" ")
for j in url:
    start = input("Which lecture to start from? ")
    start = 1 if start == "" else int(start)

    options = webdriver.EdgeOptions()
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    options.binary_location = edge_path

    options.add_argument(
        r"user-data-dir=C:\Users\Aarjav\AppData\Local\Microsoft\Edge\User Data"
    )
    options.add_argument("--disable-extensions")
    options.add_argument("profile-directory=Default")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Edge(r"C:\Users\Aarjav\edgedriver.exe", options=options)

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    driver.get(j)
    pdfs = driver.find_elements(
        By.XPATH, 
        "//div[@class='menuButton css-yk3n3m-MenuButton ecq12m83']"
    )
    try:
        resume = driver.find_element(By.XPATH, "//h4[contains( text( ), 'Resume' )]")
        skip = True
    except:
        skip = False

    for i in pdfs:
        wait(driver, 30).until(lambda x: x.find_elements(By.XPATH, "//div[@class='menuButton css-yk3n3m-MenuButton ecq12m83']"))
        driver.execute_script("window.scrollBy(0, 180)", "")
        if skip == True:
            skip = False
            continue
        if start != 1:
            start -= 1
            continue
        i.click()
        sleep(1)
        link = driver.find_elements(By.XPATH, "//p[contains( text( ), 'With annotation' )]")
        if isinstance(link, list):
            link[0].click()
        else:
            link.click()
        wait(driver, 30).until(lambda x: x.find_elements(By.XPATH, "//div[@class='menuButton css-yk3n3m-MenuButton ecq12m83']"))
        c(x=222, y=543)
    
    sleep(2)
    driver.quit()