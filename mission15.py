"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.tools import run_task, wait
from robot import *

async def mission15():
    await drive.straight(-5)
    drive.reset()
    await right_attach.run_until_stalled(500, duty_limit=15)
    await right_attach.run_angle(200, -35)

    await drive.straight(100)
    await drive.move_by(240, 430)
    await drive.turn(-27)
    await drive.straight(120)
    await drive.turn(15)

    await right_attach.run_angle(40, -40)
    await wait(1000)
    await right_attach.run_angle(85,25)
    await drive.straight(-10)
    await drive.turn(15)
    await right_attach.run_angle(100, 20)
    await drive.straight(5)
    await right_attach.run_angle(100, 25)


if __name__ == '__main__':
    run_task(mission15())
