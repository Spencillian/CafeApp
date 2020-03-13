import datetime
from Crawler import Crawler


# Database that manages the data for the API
class CafeBase:
    def __init__(self):
        self._init_base()
        # self.test()

    def _init_base(self):
        with Crawler() as c:
            c.nav()
            self.base = c.get_info()

    @staticmethod
    def hrs_min(t=None):
        if not t:
            hrs = datetime.datetime.now().time().hour
            minutes = datetime.datetime.now().time().minute
            return (hrs * 100) + minutes
        hrs = t.time().hour
        minutes = t.time().minute
        return (hrs * 100) + minutes

    def day_menu(self, day):
        day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][day]

        return {
            'breakfast': self.base[0].get(day, f"There is no breakfast menu for {day}"),
            'lunch': self.base[1].get(day, f"There is no lunch menu for {day}"),
            'dinner': self.base[2].get(day, f"There is no dinner menu for {day}"),
        }

    # def test(self):
    #     print(self.day_menu(0))


if __name__ == '__main__':
    base = CafeBase()
