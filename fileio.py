#!/usr/bin/env python

with open("input.txt", 'r') as ip, open("output.txt", 'w') as op:
    for line in ip.readlines():
        last_name, first_name = line.split(',')
        op.write("{} {}".format(first_name, last_name))
