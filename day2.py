#!/usr/bin/env python3

input_file = open("day2.txt", "r")
bag_o_presents = input_file.readlines() 
total_paper = 0
total_ribbon = 0
for  present in bag_o_presents:
    dimensions = present.split("x")
    sides = []
    sides.append(int(dimensions[0])*int(dimensions[1]))
    sides.append(int(dimensions[0])*int(dimensions[2]))
    sides.append(int(dimensions[1])*int(dimensions[2]))
    
    total_paper = total_paper + 2*sides[0] + 2*sides[1] + 2*sides[2] + min(sides)  
    perimeters =[]
    perimeters.append(int(dimensions[0])*2 + int(dimensions[1])*2)
    perimeters.append(int(dimensions[0])*2 + int(dimensions[2])*2)
    perimeters.append(int(dimensions[1])*2 + int(dimensions[2])*2)
    volume = int(dimensions[0])*int(dimensions[1])*int(dimensions[2])
    total_ribbon = total_ribbon + volume + min(perimeters)
    
print("Total Paper: {}".format(str(total_paper)))
print("Total Ribbon: {}".format(str(total_ribbon)))