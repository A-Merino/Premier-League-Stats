from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_loaded_page_id(url, ids):
    # Creates Selenium driver and grabs website
    driver = webdriver.Firefox()
    driver.get(url)

    # Waits until the page loads the element we want to grab
    return wait_id(driver, ids)



def init_loaded_page_class(url, clas):
    # Creates Selenium driver and grabs website
    driver = webdriver.Firefox()
    driver.get(url)

    # Waits until the page loads the element we want to grab
    return wait_class(driver, clas)


def wait_id(driver, ids):
    try:
        el = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID,ids)))
    finally:
        return driver


def wait_class(driver, clas):
    try:
        el = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,clas)))
    finally:
        return driver


def wait_part_link(driver, part):
    try:
        el = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,part)))
    finally:
        return driver

def init_main_driver():
    return webdriver.Firefox()