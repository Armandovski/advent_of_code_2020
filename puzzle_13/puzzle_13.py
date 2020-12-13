import numpy as np

def ft_part1(buses, arrival_time):
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
	position = []
	period = []
	for i, bus in enumerate(buses_all):
		if bus != 'x':
			position.append(-i)
			period.append(int(bus))
	while not in_sequence(position):
		print(position)
		min_idx = np.argmin(position)
		max_idx = np.argmax(position)
		print(position[max_idx], position[min_idx], period[min_idx])
		orbit = np.ceil((position[max_idx] - position[min_idx]) / period[min_idx])
		position[min_idx] += int(orbit * period[min_idx])
		if position[min_idx] == position[max_idx]:
			period[max_idx] = np.lcm(period[min_idx], period[max_idx])
			del period[min_idx]
			del position[min_idx]
	print(position)
	return position


if __name__ == '__main__':
	# Open File
	with open('./test') as file:
		raw = file.readlines()
		data = [line.strip() for line in raw]

	arrival_time = int(data[0])
	buses_all = data[1].split(sep=',')
	buses = [int(bus) for bus in buses_all if bus != 'x']

	res_p1 = ft_part1(buses, arrival_time)
	print("Part 1:", res_p1)
	res_p2 = ft_part2(buses_all)
	#print("Part 2:", res_p2)