import requests
import webbrowser
import time
from bs4 import BeautifulSoup
while(True):

    URL='https://www.amazon.in/dp/B07WLQS4F7/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07WLQS4F7&pd_rd_w=lenkl&pf_rd_p=1801b34c-8af9-42b5-8961-11f124edc99b&pd_rd_wg=dbvbf&pf_rd_r=8KTSJMRB3JHWYGZBN28S&pd_rd_r=bffbd03f-c0d0-483d-90d0-528e9a63ac29&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRjdUUk1YUUJVVzhSJmVuY3J5cHRlZElkPUEwMjg3OTc1VDJDSTFHSUdXNVFDJmVuY3J5cHRlZEFkSWQ9QTAxMTIzMDAzQ0UxVzlMR0U1UlhUJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='


    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')
    
    price = soup.find(id="priceblock_ourprice").get_text()

    my_price = float(price[2:4])

    print(my_price)

    if(my_price < 60):
        print("price is changed")
        webbrowser.open('https://www.amazon.in/dp/B07WLQS4F7/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07WLQS4F7&pd_rd_w=lenkl&pf_rd_p=1801b34c-8af9-42b5-8961-11f124edc99b&pd_rd_wg=dbvbf&pf_rd_r=8KTSJMRB3JHWYGZBN28S&pd_rd_r=bffbd03f-c0d0-483d-90d0-528e9a63ac29&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRjdUUk1YUUJVVzhSJmVuY3J5cHRlZElkPUEwMjg3OTc1VDJDSTFHSUdXNVFDJmVuY3J5cHRlZEFkSWQ9QTAxMTIzMDAzQ0UxVzlMR0U1UlhUJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==')
        time.sleep(5)
