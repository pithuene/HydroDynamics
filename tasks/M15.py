#Feuer - verschoben

import nav, arm
import color

#M15 = [[0, 0], [12, 0], [12, -0.3], [0.3, -6]]


def main():
    driveToFireTruck()

def driveToFireTruck():
    arm.close()
    arm.up()
    nav.driveDistance(100, 300)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    nav.turn(90)
    nav.driveDistance(8, 300)
    nav.turn(-90)
    nav.driveDistance(30, 300)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    nav.turn(-45)
    nav.driveDistance(25, 300)
    nav.turn(-80)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    nav.driveDistance(-5, 300)
    arm.open()
    arm.down()
    arm.close()
    arm.up()
    nav.driveDistance(-20, 300)