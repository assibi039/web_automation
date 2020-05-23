
from selenium import webdriver

from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.youtube.com')

elem = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')



elem.send_keys('searsearch')

sea = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
sea.click()

driver.quit()

