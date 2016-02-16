#todo: kleiner Feinheiten und Extras

#Importierung der Simple Mail Transfer Protocol Libary (SMTP)
import smtplib
#--------------------------Deklarierung einiger nützlicher Variablen-------------------------

	#Variable zur Abkürzung von 'mtplib.SMTP('smtp.gmail.com',587)' zu 'server'
server = smtplib.SMTP('smtp.gmail.com',587)

	#Login-Daten des Alarmaccounts
User = 'bienenstockalarm@gmail.com'
Pass = 'DisDerBienenstockalarm0815!'

	#Die Variable 'empfaenger' ist das Ziel der Benachrichtigungsmail
empfaenger = 'steffenistcool@gmail.com'

#--------------------------------------------------------------------------------------------


#----------------------Formatierung und Senden der Benachrichtigungsmail---------------------
	#Emailformatierung: Betreff, header und body der Mail (bisher nur Platzhalter)
subject = 'Bienenstockalarm'
header = 'To: ' + empfaenger + '\n' + 'From: ' + User + '\n' +'Subject: ' + subject
body = 'Anscheinend ist etwas los, beim Bienenstock.'

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

#--------------------------------------------------------------------------------------------
