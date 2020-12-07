def get_unique_sum(group_answers_list):
	# Part 1 - Get unique sum
	# Get all answers for each group
	group_all_answers = [answers.replace('\n', '') for answers in group_answers_list]
	group_answer_sets = [set(answers) for answers in group_all_answers]
	# Sum all unique answers
	sum_unique = 0
	for group in group_answer_sets:
		sum_unique += len(group)
	return sum_unique

def get_common_sum(answers_list):
	# Part 2 - Get common sum
	total_count = 0
	for group in answers_list:
		answers = ''.join(group)
		for answer in set(answers):
			if answers.count(answer) == len(group):
				total_count += 1
	return total_count


if __name__ == '__main__':
	# Open File
	with open('./customs_answers') as file:
		file_answers = file.read()
	# Make List of groups
	group_answers_list = file_answers.split('\n\n')
	# Separate answers for each group
	answers_list = [answers.split('\n') for answers in group_answers_list]

	print(get_unique_sum(group_answers_list))
	print(get_common_sum(answers_list))



