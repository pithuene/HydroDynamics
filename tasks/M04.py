import nav, arm
#rain - fertig // testen

import color

M04 = [[0, 0], [2.8, 0], [2.8, 6.3], [5.6, 6.3]]  # x und y Koordinaten


def main():
    arm.up()
    nav.followCoordinatePath(M04)
    nav.turn(20)
    nav.driveForward(50, -100)
    nav.turn(-20)
    nav.returnToStart(M04)