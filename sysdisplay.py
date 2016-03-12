#!/usr/bin/python
# Example using a character LCD plate.


# Module imports
import time
import Adafruit_CharLCD as LCD
import time
import subprocess	

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()


def getCpuTemp():
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            readableTemp = float(f.read())/1000.
            return repr(readableTemp) + 'C'


def getCpuGov():
	with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq') as f:
	    speed = int(f.read())/1000
	    return repr(speed) + 'MHz'


def getIPAddress(ifname):
	ipAddrOut = subprocess.getoutput('ip addr show dev ' + ifname + ' | grep inet | awk \'NR=1{printf $2; exit}\'')
	return ipAddrOut


# Begin Program Logic
lcd.clear()
lcd.message('Morgoth is\nalive!!')
time.sleep(5)
lcd.clear()

while 1:
	h = 0
	i = 0
	
	# Display IP Addresses
	while h < 7:
		lcd.message(" eth0: " + getIPAddress('eth0') + "\n" + " wlan0: " + getIPAddress('wlan0'))
		lcd.move_left()
		time.sleep(1)
		h += 1
	time.sleep(2)
	lcd.clear()
	
	# Display CPU Temp and CPU gov setting 
	while i < 3:
		lcd.autoscroll(lcd.message(" CPU Temp: " + getCpuTemp() + "\n" + " CPU Gov: " + getCpuGov()))
		lcd.move_left()
		time.sleep(1)
		i += 1
	time.sleep(2)
	lcd.clear()
