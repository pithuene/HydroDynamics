from pybricks.ev3devices import (Motor)
from pybricks.parameters import (Port, Stop)

import utils

motorArmMovement = Motor(Port.C)  # Motor der den Arm hoch und runter fährt
motorArmGrip = Motor(Port.D)  # Motor der die Schaufel auf und zu bewegt

torque = 80  # Drehmoment bei dem die Motoren aufhören sollen zu drehen

# Entfernung vom Ultraschallsensor, in der das Objekt noch gegriffen werden kann
grabDistance = [70, 80]


def up(angle=0):
    if(angle != 0):
        motorArmMovement.run_angle(100, angle, Stop.HOLD)
    else:
        motorArmMovement.run_until_stalled(100, Stop.HOLD, torque)


def down():
    # Arm fährt in die niedrigste Position
    motorArmMovement.run_until_stalled(-100, Stop.HOLD, torque)


def open():
    # Die Schaufel fährt soweit auf wie möglich
    motorArmGrip.run_until_stalled(-100, Stop.HOLD, torque)


def close():
    # Die Schaufel schließt so weit wie möglich
    motorArmGrip.run_until_stalled(100, Stop.HOLD, torque)

# Roboter greift zu


def grab():
    open()
    down()
    close()
    up()

# Roboter misst Distanz zu einem Objekt und nährt sich so lange bis es in Greifreichweite ist, dann greift er zu


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
