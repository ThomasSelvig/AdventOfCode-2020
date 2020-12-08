from copy import deepcopy
import os


class Program:
	def __init__(self, parsed_instructions):
		self.reset_memory = deepcopy(parsed_instructions)
		self.reset()

	def rerun_new_instruction(self, index, new_ins) -> bool:
		""" 
		Re-runs the program with an instruction change
		new_ins format: (ins, int(arg))
		:return: whether the program terminated or not
		"""
		self.reset()
		self.memory[index] = deepcopy(new_ins)
		return self.run()
		
	def reset(self):
		self.prog_counter = 0
		self.acc = 0
		self.memory = deepcopy(self.reset_memory)
		self.prog_c_history = []

	def run(self) -> bool:
		""" runs the program, returns whether it terminated or not """
		while self.prog_counter < len(self.memory):  # run until it jumps out of instruction range
			# fetch
			ins = self.memory[self.prog_counter]
			
			# parse & execute
			if self.prog_counter in self.prog_c_history:
				return False
			
			self.parse_ins(*ins)
			
			# increment
			self.prog_c_history.append(self.prog_counter)
			self.prog_counter += 1
		
		return True

	def parse_ins(self, ins, arg):
		if ins == "acc":
			self.acc += arg
		elif ins == "jmp":
			self.prog_counter += arg - 1  # -1 to compensate for increment-cycle
		elif ins == "nop":
			pass


def challenge1(parsed_instructions):
	program = Program(parsed_instructions)
	program.run()
	return program.acc
	

def challenge2(parsed_instructions):
	""" what's the acc at when the program successfully terminates? """
	program = Program(parsed_instructions)
	for i, (ins, arg) in enumerate(parsed_instructions):
		if ins in ("nop", "jmp"):
			new_ins = "nop" if ins == "jmp" else "jmp"
			# try to rerun with this edited instruction
			if program.rerun_new_instruction(i, (new_ins, arg)):
				return program.acc


def main():
	PATH = os.path.dirname(os.path.abspath(__file__))
	assert "day8.txt" in os.listdir(PATH), "Paste puzzle input in \"day8.txt\""
	
	with open(f"{PATH}/day8.txt") as f:
		# parse instructions from input data as (instruction: str, arg: int)
		instructions = [
			(lambda ls: (ls[0], int(ls[1])))(i.split()) \
			for i in f.read().strip().split("\n")
		]

	print("Challenge 1:", challenge1(instructions))
	print("Challenge 2:", challenge2(instructions))


if __name__ == "__main__":  # run all definitions before init + don't run on import
	main()
