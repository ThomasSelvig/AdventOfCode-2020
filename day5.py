from pyperclip import paste
import re


def seat_id(bp):
	bp = re.sub(r"B|R", "1", re.sub(r"F|L", "0", bp))
	row, col = [int(i, 2) for i in (bp[:7], bp[7:])]
	return row * 8 + col


boarding_passes = paste().strip().split()
seat_ids = sorted(list(map(seat_id, boarding_passes)))
print("Challenge 1:", seat_ids[-1])

last = seat_ids[0] - 1
for s in sorted(seat_ids):
	if s != last + 1:
		print("Challenge 2:", s-1)
		break
	last = s

#print("\n".join([str(i) for i in sorted(seat_ids)]))