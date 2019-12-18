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
  - **approachGrab()** - Mist den Abstand zum nächsten Objekt und fährt so lange vorwärts, bis das Objekt in reichweite ist. Danach wird grab() ausgeführt. 

  

- **Nav** (Navigation auf dem Spielfeld mit selbst ersteltem Koordinatensystem)

  - **followCoordinatePath()** - Array mit Koordinaten die abgefahren werden sollen

  - **returnToStart()** - Array mit Koordinaten wird Rückwärts abgefahren

  - **turn(angle, speed = 50)** - Drehung des Roboters 

    (Angle = Drehung der Reifen in Grad, speed = Geschwindigkeit (default 50))

  - **driveForward(angle, speed = 50)** -  Roboter fährt Vorwärts 
  
    (Angle = Drehung der Reifen in Grad, speed = Geschwindigkeit (default 50))
    
    
  
- **Color**
  
  - **readColor()** - liest die Reflektion der Farbwerte und gibt entweder schwarz, weiß oder bunt zurück
  - **driveToBlack()** - fährt zur nächsten schwarzen Linie
  - **turnMotorToBlack**() - richtet sich an gefundener schwarzer Linie aus 
  
- **Utils**

  - preciseDistance(ultrasonic, tries=5) - misst fünf Werte mit dem Ultraschallsensor und gibt den Durchschnitt davon wieder (Ultrasonic = Ultraschallsensor an der Seite oder vorne, tries = Anzahl der Messungen, die der Sensor machen soll)
  
- **Adnav** Erweiterung der Standard Navigation aus nav.py

  - **driveToPoint()** - fährt zu angegebenen Koordinaten

  - **getDistanceToWall()** - Entfernung zur Seite messen

  - **willCrossBlackLine()** - bestimmt ob eine schwarze Linie gekreuzt wird

  - **turn(angle, speed = 50)** - Drehung des Roboters 

    (Angle = Drehung der Reifen in Grad, speed = Geschwindigkeit (default 50))



## 3. Aufgaben

- M02 - Flow 
  - Befördert (max. einmal) eine große Wassermenge auf das Spielfeld des anderen Teams, indem ihr nur an dem/den Ventil(en) des Pumpsystems dreht. 
- M03 - Pump Addition
  - Bringt die Zusatzpumpe so ins Zielgebiet, dass sie nur innerhalb des Zielgebiets die Spielfeldmatte berührt.
- M04 - Rain
  - Lasst mindestens einen Regentropfen aus der Regenwolke regnen.
- M05 - Filter
  - Schiebt den Filter nach Norden, bis der Verriegelungshebel einrastet.
- M06 - Water Treatment
  - 
- M07 - Fountain
  - Platziert eine große Wassermenge in der grauen Wanne, sodass die Fontäne erkennbar angehoben wird und oben bleibt.
- M18 - Faucet
  - Dreht am gelben Wasserhahn und verändert den Wasserstand so, dass in der Tasse mehr blau als weiß zu sehen ist.