from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import json
def get_user_name_password():
    config_data = None
    with open('config.json') as json_file:
        config_data = json.load(json_file)
    return config_data["facebook"]

if __name__ == "__main__":
    print("Web Scrapping iniciado ....")
    chromedrivepath = r"C:\Users\repes\PycharmProjects\pythonProject\chromedriver.exe"
    driver = webdriver.Chrome(chromedrivepath)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    user_detail = get_user_name_password()

    try:

        driver.find_element_by_xpath('//*[@id="email"]').send_keys(user_detail["user_name"])
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys(user_detail["password"])
        driver.find_element_by_xpath('//*[@id="u_0_b"]').click()

        wait = WebDriverWait(driver, 5)

        print(driver.title)

        feed_list = driver.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[3]/div')
        for feed in feed_list:
            print("feed: " + feed.text)

        driver.close()
    except Exception as ex:
        print(ex)
        print("Falha na conexao com facebook")
    print("Web scrappimg Completo")



