#Flow - fertig // testen

import time
import nav

M02 = [[0, 0], [0, 6.8]]  # x und y Koordinaten



def main():

    nav.followCoordinatePath(M02)
    time.sleep(1)
    nav.returnToStart(M02)