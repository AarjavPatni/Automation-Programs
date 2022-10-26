
from this import d
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pyautogui import click as c
import sys

# Use the first argument as the URL
url = sys.argv[1]
url = url.split(" ")
for j in url:
    start = int(input("Which lecture to start from? "))
    if start == "":
        start = 1

    options = webdriver.ChromeOptions()
    brave_path = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
    options.binary_location = brave_path

    options.add_argument(
        r"user-data-dir=C:\Users\Aarjav\AppData\Local\BraveSoftware\Brave-Browser\User Data"
    )
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(
        chrome_options=options, executable_path=r"C:\Users\Aarjav\bravedriver.exe"
    )

    brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

    driver.get(j)
    pdfs = driver.find_elements_by_xpath(
        "//div[@class='ItemCard__MenuButton-sc-xrh60s-3 eNUrNs menuButton']"
    )
    try:
        resume = driver.find_element_by_xpath("//h4[contains( text( ), 'Resume' )]")
        skip = True
    except:
        skip = False

    for i in pdfs:
        driver.execute_script("window.scrollBy(0, 150)", "")
        if skip == True:
            skip = False
            continue
        if start != "":
            if start != 1:
                start -= 1
                continue
        i.click()
        sleep(1)
        link = driver.find_elements_by_xpath("//p[contains( text( ), 'With annotation' )]")
        if isinstance(link, list):
            link[0].click()
        else:
            link.click()
        sleep(4)
        c(x=222, y=543)
    driver.quit()

for j in url:
    keys = 