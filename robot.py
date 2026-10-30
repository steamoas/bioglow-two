from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

hub = PrimeHub()

#Drive Motors
left_drive = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_drive =Motor(Port.A, Direction.CLOCKWISE)


#Attachment Motors
left_attach = Motor(Port.B, Direction.CLOCKWISE, gears=[12, 20])
right_attach = Motor(Port.F, Direction.CLOCKWISE, gears=[12,20])

AXLE_TRACK=120

drive = DriveBase(left_drive,right_drive, 62, AXLE_TRACK)

drive.use_gyro(True)
drive.heading_control.pid(11200*.75, 8, 1900, 2, 7)
# drive.heading_control.pid(7000, 4,  2000, 2, 7)



# (7558, 0, 1889, 4, 7)

