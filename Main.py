import sys
from rubik_solver import utils
import serial
# Scramble: D' B2 L U' B L' D R' D' B2 U2 F' R2 L2 B' L2 B U2 L2 #green on front; white on top
# cube = 'oyrryorwwyyybbrywoboogrogwrggbygygrowbbgoobwrybwgwbgrw' #solve with red on front; yellow on top

# Scramble: R' B' U' B U' B2 L' B' U' B2 U2 F2 L2 U2 D' R2 L2 B2 L2 R' #green on front; white on top
# cube = 'gboyygygrygowbywbybwwrroryggrwwgyrowbrooorbwobbyowggbr' #solve with red on front; yellow on top

# Scramble: F2 L2 F2 D U2 L2 B2 D' B2 F2 U2 F' R' B2 F L' U' F2 U2 R' #green on front; white on top
# cube = 'rwbyybbwrggoybboyywobwrroogworyggrrgygwrooorbggybwbyww' #solve with red on front; yellow on top

cube = 'ryobybrgygwbgbrgbowwggrybowoybrgwgrryowroobgywwoowbryy' #solve with red on front; yellow on top
w = y = b = g = r = o = 0
for i in cube:
	if i == "w":
		w += 1
	if i == "y":
		y += 1
	if i == "b":
		b += 1
	if i == "g":
		g += 1
	if i == "r":
		r += 1
	if i == "o":
		o += 1
print("white: ", w)
print("yellow: ", y)
print("blue: ", b)
print("green: ", g)
print("red: ", r)
print("orange: ", o)

solve = utils.solve(cube, 'Kociemba')
print(solve, "size:", len(solve))


# you need to give the arduino side of things to properly initialize from prior experience, can't be sure of this until we test the theory
# t = 0;
# while t < 1000:
# 	t += 1

# arduinoData = serial.Serial('com3', 9600) # this could be either or, will have to see which one is the right one during testing
# arduinoData = serial.Serial('COM3', 9600)
# for i in solve: # this will be used to feed the data to the arduino side of things to intitiate movements on the different servos
# 	arduinoData.write(i)
