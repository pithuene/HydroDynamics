import nav
import arm

M07 = [[0, 0], [7.9, 0], [7.9, -0.5]]  # x und y Koordinaten


def main():
    arm.open()
    arm.down()
    arm.close()
    arm.up()
    nav.followCoordinatePath(M07)
    arm.open()
    nav.returnToStart(M07)
