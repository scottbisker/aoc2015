#!/usr/bin/env python3

input_file = open("day3.txt", "r")
directions = input_file.read()

x_coord = 1
y_coord = 1
santa_visits = {}
robo_visits = {}
santa_visits["1,1"] = 1
robo_visits["1,1"] = 1

santa = True
for direction in directions: 
    if direction == "^": 
        y_coord = y_coord+1
    if direction == "v":
        y_coord = y_coord-1
    if direction == ">": 
        x_coord = x_coord+1
    if direction == "<":
        x_coord = x_coord-1
    santa_visits["{},{}".format(str(x_coord),str(y_coord))] = 1 
count = 0
for item in santa_visits: 
    count = count + 1 
print("At Least One: {}".format(str(count)))