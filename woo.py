import time
from selenium import webdriver
for i in range(1,10,1):
    driver = webdriver.Chrome('C:/Users/idmakers/AppData/Local/Programs/Python/Python35/chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get('https://wootalk.today/key/%E6%88%90%E4%BA%BA%E6%A8%A1%E5%BC%8F');
    time.sleep(5) # Let the user actually see something!
    start= driver.find_element_by_id('startButton')
    start.click()
    time.sleep(5)
    search_box = driver.find_element_by_id('messageInput')
    search_box.send_keys("187找色女")
    send = driver.find_element_by_id('sendButton')
    send.click()
    time.sleep(5) # Let the user actually see something!
