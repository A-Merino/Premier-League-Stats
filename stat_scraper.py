from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_team_sites(url):
    links = dict()
    d = init_driver(url)
    table = d.find_element(By.ID, "results2017-201891_overall")
    bod = table.find_element(By.CSS_SELECTOR, "tbody")
    trs = bod.find_elements(By.CSS_SELECTOR, "tr")
    for row in trs:
        o = row.find_element(By.CSS_SELECTOR, "a")
        # print(overview.text)   
    #     if overview is not None:
    #         for i, o in enumerate(overview):
    #             if i % 2 == 0:
        links[o.text] = {"Main Link":o.get_attribute("href")} 
    d.close()
    return links


def init_driver(url):
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"results2017-201891_overall")))
    finally:
        return driver


def main():
    years = {"17-18": {"Overview":"https://fbref.com/en/comps/9/2017-2018/2017-2018-Premier-League-Stats"},
             "18-19": {"Overview":"https://fbref.com/en/comps/9/2018-2019/2018-2019-Premier-League-Stats"},
             "19-20": {"Overview":"https://fbref.com/en/comps/9/2019-2020/2019-2020-Premier-League-Stats"},
             "20-21": {"Overview":"https://fbref.com/en/comps/9/2020-2021/2020-2021-Premier-League-Stats"},
             "21-22": {"Overview":"https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats"},
             "22-23": {"Overview":"https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats"}}
    for year, link in years.items():
        print(year, link)
        dic = get_team_sites(link["Overview"])
        years[year]["Teams"] = dic
    print(years)

main()