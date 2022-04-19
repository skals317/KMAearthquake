from bs4 import BeautifulSoup
import requests

url = 'https://www.weather.go.kr/w/eqk-vol/search/korea.do?dpType=a'
        
response = requests.get(url)
    
if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        time = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(2) > span')
        time = time.get_text()
        mag = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(3) > span')
        mag = mag.get_text()
        dep = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(4) > span')
        dep = dep.get_text()
        maxint = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(5) > span')
        maxint = maxint.get_text()
        area = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(8) > span')
        area = area.get_text()
        map = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(9) > a')
        map = str(map)[9:86]

        print("발생시각 : "+time)
        print("규모 : M"+mag)
        print("깊이 : "+dep+"km")
        print("최대진도 : "+maxint)
        print("발생지역"+area)
        print("지도 : "+map)
else : 
        print(response.status_code)    
