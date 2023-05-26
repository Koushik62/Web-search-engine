from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

url = " https://leetcode.com/problemset/all/?page="

def get_a_tags(url):
    driver.get(url)
    time.sleep(1)
    html= driver.page_source
    soup =BeautifulSoup(html,'html.parser')
    all_ques = soup.find_all('a')
    pattern = "/problem/"
    ans = []
    for i in all_ques:
      try:
         if pattern in i.get('href'):
             ans.append(i.get('href'))
      except:
          pass
    return ans
  
for i in range(1,56):
      my_ans=get_a_tags(url+str(i))
      time.sleep(5)
      with open('lc.txt','a') as f:
          for j in my_ans:
              f.write(j+'\n')
            
driver.quit()