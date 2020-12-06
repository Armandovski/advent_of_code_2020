def find_seatBI(seat):
	# 'F' = 0 and 'B' = 1
	# Find Row
	loc = 0
	i = len(seat)-1
	for pos in seat:
		if pos == 'B' or pos == 'R':
			loc += 2 ** i
		i -= 1

	return loc

"""
def find_seat(seat):
	rows = list(range(0, 128))
	columns = list(range(0,8))

	# Find Row
	for pos in seat[:7]:
		if pos == 'F':
			del rows[len(rows)//2:]
		elif pos == 'B':
			del rows[:len(rows)//2]
	print(rows)
	row = rows[0]

	# Find Column
	for pos in seat[7:]:
		if pos == 'L':
			del columns[len(columns)//2:]
		elif pos == 'R':
			del columns[:len(columns)//2]
	print(columns)
	column = columns[0]

	return row, column
"""

if __name__ == '__main__':
	# Open File
	with open('./boarding_pass') as file:
		file_bpass = file.read()
	# Make List
	bpass_list = file_bpass.split('\n')
	seatID = []

	for bpass in bpass_list:
		#row, column = find_seat(bpass)
		rowBI = find_seatBI(bpass[:7])
		columnBI = find_seatBI(bpass[7:])
		#seatID.append(row * 8 + column)
		seatID.append(rowBI * 8 + columnBI)

	#print(max(seatID))

	# Part 2 - Find my seat
	ocurrences = 0
	for seat in seatID:
		if (seat + 1) not in seatID:
			if (seat+2) in seatID:
				my_seatID = (seat + 1)
				ocurrences += 1

	print(my_seatID)
	print(ocurrences)





