from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from urllib.error import HTTPError 


def get_missionary_links(url, out_file = None):
    
    # Request page
    
    try:
        page = urlopen(url)
    except HTTPError:
        print(f"Page not found: {url}")
        return None
        
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")    
    soup = BeautifulSoup(html, "html.parser")
    
    # Parse HTML
    try:
        
        header = soup.find_all("div", {"data-testid": "individualSummaryDescription"})[0]        
        missionary_name = header.find_all("h1")[0].text
      
        header = soup.find_all("div", {"data-testid": "timelineContainer"})[0]        
        entries = header.find_all("div", class_ = "timelineDrawer")
        
        birth_place = ""

        for entry in entries:
            drawer_title = entry.find_all("div", {"data-testid": "timelineDrawerTitle"})[0]
                       
            
            if "Born in" in str(drawer_title):
                birth_place = drawer_title.find_all("h4")[0].text[8:]
            
            
            if "Served<!-- --> in" in str(drawer_title):
                mission_name = drawer_title.find_all("a")[0].text 
                name = mission_name.replace("<!-- -->", "")
                                
                mission_date = drawer_title.find_all("div", class_= "hLFYFy")[0].text
                start_year = mission_date.split()[0]                
                                
                event_details = entry.find_all("div", class_ = "eventDetail")
                                
                mission_type = ""
                residence = "" 
                loc_served = ""
                
                for event in event_details: 
                    cur_text = event.text 
                    if "Mission Type" in cur_text:
                        mission_type = cur_text[12:]
                    if "Residence When Called" in cur_text:
                        residence = cur_text[21:]
                    if "Location Served" in cur_text:
                        loc_served = cur_text[15:]
                    
                data_row = [missionary_name, birth_place, name, loc_served, start_year, mission_type, residence, url]                
                
                if out_file:
                    out_file.writerow(data_row)
                else:
                    print(data_row)
                            
    except IndexError:
        print(f"Having trouble with {url}")


links = []
with open("data_collection/missionary_links_all_new.txt", "r") as f:
    for line in f:
        link = f"https://history.churchofjesuschrist.org{line.strip()}"
        links.append(link)

print(len(links))
          
with open("mission_info_new2.csv", "w", newline='', encoding='utf-8') as f:
    field_names = ["name", "birth_place", "mission", "loc_served", "year", "type", "residence", "url"]
            
    writer = csv.writer(f)
    writer.writerow(field_names)
    for i in range(len(links)):
        get_missionary_links(links[i], writer)
        if i > 0 and i % 1000 == 0:
            print(f"Finished {i} entries")
            
print("Done!")


# url = "https://history.churchofjesuschrist.org/chd/individual/lyman-palmer-pinkston-1912?lang=eng&timelineTabs=allTabs"
# get_missionary_links(url)
