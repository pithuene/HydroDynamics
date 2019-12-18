#punp addition - fertig // testen

import nav

M03 = [[0, 0], [2.8, 0], [2.8, 6.475]]  # x und y Koordinaten


def main():
    nav.followCoordinatePath(M03)
    nav.turn(-60)
    nav.driveForward(45, -100)
    nav.turn(45)
    nav.returnToStart(M03)