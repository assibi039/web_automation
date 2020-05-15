from selenium import webdriver

from selenium.webdriver.common.keys import Keys

n=1

while(n):
    driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.surveymonkey.com/r/56JD76D')

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[1]/div/div/fieldset/div/div/div[2]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[2]/div/div/fieldset/div/div/div[1]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[3]/div/div/fieldset/div/div/div[2]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[4]/div/div/fieldset/div/div/div[2]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[5]/div/div/fieldset/div/div/div[3]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[6]/div/div/fieldset/div/div/div[2]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[7]/div/div/fieldset/div/div/div[3]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[8]/div/div/fieldset/div/div/div[2]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[9]/div/div/fieldset/div/div/div[1]/div/label/span[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[10]/div/div/div/div/table/tbody/tr/td[10]/div/label/span[1]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[2]/button')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[2]/button[2]')

    elem.click()

    elem = driver.find_element_by_xpath('/html/body/main/article/section/form/div[2]/button[2]')

    elem.click()

    driver.quit()
    n=n-1



