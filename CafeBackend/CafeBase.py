import datetime
from Crawler import Crawler


# Database that manages the data for the API
class CafeBase:
    def __init__(self):
        self._init_base()
        # self.test()

    # Initializes or refreshes the database
    def _init_base(self):
        with Crawler() as c:
            c.nav()
            self.base = c.get_info()

    # For future use of the app wants menus based on time
    @staticmethod
    def hrs_min(t=None):
        if not t:
            hrs = datetime.datetime.now().time().hour
            minutes = datetime.datetime.now().time().minute
            return (hrs * 100) + minutes
        hrs = t.time().hour
        minutes = t.time().minute
        return (hrs * 100) + minutes

    # Returns an organized dict of the menu for a specific day
    # Days are 0-7 with 0 = Sun
    def day_menu(self, day):
        day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][day]

        return [
            {"title": 'Breakfast', "data": self.base[0].get(day, [])},
            {"title": 'Lunch', "data": self.base[1].get(day, [])},
            {"title": 'Dinner', "data": self.base[2].get(day, [])},
        ]

    # Test method for testing the return values of the database
    # def test(self):
    #     print(self.day_menu(0))


if __name__ == '__main__':
    base = CafeBase()
