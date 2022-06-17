# We are going to calculate the surface area of a cube based on the length of its edge:

# Input the length of an edge of a cube
cubeLengthString = input("What is the length of an edge of a cube? ")
cubeLength = int(cubeLengthString)

# Compute the surface area of the cube using the formula:
# Surface area = 6 * (edge squared)	(e2)
surfaceArea = 6 * (cubeLength ** 2)

# Print the surface area
print("The surface area of the cube is " + str(surfaceArea) + ".")
