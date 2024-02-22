from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_team_sites():
    url = "https://www.premierleague.com/clubs/"
    links = dict()
    d = init_driver(url)
    trs = d.find_elements(By.CSS_SELECTOR, "tr")
    for row in trs:
        overview = row.find_elements(By.CSS_SELECTOR, "a")
        if overview is not None:
            for i, o in enumerate(overview):
                if i % 2 == 0:
                    links[o.text] = {"Main Link":o.get_attribute("href")} 
    d.close()
    print(links)


def init_driver(url):
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"icon__arrow icon__arrow venue__arrow-icons")))
    finally:
        return driver

get_team_sites()

