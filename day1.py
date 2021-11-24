#!/usr/bin/env python3

input_file = open("day1.txt", "r")
floor = 0
my_input = input_file.read()
instructions=[]
instructions.extend(my_input)
instruction_count=1
found = False
for move_inst in instructions:
    if move_inst == "(" : 
        floor = floor + 1
    else :
        floor = floor - 1
    if not found and floor == -1: 
        found = True
        print("Basement Instruction: {}".format(str(instruction_count)))
    instruction_count = instruction_count + 1    
print("Floor: {}".format(str(floor)))