def get_layer_out(rules_dict, color):
	valid_keys = []

	for rule in rules_dict:
		if rules_dict[rule].find(color) > 0:
			valid_keys.append(rule)
			valid_keys = list(set(valid_keys))

	for key in valid_keys:
		valid_keys += get_layer(rules_dict, key)
		valid_keys = list(set(valid_keys))

	return valid_keys

def get_layer_in(rules_dict, color, cached_count):
	#valid_key = [rule for rule in rules_dict if rule == color]
	bag_count = 1
	colors = rules_dict[color]

	for clr in colors:
		#print(colors)
		#print(clr)
		#for bag in rules_dict[color]:
		#for bag in clr:
		#print(rules_dict[color])
		bag_flag = clr.split(' ', 1)[0]
		if bag_flag.isdigit():
			bag_num = clr.split(' ', 1)[0]
			bag_num = int(bag_num)
			bag_color = clr.split(' ', 1)[1]
			bag_count += bag_num * get_layer_in(rules_dict, bag_color, bag_count)
	print(bag_count)
	return bag_count


if __name__ == '__main__':
	# Open File
	with open('./bag_rules') as file:
		file_rules = file.readlines()
		rules_list = [line.strip() for line in file_rules]


	# Storing rules in dictionary
	rules_dict = {}
	for line in rules_list:
		key, value = line.split(' bags contain ')
		rules_dict[key] = value
		rules_dict[key] = rules_dict[key].replace(' bags, ', ',')
		rules_dict[key] = rules_dict[key].replace(' bags.', '')
		rules_dict[key] = rules_dict[key].replace(' bag, ', ',')
		rules_dict[key] = rules_dict[key].replace(' bag', '')
		rules_dict[key] = rules_dict[key].replace('.', '')
		rules_dict[key] = rules_dict[key].split(',')

	valid_keys_out = get_layer_out(rules_dict, 'shiny gold')
	print("Solution to Part 1:", len(valid_keys_out))

	cached_count = 0
	counter = get_layer_in(rules_dict, 'shiny gold', cached_count)-1
	print("Solution to Part 2:", counter)