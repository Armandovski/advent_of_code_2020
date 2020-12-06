file = open('./map')
passports_file = file.read()

map_list = list(passports_file.split(sep="\n\n"))
print(map_list)
map_list_orig = map_list

"""
x = 0
y = 0
i = 0
tree_count = 0
#print(len(map_list[y]))

for y in range(len(map_list)):
	i += 1
	#print('iteration:', i)
	#print("x =", x)
	#print("y = ", y)
	if map_list[y][x] == '#':
		tree_count += 1
	x += 3
	y += 1

	if x >= len(map_list[y-1]):
		x = x - len(map_list[y-1])
"""

def tree_count(map_list, x_slope, y_slope):
	tree_count = 0
	x = 0
	for y in range(0, len(map_list), y_slope):
		if map_list[y][x] == '#':
			tree_count += 1
		x += x_slope

		if x >= len(map_list[y-1]):
			x = x - len(map_list[y-1])

	return tree_count

if __name__ ==  '__main__':
	print("Right 1, Down 1:", tree_count(map_list, 1, 1))
	print("Right 3, Down 1:", tree_count(map_list, 3, 1))
	print("Right 5, Down 1:", tree_count(map_list, 5, 1))
	print("Right 7, Down 1:", tree_count(map_list, 7, 1))
	print("Right 1, Down 2:", tree_count(map_list, 1, 2))

	prod = tree_count(map_list, 1, 1) * tree_count(map_list, 3, 1) * \
		tree_count(map_list, 5, 1) * tree_count(map_list, 7, 1) * \
		tree_count(map_list, 1, 2)

	print(prod)
