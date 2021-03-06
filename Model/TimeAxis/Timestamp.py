import datetime
import time


def timestamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))
