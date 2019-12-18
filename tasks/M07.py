#Fountain - fertig // testen

import nav
import arm

M07 = [[0, 0], [8.1, 0], [8.1, -0.25]]  # x und y Koordinaten


def main():
    arm.open()
    arm.down()
    arm.close()
    arm.up()
    nav.followCoordinatePath(M07)
    arm.down()
    arm.open()
    arm.up()
    arm.close()
    arm.down()
    arm.up()
    nav.returnToStart(M07)
