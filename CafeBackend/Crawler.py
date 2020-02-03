from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import json


class Crawler:
    def __init__(self):
        self.buttons = []
        self.elements = []

        # Uncomment chrome_options to run the crawler headless (without window)
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def nav(self, location):
        if location == 'food':
            self.nav_food()

    def nav_food(self):
        self.driver.get('https://avonoldfarms.flikisdining.com/menu/avon-old-farms?mode=browse')

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//button[@class='primary']").click()

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//li[@class='menu-item']//a").click()

        temp = self.driver.find_elements_by_xpath("//ul[@class='items']")


        r = ""
        for i in range(len(temp)):
            temp[i] = temp[i].text
            r += temp[i] + "\n"
        r = r.split('\n')


        temp = []
        for i in r:
            if "Hotline" in i:
                print("breakfast")
                self.elements.append(temp)
                temp = []
            else:
                print(i)
                temp.append(i)

        self.elements = self.elements[1:]


    def get_elements(self):
        return self.elements


    def quit(self):
        self.driver.close()


if __name__ == '__main__':
    c = Crawler()
    c.nav('food')
    input("Type any key to quit: ")
    c.quit()
