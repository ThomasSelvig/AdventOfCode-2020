"""
challenge 1: sum(amount of unique flags in each group)
"""

from pyperclip import paste
groups = [i.strip().split() for i in paste().strip().split("\r\n\r\n")]


def unique_flags(group):
	return set("".join(group))


def all_yes_flags(group):
	flag_amount = {k: 0 for k in unique_flags(group)}
	for person in group:
		for flag in person:
			flag_amount[flag] += 1
	return len([flag for flag, amount in flag_amount.items() if amount == len(group)])


print("Challenge 1:", sum([len(unique_flags(i)) for i in groups]))
print("Challenge 2:", sum([all_yes_flags(i) for i in groups]))
