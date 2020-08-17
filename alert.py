import webbrowser
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from autologin import AutoLogin

url = 'https://www.7cups.com/login.php'
username = 'shonfrost69@gmail.com'
password = 'bh^yyG5Yu'
al = AutoLogin()
cookies = al.auth_cookies_from_url(url, username, password)

'''
driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.7cups.com/login.php')

elem = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/form/div[1]/input')

elem.send_keys('shonfrost69@gmail.com')

sea = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/form/div[2]/input')

sea.send_keys('bh^yyG5Yu')

doi = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/form/div[3]/button')

doi.click()

driver.quit()
'''
