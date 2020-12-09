""" written while sleep deprived don't judge >:( """

from pyperclip import paste
import re


class Bag:
	def parse(string):
		amount, adj, col = re.match(r"(\d+) (\w+) (\w+) bag", string).groups()
		return Bag(adj, col, amount=int(amount))

	def __init__(self, adj, col, *containing, amount=1):
		self.adj = adj
		self.col = col
		self.amount = amount
		self.containing = list(containing)
	
	def potential_bags_held(self, gz_bag, incl_self=False, parent=None):
		bags = {self} if incl_self else set()
		if parent:
			self.total_amount = parent.amount * self.amount
		for bag in self.containing:
			# append bag
			bags |= bag.potential_bags_held(gz_bag, incl_self=True, parent=self)
			# append potential finds
			if bag in gz_bag:
				bags |= gz_bag[bag].potential_bags_held(gz_bag, incl_self=True, parent=self)
		
		return bags
	
	def bags_required(self, definition):
		# update self
		if not self.containing and self in definition:
			self.containing = definition[self].containing

		# last link in chain condition
		if not self.containing:
			return self.amount
		
		# return self + children
		return self.amount + sum([self.amount * cbr for cbr in [b.bags_required(definition) for b in self]])
		
	def __getitem__(self, item):
		for bag in self.containing:
			if bag == item:
				return bag

	def __eq__(self, other):
		return all([i == o for i, o in zip(
			[self.adj, self.col],
			[other.adj, other.col]
		)])
	
	def __hash__(self):
		return hash(f"{self.adj} {self.col}")
	def __contains__(self, item):
		return item in self.containing
	def __str__(self):
		return f"{self.adj} {self.col}"
	def __repr__(self):
		return str(self)
	def __iter__(self):
		return self.containing.__iter__()
	def __next__(self):
		return self.containing.__next__()


# parse input as 'Bag' containments of gz_bag (definitions of a certain bag)
gz_bag = Bag("", "")  # ground-zero bag (lackluster airport sec)
for line in paste().strip().split("\r\n"):
	adj, col = re.match(r"(\w+) (\w+)", line).groups()

	gz_bag.containing.append(Bag(adj, col, *[
			Bag.parse(i) for i in line.split(" contain ")[1].split(", ")
		] if "no" not in line else []))


def challenge1():
	i = 0
	goal = Bag("shiny", "gold")
	for bag in gz_bag:
		if goal in bag.potential_bags_held(gz_bag):
			print(bag)
			i += 1
	return i


def challenge2():
	return gz_bag[Bag("shiny", "gold")].bags_required(gz_bag) - 1


print(f"Challenge 1: {challenge1()}, Challenge 2: {challenge2()}")
