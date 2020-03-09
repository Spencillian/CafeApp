import datetime
import json
from Crawler import Crawler


def current_time():
    return datetime.datetime.now()

def hrs_min(t=None):
    if not t:
        hrs = datetime.datetime.now().time().hour
        mins = datetime.datetime.now().time().minute
        return (hrs * 100) + mins
    hrs = t.time().hour
    mins = t.time().minute
    return (hrs * 100) + mins


class CafeBase:
    def __init__(self):
        self._init_base()

    def _init_base(self):
        with Crawler() as c:
            c.nav('food')
            self.base = c.get_elements()
        print(self.base)

    # def package(self):

    def time_type(self):
        if current_time().weekday() in range(5):
            if hrs_min(None) <= 730 or (hrs_min(None) >= 645 and current_time().weekday() in [0, 1, 3]) \
                    or (hrs_min(None) >= 630 and current_time().weekday() in [2, 5]):
                return "Breakfast"


if __name__ == '__main__':
    base = CafeBase()
