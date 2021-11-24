#!/usr/bin/env python3

input_file = open("day3.txt", "r")
directions = input_file.read()

santa_x = 1
santa_y = 1
robo_x = 1
robo_y = 1

visits = {}
visits["1,1"] = 1

santa = True
for direction in directions: 
    if santa: 
        if direction == "^": 
            santa_y = santa_y+1
        if direction == "v":
            santa_y = santa_y-1
        if direction == ">": 
            santa_x = santa_x+1
        if direction == "<":
            santa_x = santa_x-1
        visits["{},{}".format(str(santa_x),str(santa_y))] = 1 
        santa=False 
    else:
        if direction == "^": 
            robo_y = robo_y+1
        if direction == "v":
            robo_y = robo_y-1
        if direction == ">": 
            robo_x = robo_x+1
        if direction == "<":
            robo_x = robo_x-1
        visits["{},{}".format(str(robo_x),str(robo_y))] = 1 
        santa=True 
        
print("At Least One: {}".format(str(len(visits))))