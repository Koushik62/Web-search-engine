from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# Define the chrome driver service
s = Service('chromedriver.exe') 

#Initiate the webdriver
driver = webdriver.Chrome(service=s)  

# the base url of the page to scrap
page_url ="https://leetcode.com/problemset/all/?page=" 


#function to get all 'a' tags from a given url

def get_a_tags(url):
    
    #load the url in the browser
    driver.get(url)
    #wait for 5 seconds to ensure that the page is fully loaded
    time.sleep(5)
    #find all the 'a' elements on the page
    links= driver.find_elements(By.TAG_NAME,"a")
    ans =[]
    #iterate over each element
    for i in links:
        try: 
            #check if '/problems/' is the href of 'a' element
            if "/problems/" in i.get_attribute("href"):
            #if it is append it to the list of links
             ans.append(i.get_attribute("href"))
        except:
            pass   
        #remove the duplicate elements using set
    ans = list(set(ans))
    return ans

#list to store the final list of links
my_ans =[]
# loop through all pages(1,55)

for i in range(1,55):
    my_ans+=(get_a_tags(page_url+str(i))) # in each and every page add all questions
    
    #removing the duplicates
my_ans=list(set(my_ans))
    
    
#open a file to write the results

with open('leetcode.txt','a') as f:
    #iterate over each link in your final list
    
   for j in my_ans:
              f.write(j+'\n')
print(len(my_ans))

driver.quit()   