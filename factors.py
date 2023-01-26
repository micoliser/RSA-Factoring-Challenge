#!/usr/bin/python3

def print_factors(number):
    for num in range(2, number):
        if (number % num == 0):
            fct = number // num
            print("{:d}={:d}*{:d}".format(number, fct, num))
            break


def main():
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit()

    try:
        f = open(argv[1], "r")
    except FileNotFoundError:
        stderr.write("Could not find file {}, not exist\n".format(argv[1]))
    else:
        while (True):
            line = f.readline()
            if (not line):
                break
            line = int(line)
            print_factors(line)


main()
