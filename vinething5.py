"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.tools import run_task, wait
from robot import *


async def vinething5():


    await wait(100)
    await right_attach.run_angle(500,-60)
    await left_attach.run_until_stalled(500, duty_limit=15)
    await left_attach.run_angle(200, -40)
    await drive.straight(250)
    await drive.turn(40)
    await drive.straight(450)
    await drive.turn(50)
    await drive.straight(220)
    await drive.turn(-90)
    await drive.straight(210)
    await left_attach.run_angle(300,-40)
    await drive.straight(-200)


if __name__ == '__main__':
    run_task(vinething5())
