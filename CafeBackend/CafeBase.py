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
        self.test()

    def _init_base(self):
        with Crawler() as c:
            c.nav('food')
            self.base = c.get_elements()
        print(self.base)

    def menu(self, day):
        return self.base.get(day)

    def test(self):
        print(self.menu(0))


if __name__ == '__main__':
    base = CafeBase()
