from bs4 import BeautifulSoup
import requests
from datetime import datetime

FED_INFO_ROOT = "http://www.federalreserve.gov"
FED_CALENDAR_PAGE = FED_INFO_ROOT + "/monetarypolicy/fomccalendars.htm"

def _grab_page(url):
    return requests.get(url)
    
    
def _get_soup_from_page_text(page_text):
    return BeautifulSoup(''.join(page_text))


def get_latest_fed_schedule():
    date_now = datetime.utcnow()
    results = []
    page = _grab_page(FED_CALENDAR_PAGE)
    print "got page with status code: ", page.status_code
    soup = _get_soup_from_page_text(page.text)
    #print soup
    tables = soup.findAll("table")
    print "tables: ", len(tables)
    for tbl in tables:
        if tbl.get("class", [None])[0] in ["pressConference", "alternate"]:
            print "Processing press conference..."
            rows = tbl.findAll("tr")
            title = rows[0].text
            year = int(title.split()[0])
            print "Title %s, Year %d" % (title, year)
            remaining_data_rows = rows[1:]
            for r in remaining_data_rows:
                meeting_dict = {"group name": title, "year": year, "scrape_date": str(date_now)}
                for item in r.findAll("td"):
                    key = item.get("class", [])
                    if key:
                        if "statement2" in key:
                            #In a production version, I'd scrape th raw statement as well.
                            meeting_dict["statement_url"] = FED_INFO_ROOT + item.a.get("href") if item.a else None
                        meeting_dict[key[0]] = item.text
                results.append(meeting_dict) 
    return results
            


def main(arg=None):
    schedules = get_latest_fed_schedule()
    for sch in schedules:
        print sch
        
if __name__ == '__main__':
    main()