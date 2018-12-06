# Scramble: D' B2 L U' B L' D R' D' B2 U2 F' R2 L2 B' L2 B U2 L2 #green on front; white on top
cube = 'oyrryorwwyyybbrywoboogrogwrggbygygrowbbgoobwrybwgwbgrw' #solve with red on front; yellow on top
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


from rubik_solver import utils
print(utils.solve(cube, 'Kociemba'))
