import datetime
import json
from Crawler import Crawler


class CafeBase:
    def __init__(self):
        self._init_base()

    def _init_base(self):
        with Crawler() as c:
            c.nav()
            self.base = c.get_info()

    @staticmethod
    def hrs_min(t=None):
        if not t:
            hrs = datetime.datetime.now().time().hour
            mins = datetime.datetime.now().time().minute
            return (hrs * 100) + mins
        hrs = t.time().hour
        mins = t.time().minute
        return (hrs * 100) + mins

    def day_menu(self, day):
        if day is 0:
            day = 'Sun'
        elif day is 1:
            day = 'Mon'
        elif day is 2:
            day = 'Tue'
        elif day is 3:
            day = 'Wed'
        elif day is 4:
            day = 'Thu'
        elif day is 5:
            day = 'Fri'
        elif day is 6:
            day = 'Sun'

        return {
            'breakfast': self.base[0].get(day, f"There is no breakfast menu for {day}"),
            'lunch': self.base[1].get(day, f"There is no lunch menu for {day}"),
            'dinner': self.base[2].get(day, f"There is no dinner menu for {day}"),
        }

    # def test(self):
    #     print(self.day_menu(0))


if __name__ == '__main__':
    base = CafeBase()
