def find_combination_opt(data, nbr, cache):
	'''
	This is a recursive function to find all possible combinations of adapters.
	This function uses memorization to reduce computational load
	'''
	count = 0
	if nbr in cache:
		return cache[nbr]
	else:
		for j in range(1, 4):
			next_nbr = nbr + j
			if next_nbr == max(data):
				count += 1
				return count
			if next_nbr in data:
				count += find_combination_opt(data, next_nbr, cache)
				cache[nbr] = count
	return count

def adapter_step_count(data):
	'''
	This function counts the amount of 1-Jolt and 3-Jolt adapters
	'''
	count_1 = 0
	count_3 = 0
	for i in range(len(data)-1):
		diff = data[i+1] - data[i]
		if diff == 1:
			count_1 += 1
		elif diff == 3:
			count_3 += 1
	return count_1, count_3

if __name__ == '__main__':
	# Open File
	with open('./input.txt') as file:
		file_adapters = file.readlines()
		data = [int(line.strip()) for line in file_adapters]

	data = sorted([0] + data + [max(data) + 3])
	cache = {}

	count_1, count_3 = adapter_step_count(data)
	print("Part 1 - 1-Jolt Count:", count_1)
	print("Part 1 - 3-Jolt Count:", count_3)
	count = find_combination_opt(data, 0, cache)
	print("Part 2 - Number of adapter combinations:", count)
