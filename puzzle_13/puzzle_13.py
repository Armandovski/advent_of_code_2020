import numpy as np

def ft_part1(buses, arrival_time):
	'''
	This function finds the bus which will arrive first after time given in
	first line of data input
	'''
	best_arrival = {}
	for bus in buses:
		first_instance = np.ceil(arrival_time/bus)*bus
		best_arrival[bus] = first_instance

	best_bus = min(best_arrival, key=best_arrival.get)
	ans = best_bus*(best_arrival[best_bus] - arrival_time)
	return ans

def in_sequence(buses):
	for i in range(1, len(buses)):
		if buses[i] != buses[i - 1]:
			return False
	return True


def ft_part2(buses_all):
	'''
	This function finds the time t in which all buses will arrive at t + n where
	n is the value of their index in the order of the data input
	'''
	offset = []
	period = []
	for i, bus in enumerate(buses_all):
		if bus != 'x':
			offset.append(-i)
			period.append(int(bus))
	while not in_sequence(offset):
		min_idx = np.argmin(offset)
		max_idx = np.argmax(offset)
		orbit = np.ceil((offset[max_idx] - offset[min_idx]) / period[min_idx])
		offset[min_idx] += int(orbit * period[min_idx])
		if offset[min_idx] == offset[max_idx]:
			period[max_idx] = np.lcm(period[min_idx], period[max_idx])
			del period[min_idx]
			del offset[min_idx]
	return offset[0]


if __name__ == '__main__':
	# Open File
	with open('./input') as file:
		raw = file.readlines()
		data = [line.strip() for line in raw]

	arrival_time = int(data[0])
	buses_all = data[1].split(sep=',')
	buses = [int(bus) for bus in buses_all if bus != 'x']

	res_p1 = ft_part1(buses, arrival_time)
	print("Part 1:", res_p1)
	res_p2 = ft_part2(buses_all)
	print("Part 2:", res_p2)