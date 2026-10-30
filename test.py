"""
Mission(s):
Setup:
Author(s):
"""

from robot import *
from pybricks.tools import run_task, wait

min = 1000000
min_kp = 0

async def test():
    global min, min_kp
    # await drive.straight(100)
    # await drive.turn(90)
    # await drive.straight(100)
    # await drive.turn(-90)
    # await drive.straight(100)
    # print(hub.imu.heading())

    for i in range (2000, 20000, 100):
        drive.reset()
        await drive.turn(90)
        await drive.turn(-90)
        error = abs(hub.imu.heading())
        if error < min:
            min = error
            min_kp=i
        print(i, error)
    print("the min error is: ", min," with a kp of ", min_kp)
if __name__ == '__main__':
    run_task(test())
