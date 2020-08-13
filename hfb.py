from selenium import webdriver

from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')
driver.get('https://eduserve.karunya.edu/Login.aspx?ReturnUrl=%2f')

elem = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div[1]/div/div[2]/input')

elem.send_keys('URK17CS039')

elem = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div[2]/div/div[2]/input')

elem.send_keys('#HBprince700')

elem = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div[3]/div/input')

elem.click()


s1='/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr['
s2=']/td[5]/div/ul/li[5]/a'
for i in range(1,10):
    j=str(i)
    try:
        elem = driver.find_element_by_xpath(s1+j+s2)
        print(elem)
        elem.click()
    except:
        elem = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/div/input')
        elem.click()
        driver.quit()
