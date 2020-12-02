from pyperclip import copy, paste
import re


pw_lines = [l for l in paste().strip().split("\r\n")]


class Challenge1:
	def valid(min_c, max_c, c, pw):
		return pw.count(c) <= int(max_c) and pw.count(c) >= int(min_c)

	def __init__(self):
		valid_pws = [pw for pw in pw_lines if Challenge1.valid(*re.match(r"(\d+)-(\d+) (\w): (\w+)", pw).groups())]

		print(len(valid_pws))


class Challenge2:
	def valid(n1, n2, c, pw):
		return (pw[int(n1)-1] == c) != (pw[int(n2)-1] == c)

	def __init__(self):
		valid_pws = [pw for pw in pw_lines if Challenge2.valid(*re.match(r"(\d+)-(\d+) (\w): (\w+)", pw).groups())]

		print(len(valid_pws))


Challenge1()
Challenge2()