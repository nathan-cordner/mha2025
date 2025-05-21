from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def get_html(url):
    browser = webdriver.Chrome()
    browser.get(url)
    
    delay = 30 # seconds
    while True:
        try:
            # check if javascript is loaded
            WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "listItem")))
        except TimeoutException:
            break
        else:
            break

    html = browser.page_source
    return BeautifulSoup(html, features="html.parser")

def get_missionary_links(index, file):
    url = f"https://history.churchofjesuschrist.org/chd/search?tabFacet=people&tabSubfacet=missionaries&lang=eng&start={index}"
    soup = get_html(url)
    
    try:
        header = soup.find_all("aside", class_ = "searchBody")[0]
        if not header:
            f.write(f"found nothing at index {index}\n")
            return
        
        links = header.find_all("a")
        if not links:
            f.write(f"found nothing at index {index}\n")
            return
        # f.write(f"Starting at {index}\n")
        for link in links:
            f.write(link['href'] + "\n")
                
    except IndexError:
        f.write(f"Having trouble with {index}\n")
        
indices = list(range(0, 46960, 25))

"""
with open("missionary_links4.txt", "r") as f:
    for line in f: 
        if "found nothing" in line:
            items = line.split()
            val = items[-1].strip() 
            indices.append(int(val))
"""

with open("missionary_links_all_new.txt", "w") as f:
    for index in indices:
        get_missionary_links(index, f)
        if index > 0 and index % 1000 == 0:
            print(f"Finished {index} entries")
    

    
    
    
    
    
    