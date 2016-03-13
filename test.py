#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Ich denke, dass hier die Programmlogik falsch ist:
#
#>>> while True:
#...     try:
#...         x = int(input("Please enter a number: "))
#...         break
#...     except ValueError:
#...         print("Oops!  That was no valid number.  Try again...")
#...
try:
	while True:
		if (GPIO.input(11) == 1):
			print('Input, also alles ist gut')
			time.sleep(2)
		else:
			print:('kein Input also wird Mail gesendet')
			time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
