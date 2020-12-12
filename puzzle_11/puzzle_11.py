import numpy as np

ROW = 0
COL = 1

def find_adjacent(grid, coord):
	g_lenx = len(grid)
	g_leny = len(grid[0])
	adj = [[-1, -1], [1, 1], [-1, 1], [1, -1], [-1, 0], [1, 0], [0, -1], [0, 1]]
	for a in adj:
		a[ROW] += coord[ROW]
		a[COL] += coord[COL]
	adjacent = [tuple(a) for a in adj if 0 <= a[ROW] < g_lenx and 0 <= a[COL] < g_leny]
	adjacent = [adj for adj in adjacent if grid[adj] != '.']

	return adjacent


def game_of_chairs(seat_cache):
	to_hash = []
	for empty in seat_cache['L']:
		adjacents = find_adjacent(grid, empty)
		vol_seats = [adj for adj in adjacents if adj not in (seat_cache['#_P'] + seat_cache['L_P'])]
		if len(vol_seats) < 4:
			to_hash.append(empty)
			grid[empty] = '#'
	[seat_cache['#_P'].append(item) for item in to_hash]
	[seat_cache['L'].remove(item) for item in to_hash]

	to_L = []
	for empty in seat_cache['L']:
		adjacents = find_adjacent(grid, empty)
		perm_occ_seats = [adj for adj in adjacents if adj in (seat_cache['#_P'])]
		if len(perm_occ_seats) >= 1:
			to_L.append(empty)
			grid[empty] = 'o'
	[seat_cache['L_P'].append(item) for item in to_L]
	[seat_cache['L'].remove(item) for item in to_L]

	return seat_cache


def ft_part1(grid):
	seat_cache = {'#': [], 'L': [], '#_P': [], 'L_P': []}
	for ide, elem in np.ndenumerate(grid):
		if (elem == 'L'):
			seat_cache['L'].append((ide[0], ide[1]))
		elif(elem == '#'):
			seat_cache['L'].append((ide[0], ide[1]))

	while seat_cache['L']:
		seat_cache = game_of_chairs(seat_cache)

	seats_occupied = len(seat_cache['#_P'])
	return seats_occupied

'''
def ft_part2(data):
	return
'''

if __name__ == '__main__':
	# Open File
	with open('./input') as file:
		raw = file.readlines()
		data = [line.strip() for line in raw]
		grid = [list(line) for line in data]

	grid = np.array([np.array(i) for i in grid])
	seats_occupied = ft_part1(grid)
	print("Part 1:", seats_occupied)
	#res_p2 = ft_part2(data)
	#print("Part 2:", res_p2)