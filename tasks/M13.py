#flowser - verschoben

import nav, arm
import color

M07 = [[0, 0], [18.5, 0], [18.5,3], [2.4,3]]  # x und y Koordinaten
half = [[0, 0], [15, 0], [15,-0.8], [15.1,-0.8]]  # x und y Koordinaten
secoundHalf = [[15.8, -0.8]]
toThePlant = [[15.8,1],[14,1]]


def main():
    '''arm.open()
    arm.down()
    arm.close()'''
    arm.up()
    nav.followCoordinatePath(half)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    nav.followCoordinatePath(secoundHalf)
    nav.turn(-50)
    nav.driveForward(500, 100)
    nav.turn(-50)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    #nav.followCoordinatePath(toThePlant)
    nav.driveForward(-50, 100)
    nav.turn(-50)
    nav.driveForward(200, 100)
    arm.down()
    arm.open()
    arm.up()
    arm.close()
    arm.down()
    arm.up()
    nav.returnToStart(M07)
