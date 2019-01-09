import serial
port = serial.Serial('com4', 9600)
port.write(b"1");