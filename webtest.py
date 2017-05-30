import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/idmakers/AppData/Local/Programs/Python/Python35/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://vmus.co');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_class_name('search-field')
name = input('請輸入名稱')
if(name != 0):
    search_box.send_keys(name)
    search_box.submit()
    time.sleep(5) # Let the user actually see something!
