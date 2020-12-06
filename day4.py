import re


with open("day4.txt") as f:
	passports = [i.strip() for i in f.read().split("\n\n")]


# hgt_criteria : non python3.8 solution since i solved this on my chromebook lol
# def hgt_criteria(hgt):
# 	r = re.match(r"(\d+)(cm|in)", hgt)
# 	if r:
# 		val, unit = r.groups()
# 		val = int(val)
# 		return val >= 150 and val <= 193 if unit == "cm" else \
# 			val >= 59 and val <= 76


criteria = {
	"byr": lambda byr: len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002,
	"iyr": lambda iyr: len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020,
	"eyr": lambda eyr: len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030,
	"hgt": lambda hgt: bool(r := re.match(r"(\d+)(cm|in)", hgt)) and \
		(val := int(r.groups()[0])) >= 150 and val <= 193 if r.groups()[1] == "cm" else \
		(val := int(r.groups()[0])) >= 59 and val <= 76,
	"hcl": lambda hcl: bool(re.match(r"#[a-f0-9]{6}", hcl)),
	"ecl": lambda ecl: bool(re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", ecl)),
	"pid": lambda pid: bool(re.match(r"^\d{9}$", pid))
}


def valid(passport):
	if all([field in passport for field in criteria.keys()]):
		for k, v in [i.split(":") for i in passport.split()]:
			if k != "cid":
				#print(k, criteria[k](v))
				if not criteria[k](v):
					break
		else:
			return True

print(len([pp for pp in passports if valid(pp)]))