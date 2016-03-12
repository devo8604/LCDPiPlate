LCDPiPlate

"Pi Plate: Serving you delicious information, the Raspberry Pi way"
GitHub Web Page: http://devo8604.github.io/LCDPiPlate

My implementation of displaying information on Adafruit Pi Hat
Uses Adafruit's CharLCD Library: https://github.com/adafruit/Adafruit_Python_CharLCD

Adafruit's CharLCD library is completely unmodified and is only used here as a matter of installation convenience.

TODO
- Add installation Script
- Add Safe shutdown when service stops
- Add menu
- Code Cleanup!

Setup
- sudo cp piPlate.service /etc/systemd/system/
- sudo systemctl enable piPlate.service
- sudo systemctl start piPlate.service
