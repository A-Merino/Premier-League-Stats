from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_club_page(url):
    driver = webdriver.Firefox()
    driver.get(url)

    try:
        el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "stats_misc_9")))
    finally:
        return driver



def init_league_page(url, ids):
    # Creates Selenium driver and grabs website
    driver = webdriver.Firefox()
    driver.get(url)

    # Waits until the page loads the table we want to grab
    try:
        el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,ids)))
    finally:
        return driver
