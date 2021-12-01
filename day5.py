#!/usr/bin/env python3

input_file = open("day5.txt", "r")
inputs = input_file.readlines()

is_nice = True
for line in inputs:
    vowel_count = 0
    for vowel in ["a","e","i","o","u"]: 
        if line.__contains__(vowel): 
            vowel_count = vowel_count +1
        
print(len(inputs))