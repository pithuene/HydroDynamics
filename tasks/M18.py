#faucet - in arbeit

import nav, arm
import color

M18 = [[0, 0], [15, 0], [15,-0.8], [15.1,-0.8]]  # x und y Koordinaten



def main():

    arm.up()
    arm.close()
    nav.followCoordinatePath(M18)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    