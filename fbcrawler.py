from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import json
import time
def get_user_name_password():
    config_data = None
    with open('config.json') as json_file:
        config_data = json.load(json_file)
    return config_data["facebook"]

if __name__ == "__main__":
    print("Web Scrapping iniciado ....")
    chromedrivepath = r"C:\Users\repes\Desktop\Big Data\Coleta de dados\Crawler\chromedriver.exe"
    driver = webdriver.Chrome(chromedrivepath)
    driver.maximize_window()

    user_detail = get_user_name_password()
    page_name = user_detail["page_name"]
    LOGIN_URL = 'https://www.facebook.com/login'
    REQUEST_URL = f'https://www.facebook.com/{page_name}/settings/?tab=people_and_other_pages&ref=page_edit'
    driver.get(LOGIN_URL)

    time.sleep(2)
    scrolls = 15
    try:

        driver.find_element_by_xpath('//*[@id="email"]').send_keys(user_detail["user_name"])
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys(user_detail["password"])
        driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

        wait = WebDriverWait(driver, 5)

        print(driver.title)

        driver.get(REQUEST_URL)

        for i in range(1, scrolls):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            page = driver.page_source
            soup = BeautifulSoup(page, "html.parser")
            names = soup.find_all('a', class_='_3cb8')
            people_who_liked_page = []
            for name in names:
                people_who_liked_page.append(name.text)
    except Exception as ex:
        print(ex)
        print("Falha na conexao com facebook")
    print("Web scrappimg Completo")


