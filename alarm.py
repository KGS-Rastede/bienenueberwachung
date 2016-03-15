#Importierung der Simple Mail Transfer Protocol (SMTP), CSV Libraries und Time/Sleep Funktion
#!/usr/bin/python
from time import sleep
import smtplib
import csv
import RPi.GPIO as GPIO
import subprocess

#Waehlen des GPIO-Pin Layouts (GPIO.BOARD oder GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
#definieren von GPIO-Pin 18 als Input-Pin
GPIO.setup(18, GPIO.IN)
#--------------------------Deklarierung einiger nuetzlicherVariablen-------------------------
	#Einbindung der daten-CSV-Datei, Pfad kann geaendert werden
with open('/home/bienenpi/daten.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for element in readCSV:
		#definieren der Variablen 'User' und 'Pass' als Element 1 und 2 der daten-CSV-Datei
		User = element[0]
		Pass = element[1]
		#Die Variable 'empfaenger' ist das Ziel der Benachrichtigungsmail
		empfaenger = element[2]

	#Variable zur Abkuerzung von 'smtplib.SMTP('smtp.gmail.com',587)' zu 'server'
server = smtplib.SMTP('smtp.gmail.com',587)

	

#--------------------------------------------------------------------------------------------


#----------------------Formatierung und Senden der Benachrichtigungsmail---------------------
	#Emailformatierung: Betreff, header und body der Mail (bisher nur Platzhalter)
subject = 'Bienenprobleme'
header = 'To: ' + empfaenger + '\n' + 'From: ' + User + '\n' +'Subject: ' + subject
body = 'Anscheinend sind die Bienenkaesten umgefallen.'
	#startet Timer fuer das Senden der Mail
for Timer in range(0,60):
	#Timer zaehlt jede Sekunde runter
	print(60 - Timer)
	sleep(1)
	#wenn Stromkreis geschlossen, starte Warten-Skript
	if (GPIO.input(18) == 1):
		print('Verbindung wiederhergestellt')
		status = subprocess.call("sudo python" + " /home/bienenpi/warten.py", shell=True)

	#Handshake mit dem Googlemail-Server
server.ehlo()
	#Herstellung einer Verschluesselung zur sicheren Datenuebertragung
server.starttls()
	#Authentifizierung des Mailaccounts
server.login(User, Pass)
	#Senden der Mail
server.sendmail(User, empfaenger, header + '\n\n'+ body)
	#beendet die Verbindung zum Googlemail-Server
server.quit()

	#startet das Warten-Skript, wenn Mail gesendet
status = subprocess.call("sudo python" + " /home/bienenpi/warten.py", shell=True)


#-------------------------------------------------------------------------------------------
