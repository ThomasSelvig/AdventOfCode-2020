from itertools import combinations


with open("day9.txt") as f:
	data = [int(i) for i in f.read().split()]


def challenge1():
	for i, n in enumerate(data[25:]):
		if not n in [sum(c) for c in combinations(data[i:i+25], r=2)]:
			return n


def challenge2(n):
	for i in range(len(data)):
		for remaining_number_scanner in range(i+1, len(data) + i+1):
			combo = data[i:remaining_number_scanner]
			if len(combo) > 1 and sum(combo) == n:
				return sum((min(combo), max(combo)))


n = challenge1()
print("Challenge 1:", n)
assert n

print("Challenge 2:", challenge2(n))