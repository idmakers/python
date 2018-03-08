import time
from selenium import webdriver


for i in range(1,2,1):
    driver = webdriver.Chrome('C:/Users/idmakers/AppData/Local/Programs/Python/Python36/chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get('https://stucis.ttu.edu.tw/login.php');
    schoolID = driver.find_element_by_name('ID')
    schoolID.send_keys('410306234')
    PWD = driver.find_element_by_name('PWD')
    PWD.send_keys('10timmy10')
    start= driver.find_element_by_name('Submit')
    start.click()
    driver.get('https://stucis.ttu.edu.tw/menu/selmenu.htm');
    driver.get('https://stucis.ttu.edu.tw/selcourse/FastSelect.php');
    CLASS = driver.find_element_by_name('EnterSbj')
    CLASS.send_keys('I4820\nW5530\nI4810\nG2740\nG4500\n')
    start= driver.find_element_by_name('Submit')
    start.click()
    driver.quit
