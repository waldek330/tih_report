import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.packaging import workbook
#log on to page
options = Options()
options.headless = True
options.add_argument("--ignore-certificate-errors") 
options.add_argument("--headless")
options.add_argument("window-size=1920,1080") 
options.add_argument("disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
driver = webdriver.Chrome(executable_path=r"C:\\users\\walde\\Downloads\\chromedriver.exe", options=options)
#driver = webdriver.Chrome(r"C:\Users\walde\Downloads\chromedriver.exe")  # webdriver path
driver.get("https://IVY-RTV-R03:twinz992@cdmv.ups-scs.com/CDMvSPL/remote/rtvSimpleStockEnquiry")

#cdmv operations
depot = driver.find_element_by_id("depotcode")
depot.send_keys("90001")
zone = driver.find_element_by_id("zone")
zone.send_keys("TEST_INHOUSE_INTEST")
search_button = driver.find_element_by_name("pressedButtons(search).value")
search_button.click()
tabel = driver.find_element_by_id("scroller_row")
excel_download = driver.find_element_by_id("_exp_1")
excel_download.click()
driver.quit() 
#closing driver

#excel operations
