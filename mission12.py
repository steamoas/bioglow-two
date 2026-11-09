"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.tools import run_task, wait
from robot import *


async def mission12():
    await right_attach.run_until_stalled(500, duty_limit=15)
    await wait(333)
    await right_attach.run_angle(200, -20)
    await drive.straight(740)
    await drive.turn(85)
    await right_attach.run_until_stalled(500, duty_limit=15)
    await drive.straight(200)
    await right_attach.run_angle(100, -50)
    await drive.straight(-200)
    await drive.turn(-85)
    await drive.straight(-740)






if __name__ == '__main__':
    run_task(mission12())
