#!/usr/bin/env python
# random_sleep requirements
from __future__ import division
import time
import random


# compatibility layer between Python 2 and Python 3
import future
import six

# Performance testing using monotonic():
# Python 3.3 or older:
import datetime
from monotonic import monotonic
# Python 3.4 or newer:
#import datetime
#from datetime import monotonic

# How many milliseconds to sleep
# Defaults:  min - 10 milliseconds, max - 100 ms
# pass paramaters to increase/decrease default range
def randomsleep(maxlimit=100,minlimit=10):
    time.sleep(random.randint(minlimit,maxlimit) / 1000.0)

start_time = monotonic()
randomsleep
end_time = monotonic()
print(datetime.timedelta(seconds=end_time - start_time))


start_time = monotonic()
randomsleep(1000)
end_time = monotonic()
print(datetime.timedelta(seconds=end_time - start_time))


start_time = monotonic()
randomsleep(1000, 999)
end_time = monotonic()
print(datetime.timedelta(seconds=end_time - start_time))


start_time = monotonic()
randomsleep(minlimit=990, maxlimit=991)
end_time = monotonic()
print(datetime.timedelta(seconds=end_time - start_time))
