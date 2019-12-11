import nav
import arm
import color

M15 = [[0, 0], [12, 0], [12, -0.3], [0.3, -6]]


def main():
    driveToFireTruck()


def driveToFireTruck():
    arm.close()
    arm.up()
    # nav.driveDistance(-1500, 300)
    nav.followCoordinatePath(M15)
    # color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    # nav.turn(90)
    # nav.driveDistance(80, 300)
    # nav.turn(-90)
    # nav.driveDistance(300, 300)
    # color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    # nav.turn(-45)
    # nav.driveDistance(250, 300)
    # nav.turn(-80)
    # color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
    # nav.driveDistance(-50, 300)
    # arm.open()
    # arm.down()
    # arm.close()
    # arm.up()
    # nav.driveDistance(-200, 300)
