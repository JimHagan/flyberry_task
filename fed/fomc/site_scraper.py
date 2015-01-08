from bs4 import BeautifulSoup
import requests
from datetime import datetime

FED_CALENDAR_PAGE = "http://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"

def _grab_page(url):
    return requests.get(url)
    
    
def _get_soup_from_page_text(page_text):
    return BeautifulSoup(''.join(page_text))


def get_latest_fed_schedule():
    results = []
    page = _grab_page(FED_CALENDAR_PAGE)
    print "got page with status code: ", page.status_code
    soup = _get_soup_from_page_text(page.text)
    #print soup
    tables = soup.findAll("table")
    print "tables: ", len(tables)
    for tbl in tables:
        #print tbl.get("class")
        if tbl.get("class", [None])[0] in ["pressConference", "alternate"]:
            print "Processing press conference..."
            rows = tbl.findAll("tr")
            title = rows[0].text
            year = int(title.split()[0])
            print "Title %s, Year %d" % (title, year)
            remaining_data_rows = rows[1:]
            for r in remaining_data_rows:
                meeting_dict = {"group name": title, "year": year, "data_retrieval_date": str(datetime.utcnow())}
                for item in r.findAll("td"):
                    key = item.get("class", [])
                    if key:
                        meeting_dict[key[0]] = item.text
                        results.append(meeting_dict) 
    return results
            


def main(arg=None):
    schedules = get_latest_fed_schedule()
    for sch in schedules:
        print sch
        
if __name__ == '__main__':
    main()