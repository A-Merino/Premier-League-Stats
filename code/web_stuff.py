from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



    

def runSite(site, tname, datapoints):

    # Starts a new weddriver window and puts in the site
    driver = webdriver.Firefox()
    driver.get(site)


    players = []

# Traverses through the html from player table => tbody => table rows
    table = driver.find_element(By.ID, tname)
    bod = table.find_element(By.CSS_SELECTOR, "tbody")
    trs = bod.find_elements(By.CSS_SELECTOR, "tr")
    

    # Go through each of the table tr tags
    name = ""
    count = 1
    for row in trs:
        # If the tag has the "thead" class it is not the data we want
        if row.get_attribute("class") == 'thead':
            continue

        # Create a list of each td tag to iterate through
        data = row.find_elements(By.CSS_SELECTOR, "td")
        pd = []
        for d in data:
            # Check to see if data is in list, if not, don't collect it
            if d.get_attribute("data-stat") not in datapoints:
                continue

            elif d.get_attribute("data-stat") == 'player':
                # Players have funny letters in their names, change all of them to ?
                pd.append(d.find_element(By.CSS_SELECTOR, "a").get_attribute("href"))
                n = d.text.encode(encoding="ascii",errors="replace").decode(encoding="ascii")
                
                # If player played for two teams in one season then add number to name
                if n == name:
                    pd.append(n+str(count))
                    name = n+str(count)
                    count += 1
                else:
                    count = 1
                    pd.append(n)
                    name = n
                    
            elif d.text == '':  # If empty then put a 0
                pd.append("0")

            elif d.get_attribute("data-stat") == 'nationality':
                pd.append(d.text.split(' ')[1])  # Formatting to make data clean

            elif d.get_attribute("data-stat") == 'position':
                pd.append(d.text.split(',')[0])  # Formatting to get rid of two position type
            elif "," in d.text:
                pd.append(d.text.replace(",", ""))
            else:
                pd.append(d.text)
        players.append(pd)

    # Close site and return list of players
    driver.close()
    return players
