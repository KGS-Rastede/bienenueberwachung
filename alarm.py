#Letzte Aenderungen: Login-Daten in CSV-Datei und Timerfunktion
#Todo: GPIO-Pins,	Stromkreis unterbrochen = Benachrichtigung
#			Stromkreis wiederhergestellt = Timer unterbrochen

#Importierung der Simple Mail Transfer Protocol (SMTP), CSV Libaries und Time/Sleep Funktion
#!/usr/bin/python
from time import sleep
import smtplib
import csv
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)
#--------------------------Deklarierung einiger nuetzlicherVariablen-------------------------
	#Einbindung der Login-CSV-Datei, Pfad kann geaendert werden
with open('/home/bienenpi/login.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		User = row[0]
		Pass = row[1]

	#Variable zur Abkuerzung von 'smtplib.SMTP('smtp.gmail.com',587)' zu 'server'
server = smtplib.SMTP('smtp.gmail.com',587)

	#Die Variable 'empfaenger' ist das Ziel der Benachrichtigungsmail
empfaenger = 'steffenistcool@gmail.com'

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
