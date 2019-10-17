#!/usr/bin/python
import argparse
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lines')
    args = parser.parse_args()
    
    with open(args.lines, "r") as f:
        line_numbers = f.read().splitlines()
    idx = 0
    num = 1
    for line in sys.stdin:
        if num > int(line_numbers[-1]):
            sys.exit(0)
        if int(line_numbers[idx]) == num:
            print line,
            idx += 1
        num += 1    

