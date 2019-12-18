import time

'''
    Es werden fünf (default) oder x Werte mit dem Ultraschallsensor gemessen und der Durchschnitt davon zurückgegeben
'''

def preciseDistance(ultrasonic, tries=5):
    sum = 0
    for i in range(0, tries):
        sum += ultrasonic.distance()
        time.sleep(0.03)
    return sum / tries
