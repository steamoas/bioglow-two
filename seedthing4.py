"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.tools import run_task, wait
from robot import *


async def seedthing4():
    await drive.straight(-10)
    await right_attach.run_until_stalled(400,duty_limit=20)
    await right_attach.run_angle(100,-108)
    await drive.straight(175)
    await drive.turn(50)
    await drive.straight(300)
    await right_attach.run_angle(200,70)
    await drive.straight(-150)
    await drive.straight(-250)

if __name__ == '__main__':
    run_task(seedthing4())
