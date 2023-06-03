import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import webDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

headingclass = ".mr2-2.text-label-1"
bodyclass =".px-5.pt-4"
index =1
Qdata_folder ="Qdata"



def get_array_of_links():
    
    arr = []

    with open("lc_problems.txt","r") as file:
        for line in file:
            arr.append(line)
    return arr

def add_text_to_index_file(text):
    index_file_path = os.path.join(Qdata_folder,"index.txt")
    with open(index_file_path,"a") as index_file:
        index_file.write(text+"\n")

def add_links_to_Qindex_file(text):
    index_file_path = os.path.join(Qdata_folder,"Qindex.txt")
    with open(index_file_path,"a") as Qindex_file:
        Qindex_file.write(text)



def create_and_add_text_to_file(filename, text):
    folder_path = os.path.join(Qdata_folder,filename)
    os.makedirs(folder_path,exist_ok=True)
    file_path = os.path.join(folder_path,filename+".txt")
    with open(file_path, "w") as new_file:
       new_file.write(text)
    
def getpageData(url, index):
    try:
        driver.get(url)
        webDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,bodyclass)))
        time.sleep(1)
        heading = driver.find_element(By.CSS_SELECTOR,headingclass)
        body = driver.find_element(By.CSS_SELECTOR,bodyclass)
        print(heading.text)
        if(heading.text):
            add_text_to_index_file(heading.text)
            add_links_to_Qindex_file(url)
            create_and_add_text_to_file(str(index),body.text)
        time.sleep(1)
        return True
        
        
    except Exception as e:
        print(e)
        return False

arr = get_array_of_links()
for links in arr:
    success = getpageData(links,index)
    if(success):
      index = index+1


driver.quit()      
     
