#!/usr/bin/env python3
import hashlib

input_file = open("day4.txt", "r")
prefix = input_file.read()

suffix = 0
found = False
while not found: 
    prehash = "{}{:05d}".format(prefix,suffix)
    md5_hash = hashlib.md5(prehash.encode()).hexdigest()
    if md5_hash.startswith("000000"): 
        found = True
    else: 
        suffix = suffix + 1
print(suffix)
    
