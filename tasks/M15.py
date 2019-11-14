import nav, arm
import color

#M15 = [[0, 0], [12, 0], [12, -0.3], [0.3, -6]]


def main():
    driveToFireTruck()

def driveToFireTruck():
    arm.close()
    arm.up()
    nav.driveDistanceForward(100, 300)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    nav.turn(90)
    nav.driveDistanceForward(8, 300)
    nav.turn(-90)
    nav.driveDistanceForward(30, 300)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    nav.turn(-45)
    nav.driveDistanceForward(25, 300)
    nav.turn(-80)
    color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    nav.driveDistanceForward(-5, 300)
    arm.open()
    arm.down()
    arm.close()
    arm.up()
    nav.driveDistanceForward(-20, 300)