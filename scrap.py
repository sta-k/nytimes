import calendar
import requests
import json
class Scrap:
    def __init__(self):
        self.calendar = calendar.TextCalendar()

    def get_url(self, url):
        r = requests.get(url)
        resp = []
        splitted = r.text.split('headline":"')
        for s in splitted:
            resp.append(s.split('","')[0])            
        return resp


    def get_month(self,year,m):
        if 2025>year>1851:
            datas = {}
            for day in self.calendar.itermonthdates(year, m):
                if day.month == m:
                    url = f'https://www.nytimes.com/sitemap/{year}/{m:02d}/{day.day:02d}/'
                    datas[f'{day.day:02d}{m:02d}{year}'] = self.get_url(url)                
            with open(f'{m}_{year}.json', 'w') as f:
                # json.dump(datas, f)
                print(f'going to save: {m}_{year}.json')
                json.dump(datas, f, indent=4) 
        else:
            print('Year must be between 1852-2025')    

    def get_year(self, year):
        for m in range(1,13):
            self.get_month(year,m)
    def scrap(self):
        for year in range(1894,1920):
            self.get_year(year)


s = Scrap()
s.scrap()
