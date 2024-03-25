import csv
from datetime import datetime
import time
from http.server import executable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromedriver_path="/Users/huios/NEXT/Session/NEXT_Session_6/dev/chromedriver"
user_data_dir="/Users/huios/NEXT/Session/NEXT_Session_6/data"

chrome_options=Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service=Service(executable_path=chromedriver_path)

driver=webdriver.Chrome(service=service, options=chrome_options)
## ERROR line 18
url = 'https://music.bugs.co.kr/genre/chart/kpop/rnh/total/day'
driver.get(url)
a=[]
b=[]
c=[]
#practice1
titles = driver.find_elements(By.CLASS_NAME, 'title')
for title in titles:
    a.append(title.text)
    print(title.text)

artists = driver.find_elements(By.CLASS_NAME, 'artist')
for artist in artists:
    b.append(artist.text)
    # print(artist.text)
    
albums = driver.find_elements(By.CLASS_NAME, 'album')
for album in albums:
    c.append(album.text)
    # print(album.text)
    
# print(titles)
today=datetime.now().strftime('%Y%m%d')
file=open(f'bugs_{today}.csv', mode='w', newline='')
writer=csv.writer(file)
# writer.writerow(["titles","artists","albums"])

########
print(len(a), len(b), len(c))
for i in range(len(artists)):
    writer.writerow([a[i+2],b[i],c[i]])
time.sleep(3)
#######
file.close()
# #practice5
# infos=driver.find_elements(By.XPATH, '//*[@id="lst50"]')
# for i, info in enumerate(infos, start=1):
#     rank=i
    
#     title=info.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a").text
#     singer=info.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[2]/a").text
    
#     writer.writerow([rank,title,singer])
#     print(rank,title,singer)
# file.close()
# time.sleep(3)
