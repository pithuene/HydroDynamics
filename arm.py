from pybricks.ev3devices import (Motor)
from pybricks.parameters import (Port, Stop)

import utils

motorArmMovement = Motor(Port.C)
motorArmGrip = Motor(Port.D)

torque = 80

grabDistance = [70, 80]


def up():
    motorArmMovement.run_until_stalled(100, Stop.HOLD, torque)


def down():
    # Komplett Hoch
    motorArmMovement.run_until_stalled(-100, Stop.HOLD, torque)


def open():
    motorArmGrip.run_until_stalled(-100, Stop.HOLD, torque)


def close():
    motorArmGrip.run_until_stalled(100, Stop.HOLD, torque)


def grab():
    open()
    down()
    close()
    up()


def approachGrab(us, nav):
    while (True):
        dist = utils.preciseDistance(us, 3)
        if(dist > 150):
            nav.driveDistance(100, 100)
        else:
            break

    while (True):
        dist = utils.preciseDistance(us, 10)
        if(dist < grabDistance[0]):
            # Back
            nav.driveDistance(-25, 50)
        elif (dist > grabDistance[1]):
            # Forward
            nav.driveDistance(25, 50)
        else:
            break
    grab()
