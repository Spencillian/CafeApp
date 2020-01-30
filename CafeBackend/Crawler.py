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
        # chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def nav(self, location):
        if location is 'food':
            self.nav_food()

    def nav_food(self):
        self.driver.get('https://avonoldfarms.flikisdining.com/menu/avon-old-farms?mode=browse')

        self.driver.implicitly_wait(2)

        self.driver.find_element_by_xpath("//button[@class='primary']").click()
        self.driver.find_element_by_xpath("//li[@class='menu-item']//a").click()

        temp = self.driver.find_elements_by_xpath("//ul[@class='items']")

        r = ""

        for i in range(len(temp)):
            temp[i] = temp[i].text
            r += temp[i]
            print(temp[i])

        print("------------------------------------------------")

        print(r)


        t = []
        for i, k in enumerate(temp):
            if i is 0:
                continue

            if k == "Hotline":
                print("fuck")
                self.elements.append(t)
                t = []
            else:
                print("suck")
                t.append(k)

        print(self.elements)


    def quit(self):
        self.driver.close()


if __name__ == '__main__':
    c = Crawler()
    c.nav('food')
    input("Type any key to quit: ")
    c.quit()
