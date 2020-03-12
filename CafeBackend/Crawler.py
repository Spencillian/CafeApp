from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json


class Crawler:
    def __init__(self):
        self.buttons = []
        self.menu = []

        # Uncomment chrome_options to run the crawler headless (without window)
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def nav(self):
        # Navigate to the Flik Dining website
        self.driver.get('https://avonoldfarms.flikisdining.com/menu/avon-old-farms?mode=browse')

        # Click on a button to go to the menus
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//button[@class='primary']").click()


        # --------------------- Breakfast ------------------------
        # Select the breakfast menu from the list of menus
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[@class='menu-item']//a").click()

        # TODO: Comment this out to reflect the correct menu for this week
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//li[@class='arrow']//a").click()

        # TODO: Get the menus for the entire month
        # self.driver.implicitly_wait(5)
        # Select(self.driver.find_element_by_xpath("//select")).select_by_index(2)

        # Get the information from the web menus
        week = self._get_menu()

        # Adds the breakfast foods to the crawler's menu
        self.menu.append(self._package(week))
        print(self.menu[0])


        # --------------------- Lunch ------------------------
        # Go to the Lunch menu
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_xpath("//ul[@class='nav-content']//li//a")[2].click()

        # Get the foods and dates from the Lunch menu
        week = self._get_menu()

        # Add the Lunch menu to the crawler's menu
        self.menu.append(self._package(week))
        print(self.menu[1])


        # --------------------- Dinner ------------------------
        # Go to the Dinner menu
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_xpath("//ul[@class='nav-content']//li//a")[3].click()

        # Get the foods and dates from the Dinner menu
        week = self._get_menu()

        # Add the Dinner menu to the crawler's menu
        self.menu.append(self._package(week))
        print(self.menu[2])


    def _package(self, elem_arr):
        for i, item in enumerate(elem_arr):
            elem_arr[i] = item.text

        val = {}
        day = ""
        for item in elem_arr:
            try:
                int(item[0])
                day = item[-3:]
                val[day] = []
            except ValueError:
                val[day].append(item)
        return val

    def _get_menu(self):
        # Make sure that the food items in the web menu are there
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_xpath("//li[@class='day']//ul[li[@class='food text-links']]")

        # Make sure that the dates on the web menu are there
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_xpath("//li[@class='day']//h3")

        # Get the food items and dates from the web menu
        self.driver.implicitly_wait(10)
        return self.driver.find_elements_by_xpath("//li[@class='day']//ul[@class='items']//li[@class='food text-links']"
                                                  " | //li[@class='day']//h3")

    # Get menus in dict form
    def get_info(self):
        # TODO: Return conglomerate of menu
        return self.menu

    # Get menus in json form
    def get_json(self):
        return json.dumps(self.menu)

    # Quit the driver
    def quit(self):
        self.driver.close()

    # Function that allows the Crawler to be used with encapsulation
    def __enter__(self):
        return self

    # Manages when the code leaves the encapsulation
    def __exit__(self, t, value, traceback):
        self.quit()


if __name__ == '__main__':
    with Crawler() as c:
        c.nav()
        input("Type any key to quit: ")
