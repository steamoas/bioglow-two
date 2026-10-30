"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.tools import run_task, wait
from robot import *


async def RUN1():

    await left_attach.run_until_stalled(-300, duty_limit=20)
    left_attach.reset_angle(-10)
    await drive.straight(500)
    await left_attach.run_target(200, 217)
    await drive.straight(-150)



if __name__ == '__main__':
    run_task(RUN1())
