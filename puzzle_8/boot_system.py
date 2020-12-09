from copy import deepcopy

def parse_sequence(boot_list):
	'''
		This function just parses the sequence of commands into a list of lists
	'''
	seq_list = [cmd.split(sep=' ') for cmd in boot_list]
	return seq_list

def run_sequence(seq_list_orig, acc):
	'''
		This function runs the boot sequence and returns list of commands ran
		and whether the boot was successful or not.
	'''
	i = 0
	boot = False
	seq_list = deepcopy(seq_list_orig)
	# Run through list, overwrite X for commands ran, exits if infinite loop
	while i <= len(seq_list):
		if seq_list[i][1] == 'X':
			break
		elif seq_list[i][0] == 'jmp':
			jmp = int(seq_list[i][1])
			seq_list[i][1] = 'X'
			i += jmp
		elif seq_list[i][0] == 'acc':
			acc += int(seq_list[i][1])
			seq_list[i][1] = 'X'
			i += 1
		else:
			seq_list[i][1] = 'X'
			i += 1

		# Boot sequence ends when iteration outside of commands list
		if i >= len(seq_list):
			boot = True
			break

	return acc, boot, seq_list, seq_list_orig

def fix_sequence(seq_list_orig, acc):
	'''
		This function runs the boot sequence and modifies flips jmp to nop and
		vice-versa command by command until the boot sequence returns true
	'''
	boot = False
	seq_list = deepcopy(seq_list_orig)
	# Flip jmp and nop commands until boot returns true
	for cmd in seq_list:
		if cmd[0] == 'jmp':
			cmd[0] = 'nop'
			acc, boot, _, _ = run_sequence(seq_list, acc=0)
			if boot:
				break
			else:
				cmd[0] = 'jmp'
		elif cmd[0] == 'nop':
			cmd[0] = 'jmp'
			acc, boot, _, _ = run_sequence(seq_list, acc=0)
			if boot:
				break
			else:
				cmd[0] = 'nop'

	return acc, boot, seq_list

if __name__ == '__main__':
	# Open File
	with open('./boot_sequence') as file:
		file_boot = file.readlines()
		boot_list = [line.strip() for line in file_boot]

		seq_list_orig = parse_sequence(boot_list)
		acc, boot, seq_list_ran, seq_list_orig = run_sequence(seq_list_orig, 0)

		print("Part 1 Acc:", acc)

		acc, boot, seq_list_booted = fix_sequence(seq_list_orig, acc=0)

		print("Part 2 Acc:", acc)
		print("Part 2 Boot:", boot)