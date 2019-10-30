from pybricks.ev3devices import (Motor)
from pybricks.parameters import (Port, Stop)

motorArmMovement = Motor(Port.C)
motorArmGrip = Motor(Port.D)

torque = 80

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