import pandas as pd

file = open('./input')
input = file.read()

# Word limit
input_list = list(input.split(sep="\n"))

pwds = []
for elem in input_list:
	elem = elem.replace(': ', ':')
	elem = elem.replace('-', ':')
	elem = elem.replace(' ', ':')
	elem = elem.split(':')
	pwds.append(elem)
	#param.append(elem.split(sep=':'))

print(pwds)
pwds_count = 0

for elem in pwds:
	if (int(elem[0]) <= elem[3].count(elem[2]) <= int(elem[1])):
		pwds_count += 1

#print(pwds_count)

# Part 2
pwds_count2 = 0
i = 0

for elem in pwds:
	i += 1
	elem[0] = int(elem[0])
	elem[1] = int(elem[1])
	cond1 = False
	cond2 = False
	if (elem[0] <= 0) or (elem[0] > len(elem[3])):
		cond1 = True
	if (elem[1] <= 0) or (elem[1] > len(elem[3])):
		cond2 = True

	if cond1:
		if elem[3][elem[1]-1] == elem[1]:
			pwds_count2 += 1
	elif cond2:
		if elem[3][elem[0]-1] == elem[0]:
			pwds_count2 += 1
	else:
		if (elem[3][elem[1]-1] == elem[2]) and (elem[3][elem[0]-1] == elem[2]):
			pass
		elif ((elem[3][elem[1]-1] != elem[2]) and (elem[3][elem[0]-1] != elem[2])):
			pass
		elif ((elem[3][elem[1]-1] == elem[2]) and (elem[3][elem[0]-1] != elem[2])):
			pwds_count2 += 1
		elif ((elem[3][elem[1]-1] != elem[2]) and (elem[3][elem[0]-1] == elem[2])):
			pwds_count2 += 1

print(pwds_count2)


