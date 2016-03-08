#Letzte Änderungen: Login-Daten in CSV-Datei und Timerfunktion
#Todo: GPIO-Pins,	Stromkreis unterbrochen = Benachrichtigung
#			Stromkreis wiederhergestellt = Timer unterbrochen

#Importierung der Simple Mail Transfer Protocol Libary (SMTP)
from time import sleep
import smtplib
import csv
#--------------------------Deklarierung einiger nützlicher Variablen-------------------------
	#Einbindung der Login-CSV-Datei, Pfad kann geändert werden
with open('/mnt/Steffweiterung/Schule/Seminarfach/Facharbeit/bienenueberwachung/login.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		User = row[0]
		Pass = row[1]

	#Variable zur Abkürzung von 'smtplib.SMTP('smtp.gmail.com',587)' zu 'server'
server = smtplib.SMTP('smtp.gmail.com',587)

	#Die Variable 'empfaenger' ist das Ziel der Benachrichtigungsmail
empfaenger = 'steffenistcool@gmail.com'

#--------------------------------------------------------------------------------------------


#----------------------Formatierung und Senden der Benachrichtigungsmail---------------------
	#Emailformatierung: Betreff, header und body der Mail (bisher nur Platzhalter)
subject = 'Bienenstockalarm'
header = 'To: ' + empfaenger + '\n' + 'From: ' + User + '\n' +'Subject: ' + subject
body = 'Anscheinend ist etwas los, beim Bienenstock.'

for Timer in range(0,60):
	print(60 - Timer)
	sleep(1)

	#Handshake mit dem Googlemail-Server
server.ehlo()
	#Herstellung einer Verschlüsselung zur sicheren Datenübertragung
server.starttls()
	
	#Authentifizierung des Mailaccounts
server.login(User, Pass)
	#Senden der Mail
server.sendmail(User, empfaenger, header + '\n\n'+ body)

#beendet die Verbindung zum Googlemail-Server
server.quit()

#-------------------------------------------------------------------------------------------
