from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
from openpyxl import Workbook

url = 'https://info.korea.ac.kr/info/board/notice_under.do'
L = []
try:
    headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    if response.status_code == 200:
        html_text = response.text
        
        soup = bs(html_text, 'html.parser')
        
        # notice=soup.find_all(class_='top-notice-bg')
        # notice = list(map(lambda x: x. text.strip(), notice))
        
        notice=soup.find_all('td')
        notice = list(map(lambda x: x. text.strip(), notice))
        print(len(notice)) # 5 묶음
        nums=[]
        titles=[]
        authors=[]
        amounts=[]
        dates=[]
        for i in range(len(notice)):
            if i%5==0:
                nums.append(notice[i])
            if i%5==1:
                titles.append(notice[i])
            if i%5==2:
                authors.append(notice[i])
            if i%5==3:
                amounts.append(notice[i])
            if i%5==4:
                dates.append(notice[i])

        wb = Workbook()
        ws = wb.active
        
        ws.append(["번호","제목","작성자", "조회수", "작성일"])
        
        for i, (num, title, author, amount, date) in enumerate(zip (nums, titles, authors, amounts, dates), start=1):
            ws.append([num, title, author, amount, date])   
        
        today = datetime.now().strftime('%Y%m%d')
        
        filename = f'KU_{today}.xlsx'
        wb.save(filename)
        # print(f"엑셀 저장완료: {filename}")
        
    else: 
        print(f"Error: HTTP 요청 실패. 상태코드; {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Error: 요청 중 오류 발생. 오류메세지:{e}")