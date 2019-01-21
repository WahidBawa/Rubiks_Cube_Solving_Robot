import time
import sys
from rubik_solver import utils # this is how we actually get the algorithm for solving the cube
import serial # this will be used so that the python interface can interact with the arduino interface

# these are just a bunch of scrambles and the cube states along side them
# Scramble: D' B2 L U' B L' D R' D' B2 U2 F' R2 L2 B' L2 B U2 L2 #green on front; white on top
# cube = 'oyrryorwwyyybbrywoboogrogwrggbygygrowbbgoobwrybwgwbgrw' #solve with red on front; yellow on top

# Scramble: R' B' U' B U' B2 L' B' U' B2 U2 F2 L2 U2 D' R2 L2 B2 L2 R' #green on front; white on top
# cube = 'gboyygygrygowbywbybwwrroryggrwwgyrowbrooorbwobbyowggbr' #solve with red on front; yellow on top

# Scramble: F2 L2 F2 D U2 L2 B2 D' B2 F2 U2 F' R' B2 F L' U' F2 U2 R' #green on front; white on top
cube = 'rwbyybbwrggoybboyywobwrroogworyggrrgygwrooorbggybwbyww' #solve with red on front; yellow on top
# this below is just to count the amount of tiles with the same colour to ensure that their is no human error involved
w = y = b = g = r = o = 0
sides = ["w", "y", "b", "g", "r", "o"]
sideNums = [0, 0, 0, 0, 0, 0]
for i in cube:
	sideNums[sides.index(i)] += 1

maxTiles = max(sideNums[sides.index("w")], sideNums[sides.index("y")], sideNums[sides.index("b")], sideNums[sides.index("g")], sideNums[sides.index("r")], sideNums[sides.index("o")])
# print("Max:", maxTiles)

port1 = "com4"
port2 = "com5"

if maxTiles == 9:
	solve = utils.solve(cube, 'Kociemba') # this gets a solve alg
	algo = [] # this creates an empty list
	for i in solve: #this will go through your solve
		tmp = str(i) # it converts the solve instance to a string
		if len(tmp) == 1: # this will add a space on single clockwise moves
			tmp += " "
		algo.append(tmp) # this will add the single move to the algo list
	print(solve, "size:", len(algo)) # this will print out the solve along with the actual size of the movements

	algo = ["R2", "L2", "U2", "D2", "F2", "B2"] # testing the actual servos on something that should always work
	print(algo, "size:", len(algo)) # this will print out the solve along with the actual size of the movements
	# you need to give the arduino side of things to properly initialize from prior experience, can't be sure of this until we test the theory
	
	try:
		arduinoData = serial.Serial(port1, 9600, timeout=5) # this could be either or, will have to see which one is the right one during testing
	except:
		print("Port 1 is using the wrong port")

	try:
		arduinoData = serial.Serial("port2", 9600, timeout=5) # this could be either or, will have to see which one is the right one during testing
	except:
		print("Port 2 is using the wrong port")

	my_str = str(len(algo))
	my_str_as_bytes = str.encode(my_str)
	arduinoData.write(my_str_as_bytes)


	time.sleep(2) # sleeps for two seconds giving the arduino enough time to initialize
	# arduinoData = serial.Serial('COM3', 9600)
	# counter = 0;
	while(True): # commenting this out for the time being to see if it will work
		for i in algo: # this will be used to feed the data to the arduino side of things to intitiate movements on the different servos
			my_str = i
			my_str_as_bytes = str.encode(my_str)
			arduinoData.write(my_str_as_bytes)
			readin = arduinoData.readline()
			print(readin)
else:
	print("Human Error, cube state was entered incorrectly")