"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.tools import run_task, wait
from robot import *

async def RUN2():

    await drive.straight(660)
    await drive.straight(-680)




if __name__ == '__main__':
    run_task(RUN2())
