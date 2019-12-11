#!/usr/bin/env pybricks-micropython

# import arm
import nav
# import color
import advnav
# import tasks.M07
from line import Line
from vector import Vector

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# tasks.M07.main()
# nav.driveDistance(1000)

# print(Line(
#     Vector(18, 33.25),
#     Vector(160, 33.25)
# ).intersects(Line(
#     Vector(129.5, 0),
#     Vector(129.5, 114)
# )))

# advnav.driveDistance(10, 50)
advnav.followCoordinatePath([
    Vector(40, 33.25),
    Vector(40, 88),
])



# advnav.turnToLookingDirection(Vector(0,-1))

# print(str(advnav.willCrossBlackLine(Vector(18, 33.25), Vector(160, 33.25))))

# arm.up()
# arm.open()
# wait(2000)
# arm.down()
# arm.close()
# arm.up()
# wait(5000)
# arm.open()
