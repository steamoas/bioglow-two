"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.parameters import Button, Color
from pybricks.tools import run_task, wait, multitask

from mission12 import mission12
from mission15 import mission15
from robot import *
from mission3 import mission3
from vinething5 import vinething5

programs = []
programs.append(0)
programs.append(mission3) #1
programs.append(mission12)
programs.append(mission15)
programs.append(vinething5)

async def center_button_pressed():
    while Button.CENTER in hub.buttons.pressed():
        await wait(15)
    while True:
        if Button.CENTER in hub.buttons.pressed():
            return
        await wait(100)

async def switcher():
    hub.system.set_stop_button((Button.LEFT,Button.RIGHT))
    program_num = 1
    hub.display.number(1)
    default_settings = drive.settings()
    hub.light.on(Color.RED)
    while True:
        await wait(50)

        buttons = hub.buttons.pressed()
        if Button.LEFT in buttons:
            program_num -= 1
            if program_num < 1:
                program_num = len(programs) - 1
            hub.display.number(program_num)
            while Button.LEFT in hub.buttons.pressed():
                await wait(20)

        elif Button.RIGHT in buttons:
            program_num += 1
            if program_num == len(programs):
                program_num = 1
            hub.display.number(program_num)
            while Button.RIGHT in hub.buttons.pressed():
                await wait(20)

        elif Button.CENTER in buttons:
            hub.light.on(Color.GREEN)
            drive.reset()
            hub.imu.reset_heading(0)
            await multitask(programs[program_num](), center_button_pressed(), race=True)
            drive.settings(*default_settings)
            left_attach.stop()
            right_attach.stop()
            drive.stop()
            hub.light.on(Color.RED)
            while Button.CENTER in hub.buttons.pressed():
                await wait(15)


run_task(switcher())



