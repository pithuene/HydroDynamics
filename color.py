import time

from pybricks.parameters import (Port, Stop, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)

colorRight = ColorSensor(Port.S2)
colorLeft = ColorSensor(Port.S3)


def readColor(colorSensor):
    val = colorSensor.reflection()
    if val < 15:
        return 'black'
    elif val < 75:
        return 'color'
    else:
        return 'white'


def driveToBlack(db, motorWheelLeft, motorWheelRight):
    db.drive(30, 0)
    colHistL = []
    colHistR = []
    colL = ''
    colR = ''

    while True:
        colL = readColor(colorLeft)
        colR = readColor(colorRight)

        if (colL == 'black') & ('white' in colHistL):
            db.stop(Stop.HOLD)
            turnMotorToBlack(motorWheelRight, colorRight,
                             'white' not in colHistR and colR != 'white')
            turnMotorToBlack(motorWheelLeft, colorLeft, False)
            break
        elif (colR == 'black') & ('white' in colHistR):
            db.stop(Stop.HOLD)
            turnMotorToBlack(motorWheelLeft, colorLeft,
                             'white' not in colHistL and colL != 'white')
            turnMotorToBlack(motorWheelRight, colorRight, False)
            break
        # else:
            # print('Read black?: ' + str('black' in colHistR))
        colHistL.append(colL)
        colHistR.append(colR)
        if(len(colHistL) > 100):
            colHistL.pop(0)
            colHistR.pop(0)


def turnMotorToBlack(motor, colorSensor, mustHaveSeenWhite=True):
    motor.run(30)
    colHist = []
    col = ''
    while True:
        time.sleep(0.003)
        col = readColor(colorSensor)
        if (col == 'black') and (('white' in colHist) or not mustHaveSeenWhite):
            motor.stop(Stop.HOLD)
            break
        colHist.append(col)
        if len(colHist) > 100:
            colHist.pop(0)
