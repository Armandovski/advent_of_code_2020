import numpy as np

ROW = 0
COL = 1

def find_adjacent(grid, coord):
	'''
	This functions finds all adjacent points in the grid of a given coordinate
	'''
	g_lenx = len(grid)
	g_leny = len(grid[0])
	adj = [[-1, -1], [1, 1], [-1, 1], [1, -1], [-1, 0], [1, 0], [0, -1], [0, 1]]
	for a in adj:
		a[ROW] += coord[ROW]
		a[COL] += coord[COL]
	adjacent = [tuple(a) for a in adj if 0 <= a[ROW] < g_lenx and 0 <= a[COL] < g_leny]
	adjacent = [adj for adj in adjacent if grid[adj] != '.']

	return adjacent


def find_visible(grid, coord):
	'''
	This function finds all visible points (not floor) from a given coordinate
	'''
	multiplier = 1
	g_lenx = len(grid)
	g_leny = len(grid[0])
	adj_points = [[-1, -1], [1, 1], [-1, 1], [1, -1], [-1, 0], [1, 0], [0, -1], [0, 1]]
	adj_points_ref = [[-1, -1], [1, 1], [-1, 1], [1, -1], [-1, 0], [1, 0], [0, -1], [0, 1]]
	adjacent = []

	while adj_points:
		for rel_a in adj_points_ref:
			if rel_a not in adj_points:
				continue
			abs_a = []
			rel_a_search = [i * multiplier for i in rel_a]
			abs_a.append(rel_a_search[ROW] + coord[0])
			abs_a.append(rel_a_search[COL] + coord[1])
			if (0 <= abs_a[ROW] < g_lenx) and (0 <= abs_a[COL] < g_leny):
				if grid[tuple(abs_a)] != '.':
					adjacent.append(abs_a)
					adj_points.remove(rel_a)
			else:
				adj_points.remove(rel_a)
		multiplier += 1

	adjacent = [tuple(item) for item in adjacent]
	return adjacent


def game_of_chairs(seat_cache):
	'''
	This function iterates through the rules of part 1 until all chairs are settled
	'''
	to_hash = []
	count = 0
	for empty in seat_cache['L']:
		adjacents = find_adjacent(grid, empty)
		occ_seats = [adj for adj in adjacents if adj in (seat_cache['#'] + seat_cache['#_P'])]
		if len(occ_seats) == 0 :
			to_hash.append(empty)
			grid[empty] = '#'
			count += 1
	[seat_cache['#'].append(item) for item in to_hash]
	[seat_cache['L'].remove(item) for item in to_hash]

	to_L = []
	for empty in seat_cache['#']:
		adjacents = find_adjacent(grid, empty)
		occ_seats = [adj for adj in adjacents if adj in (seat_cache['#'] + seat_cache['#_P'])]
		if len(occ_seats) >= 4:
			to_L.append(empty)
			grid[empty] = 'L'
			count += 1
	[seat_cache['L'].append(item) for item in to_L]
	[seat_cache['#'].remove(item) for item in to_L]

	return seat_cache, count


def game_of_chairs2(seat_cache):
	'''
	This function iterates through the rules of part 2 until all chairs are settled
	'''
	to_hash = []
	count = 0
	for empty in seat_cache['L']:
		visibles = find_visible(grid, empty)
		occ_seats = [vis for vis in visibles if vis in (seat_cache['#'] + seat_cache['#_P'])]
		if len(occ_seats) == 0 :
			to_hash.append(empty)
			grid[empty] = '#'
			count += 1
	[seat_cache['#'].append(item) for item in to_hash]
	[seat_cache['L'].remove(item) for item in to_hash]

	to_L = []
	for empty in seat_cache['#']:
		visibles = find_visible(grid, empty)
		occ_seats = [vis for vis in visibles if vis in (seat_cache['#'] + seat_cache['#_P'])]
		if len(occ_seats) >= 5:
			to_L.append(empty)
			grid[empty] = 'L'
			count += 1
	[seat_cache['L'].append(item) for item in to_L]
	[seat_cache['#'].remove(item) for item in to_L]

	return seat_cache, count


def ft_part1(grid):
	'''
	This function resolves part 1
	'''
	seat_cache = {'#': [], 'L': [], '#_P': [], 'L_P': []}
	for ide, elem in np.ndenumerate(grid):
		if (elem == 'L'):
			seat_cache['L'].append((ide[0], ide[1]))
		elif(elem == '#'):
			seat_cache['L'].append((ide[0], ide[1]))

	count = 1
	while count != 0:
		seat_cache, count = game_of_chairs(seat_cache)
	seats_occupied = len(seat_cache['#'])
	return seats_occupied


def ft_part2(data):
	'''
	This function resolves part 2
	'''
	seat_cache = {'#': [], 'L': [], '#_P': [], 'L_P': []}
	for ide, elem in np.ndenumerate(grid):
		if (elem == 'L'):
			seat_cache['L'].append((ide[0], ide[1]))
		elif(elem == '#'):
			seat_cache['L'].append((ide[0], ide[1]))

	count = 1
	while count != 0:
		seat_cache, count = game_of_chairs2(seat_cache)
	seats_occupied = len(seat_cache['#'])
	return seats_occupied


if __name__ == '__main__':
	# Open File
	with open('./input') as file:
		raw = file.readlines()
		data = [line.strip() for line in raw]
		grid = [list(line) for line in data]

	grid = np.array([np.array(i) for i in grid])
	#seats_occupied = ft_part1(grid)
	#print("Part 1:", seats_occupied)
	seats_occupied = ft_part2(grid)
	print("Part 2:", seats_occupied)