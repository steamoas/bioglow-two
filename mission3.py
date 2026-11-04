"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.tools import run_task, wait
from robot import *


async def mission3():
    await drive.straight(-5)
    drive.reset()

    await drive.straight(250)
    # await drive.turn(-90)
    # await drive.straight(445)
    await drive.move_by(0, 445)

    # await drive.turn(-90)
    # await drive.straight(120)

    await drive.move_by(-130, 0)

    await left_attach.run_time(200, 1000)
    await wait(1000)
    await left_attach.run_target(400, -90)

    await drive.straight(-650)
    await drive.arc(-AXLE_TRACK / 2, 130)



    drive.drive(90, 0)
    await wait(3500)

    await drive.straight(-115)

    await drive.turn(-90)
    await drive.straight(-190)
    await drive.straight(125)

    await drive.turn(-40)
    await drive.straight(-250)
    await drive.turn(75)
    await drive.straight(-600)





if __name__ == '__main__':
    run_task(mission3())
