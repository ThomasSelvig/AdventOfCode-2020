import os
from pathlib import Path


assert "day3.txt" in os.listdir(str(Path(__file__).absolute().parent)), \
	"Paste puzzle input in 'day3.txt'"


with open(f"{str(Path(__file__).absolute().parent)}/day3.txt") as f:
	sledmap = [i.strip() for i in f.readlines() if i.strip()]


def drive_sled(right, down):
	x = 0
	crash_count = 0
	for line in sledmap[::down]:
		if line[x % len(line)] == "#":
			crash_count += 1
		x += right
	
	return crash_count


print("First:", drive_sled(3, 1))

combos = [
	(1, 1),
	(3, 1),
	(5, 1),
	(7, 1),
	(1, 2)
]

ans = 1
for crash_sum in [drive_sled(r, d) for r, d in combos]:
	ans *= crash_sum
print("Second:", ans)