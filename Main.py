from rubik_solver import utils
# Scramble: D' B2 L U' B L' D R' D' B2 U2 F' R2 L2 B' L2 B U2 L2 #green on front; white on top
# cube = 'oyrryorwwyyybbrywoboogrogwrggbygygrowbbgoobwrybwgwbgrw' #solve with red on front; yellow on top

# Scramble: R' B' U' B U' B2 L' B' U' B2 U2 F2 L2 U2 D' R2 L2 B2 L2 R' #green on front; white on top
# cube = 'gboyygygrygowbywbybwwrroryggrwwgyrowbrooorbwobbyowggbr' #solve with red on front; yellow on top

# Scramble: F2 L2 F2 D U2 L2 B2 D' B2 F2 U2 F' R' B2 F L' U' F2 U2 R' #green on front; white on top
# cube = 'rwbyybbwrggoybboyywobwrroogworyggrrgygwrooorbggybwbyww' #solve with red on front; yellow on top
cube = 'gwbbyowbwworybbgyybrbwryggoogrggowwyygrwobbyorrgowryro' #solve with red on front; yellow on top

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