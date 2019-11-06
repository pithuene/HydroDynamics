import time


def preciseDistance(ultrasonic, tries=5):
    sum = 0
    for i in range(0, tries):
        sum += ultrasonic.distance()
        time.sleep(0.03)
    return sum / tries
