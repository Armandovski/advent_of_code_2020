import json
import string

file = open('./passports')
file_passports = file.read()

if __name__ == '__main__':
	passports = list(file_passports.split(sep='\n\n'))
	passports_list = []

	for elem in passports:
		elem = elem.replace('\n', ' ')
		elem = "{\"" + elem + "\"}"
		elem = elem.replace(' ', '\", \"')
		elem = elem.replace(':', '\":\"')
		passports_list.append(json.loads(elem))

	valid_features = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	valid_count = 0
	valid_passports = []

	for passport in passports_list:
		if set(valid_features).issubset(set(passport.keys())):
			valid_count += 1
			valid_passports.append(passport)

	def check_year(yr, low_limit, high_limit, flag):
		if (len(yr) != 4):
			print(flag, "INVALID")
			return False
		elif not (low_limit <= int(yr) <= high_limit):
			print(flag, "INVALID")
			return False
		else:
			return True

	def check_hgt(hgt):
		if 'cm' in hgt:
			hgt = hgt.replace('cm', '')
			if 150 <= int(hgt) <= 193:
				return True
			else:
				print("hgt INVALID")
				return False
		elif 'in' in hgt:
			hgt = hgt.replace('in', '')
			if 59 <= int(hgt) <= 76:
				return True
			else:
				print("hgt INVALID")
				return False
		else:
			print("hgt INVALID")
			return False

	def check_hcl(hcl):
		if hcl.startswith('#'): #'#' in hcl:
			hcl = hcl.replace('#', '')
			if (len(hcl) == 6):# and all(ch in string.hexdigits for ch in hcl):
				return True
			else:
				print("hcl INVALID")
				return False
		else:
			print("hcl INVALID")
			return False

	def check_ecl(ecl):
		if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			return True
		else:
			print("ecl INVALID")
			return False

	def check_pid(pid):
		if (len(pid) == 9): #and (isinstance(int(passport['pid']), int)):
			return True
		else:
			print("pid INVALID")
			return False

	i = 0
	valid_count = 0
	for passport in valid_passports:
		byr_ok = check_year(passport['byr'], 1920, 2002, 'byr')
		iyr_ok = check_year(passport['iyr'], 2010, 2020, 'iyr')
		eyr_ok = check_year(passport['eyr'], 2020, 2030, 'eyr')
		hgt_ok = check_hgt(passport['hgt'])
		hcl_ok = check_hcl(passport['hcl'])
		ecl_ok = check_ecl(passport['ecl'])
		pid_ok = check_pid(passport['pid'])

		if byr_ok and iyr_ok and eyr_ok and hgt_ok and hcl_ok and ecl_ok and pid_ok:
			valid_count += 1
			#print("Passport", i, "is OK")
		else:
			print(passport)
			print("Passport", i, "INVALID\n")
		i += 1


print(valid_count)