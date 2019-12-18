import advnav
import arm
import time
import color
from vector import Vector


def main():
    arm.close()
    arm.up()
    advnav.followCoordinatePath([
        # Vector(140, 16),
        Vector(155, 25),
    ])
    advnav.turnToLookingDirection(Vector(11, 37).normalize())
    advnav.driveDistance(11.5, 50)
    arm.down()
    time.sleep(2)
    arm.up()
    advnav.driveDistance(-10)
    advnav.turn(-85)
    advnav.driveDistance(200)
