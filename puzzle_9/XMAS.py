def decode(entry, precede_list):
	'''
		This function checks a given number against preceding list. Returns
		True if 2 numbers of the preceding list add up to checked number, False
		if not.
	'''
	sum_check = False
	for i in range(len(precede_list)):
		for j in range(i+1, len(precede_list)):
			num_sum = precede_list[i] + precede_list[j]
			if num_sum == entry:
				sum_check = True
	return entry, sum_check

def check_XMAS_nums(XMAS_list, preamble_size):
	'''
		This function runs through the list until no 2 numbers of the preceding
		sequence add up to the number being checked. Returns number checked.
	'''
	i = 0
	sum_check = True
	while sum_check:
		entry = XMAS_list[preamble_size + i]
		precede_list = [num for num in XMAS_list[i : i + preamble_size]]
		entry, sum_check = decode(entry, precede_list)
		i += 1
	return entry, sum_check

def find_weakness(XMAS_list, entry):
	'''
		This function runs through the entire list and checks if any sequence of
		numbers at all (any length) add up to number being checked.
	'''
	for i in range(len(XMAS_list)):
		for j in range(i+1, len(XMAS_list)):
			sum_list = [num for num in XMAS_list[i : j]]
			if sum(sum_list) == entry:
				return min(sum_list) + max(sum_list)

if __name__ == '__main__':
	# Open File
	with open('./XMAS') as file:
		file_XMAS = file.readlines()
		XMAS_list = [line.strip() for line in file_XMAS]

	# Define preamble size
	preamble_size = 25

	# Run through XMAS list
	XMAS_list = [int(num) for num in XMAS_list]
	entry, sum_check = check_XMAS_nums(XMAS_list, preamble_size)
	print("Part 1:", entry, sum_check)
	weakness = find_weakness(XMAS_list, entry)
	print("Part 2:", weakness)
