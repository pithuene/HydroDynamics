# **Autotron - Team 1**

## 1. Projektaufgabe

Erreichen der First Lego League Hydro Dynamics Aufgaben M02 (Flow), M03 (Pump Addition), M04 (Rain), M05 (Filter), M06 (Water Treatment), M07 (Fountain), M13 (Flower), M15 (Fire) und M18 (Faucet) durch Programmierung in MicroPython. Diese Aufgaben haben wir ausgewählt, da sie ein eingeschränktes Fähigkeitsspektrum von schieben, greifen und drücken erfordern. Dadurch werden alle diese Aufgaben mit einem einzigen Roboter zu bewerkstelligen sein. 

## 2. Aufbau des Roboters

### 2.1 Roboter

Der Roboter verfügt über zwei angetriebene Räder und einen Greifarm, der mit einem Motor nach oben / unten bewegt werden kann, und mit einem anderen Motor zugreifen und loslassen kann. Somit werden zu bewegende Gegenstände über den Ultraschallsensor gehoben, damit dieser auch beim Tragen noch brauchbar ist. Darüberhinaus hat der Roboter noch zwei Farbsensoren, die zur Orientierung und Ausrichtung genutzt werden und zusätzlich noch einen weiteren Ultraschallsensor an der rechten Seite, der zum Messen des Abstandes zwischen Außenmauer und Roboter genutzt wird. 

### 2.2 Ports

- **Ausgabeports**
  - Port A - Motor links
  - Port B - Motor rechts
  - Port C - Arm hoch/runter
  - Port D - Arm auf/zu
- **Inputports**
  - Port S1 - Seite rechts Ultraschall
  - Port S2 - rechter Farbsensor
  - Port S3 - linke Farbsensor
  - Port S4 - Ultraschall vorne 

### 2.3 Python Module

- **Arm** (Greifarm steuern)

  - **up()** - Arm zum höchsten Punkt hochfahren
  - **down()** - Arm zum niedrigsten Punkt runterfahren
  - **close()** - Arm wird geschlossen, bis der Motor blockiert
  - **open()** - Arm wird geöffnet, bis der Motor blockiert
  - **grab()** - Der Arm fährt runter, öffnet, schließt und fährt wieder hoch

  

- **Nav** (Navigation auf dem Spielfeld mit selbst ersteltem Koordinatensystem)

  - **followCoordinatePath()** - Array mit Koordinaten die abgefahren werden sollen

  - **turn(angle, speed = 50)** - Drehung des Roboters 

    (Angle = Drehung der Reifen in Grad, speed = Geschwindigkeit (default 50))

  - **driveForward(angle, speed = 50)** -  Roboter fährt Vorwärts 

    (Angle = Drehung der Reifen in Grad, speed = Geschwindigkeit (default 50))
    
    
  
- **Utils**

  - Später
