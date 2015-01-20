from bs4 import BeautifulSoup
import requests
#import string
from datetime import datetime
from fomc.models import populate_projection_tables

FED_INFO_ROOT = "http://www.federalreserve.gov"
FED_CALENDAR_PAGE = FED_INFO_ROOT + "/monetarypolicy/fomccalendars.htm"

def _grab_page(url):
    return requests.get(url)
    
    
def _get_soup_from_page_text(page_text):
    return BeautifulSoup(''.join(page_text))


#TODO: This is not efficient but we know it and should fix it.
def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeEncodeError:
        return False

def format_cell(cell):
    raw = cell.strip().replace('\n', '')
   
    if (raw == "-"):
        return None
    elif (raw == ""):
        return None
    else:
        try:
            val = float(raw) if "." in raw else int(raw)
            return val
        except:
            #print raw
            fixed =  "".join([r for r in raw if is_ascii(r)])
            return fixed
     
        

def parse_projection_tables(page_url):
    page = _grab_page(page_url)
    soup = _get_soup_from_page_text(page.text)
    subhead_spans = soup.findAll("span", "tablesubhead")
    tables = []
    for s in subhead_spans:
        if s:
            units = s.findNextSibling("span")
            table = {"name": s.text.lower().replace(' ', '_'),"units": units.text if units else 'unknown', "dat": []}
            table_div = s.parent.findNextSibling("div")
            
            #TODO: remove this next two line kludge.
            if not table_div:
                table_div = s.parent.findNextSibling("table")

            if table_div.get("class", [])[0] in ["page", "pubtables"]:
                table_header = table_div.findNext('thead')
                items = table_header.findAll("tr")[0]
                raw_header_list = [format_cell(i.text) for i in items.findAll("th")]
              
                table["dat"].append(raw_header_list)
                table_body = table_div.findNext('tbody')
                rows = table_body.findAll("tr")
                for r in rows:
                    raw_row_data = [format_cell(col.text) for col in r.findAll('td')]
                    table["dat"].append(raw_row_data)
                tables.append(table)
    return tables
                

def parse_fed_schedules():
    date_now = datetime.utcnow()
    results = []
    page = _grab_page(FED_CALENDAR_PAGE)
    #print "got page with status code: ", page.status_code
    soup = _get_soup_from_page_text(page.text)
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
                        if "video" in key:
                            if "Projections Material" in item.text:
                                _top_level_link = item.get("href", "").lower()
                                if "projtab" in _top_level_link:
                                    if ".pdf" in _top_level_link:
                                         meeting_dict["projections_pdf_url"] = FED_INFO_ROOT + _link
                                    elif ".htm" in top_level_link:
                                        meeting_dict["projections_html_url"] = FED_INFO_ROOT + _link
                                links = item.findAll("a")
                                for l in links:
                                    _link =  l.get("href").lower()
                                    if "projtab" in _link:
                                        if ".pdf" in _link:
                                            meeting_dict["projections_pdf_url"] = FED_INFO_ROOT + _link
                                        elif ".htm" in _link:
                                            meeting_dict["projections_html_url"] = FED_INFO_ROOT + _link 
                                        
                        meeting_dict[key[0]] = item.text
                
                if  "projections_html_url" in meeting_dict:
                    print "processing meeting row for ", meeting_dict["projections_html_url"]                    
                    meeting_dict["parsed_proj_table_body"] = parse_projection_tables(meeting_dict["projections_html_url"])
                    #print meeting_dict["parsed_proj_table_body"]
                results.append(meeting_dict) 
    return results
            


def main(arg=None):
    schedules = parse_fed_schedules()
    for sch in schedules:
        print sch
    
        
if __name__ == '__main__':
    main()