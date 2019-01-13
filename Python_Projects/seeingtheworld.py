

first10 = list(range(1, 11))

for value in first10:
	print(value**3)
cubes = [value**3 for value in range(1, 101)]
print(cubes)
