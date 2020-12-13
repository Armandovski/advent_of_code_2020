import numpy as np
from copy import deepcopy

def ft_part1(data):
	'''
	This function returns the manhattan distance of the ship after navigating
	through the input instructions "data".
	'''
	pos = [0, 0]
	bearing = 0
	for dir in data:
		direction = dir[0]
		mov = int(dir[1:])
		if direction == 'N':
			pos[1] += mov
		if direction == 'S':
			pos[1] -= mov
		if direction == 'E':
			pos[0] += mov
		if direction == 'W':
			pos[0] -= mov
		if direction == 'R':
			bearing -= mov
		if direction == 'L':
			bearing += mov
		if direction == 'F':
			pos[0] += round(mov*np.cos(np.radians(bearing)))
			pos[1] += round(mov*np.sin(np.radians(bearing)))

	manhattan_dist = abs(pos[0]) + abs(pos[1])
	return manhattan_dist


def ft_part2(data):
	'''
	This function returns the manhattan distance of the ship after chasing the
	waypoint, which moves according to instructions in "data"
	'''
	wypt = [10, 1]
	pos_ship = [0, 0]
	for dir in data:
		direction = dir[0]
		mov = int(dir[1:])
		if direction == 'N':
			wypt[1] += mov
		if direction == 'S':
			wypt[1] -= mov
		if direction == 'E':
			wypt[0] += mov
		if direction == 'W':
			wypt[0] -= mov
		if direction == 'R':
			buffer = deepcopy(wypt)
			for _ in range(0, int(mov/90)):
				wypt[0] = buffer[1]
				wypt[1] = -buffer[0]
				buffer = deepcopy(wypt)
		if direction == 'L':
			buffer = deepcopy(wypt)
			for _ in range(0, int(mov/90)):
				wypt[0] = -buffer[1]
				wypt[1] = buffer[0]
				buffer = deepcopy(wypt)
		if direction == 'F':
			pos_ship[0] += wypt[0]*mov
			pos_ship[1] += wypt[1]*mov

	manhattan_dist = abs(pos_ship[0]) + abs(pos_ship[1])
	return manhattan_dist


if __name__ == '__main__':
	# Open File
	with open('./input') as file:
		raw = file.readlines()
		data = [line.strip() for line in raw]

	res_p1 = ft_part1(data)
	print("Part 1:", res_p1)
	res_p2 = ft_part2(data)
	print("Part 2:", res_p2)