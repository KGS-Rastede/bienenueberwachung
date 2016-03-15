#----------------Importierung nuetzlicher Variablen und Libraries--------------
#!/usr/bin/python
import os
import RPi.GPIO as GPIO
import time
import subprocess
#Waehlen des GPIO-Pin Layouts (GPIO.BOARD oder GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
#Setup des/der zu benutzenden Pins
GPIO.setup(18,GPIO.IN)

#Derzeitiger Status des Pins (nuetzlich, um Warten bei Fehlern vorzubeugen)
print GPIO.input(18)
#While-Schleife zum Pruefen, ob Stromkreis geschlossen ist
while True:
	#wenn Stromkreis offen
	if (GPIO.input(18) == 0):
		#gib 'Unterbrochen' aus
		print('Unterbrochen')
		#gib Datum und Zeit an
		os.system('date')
		#gib Status von Pin 18 an, um zu verdeutlichen, dass Stromkreis offen ist
		print GPIO.input(18)
		#warte 5 Sekunden
		time.sleep(5)
		#starte Skript zum Senden der Benachrichtigung 
		status = subprocess.call("python" + " /home/bienenpi/alarm.py", shell=True)

#-----------------------------------------------------------------------------
