from pyperclip import copy, paste
from itertools import product
from math import prod  # requires python 3.8


# parse input from clipboard
nums = [int(i) for i in paste().strip().split("\r\n")]


def challenge(n):
	""" n = challenge number """
	for ls in product(nums, repeat=n+1):
		if sum(ls) == 2020:
			return prod(ls)


print(f"First: {challenge(1)} \nSecond: {challenge(2)}")
