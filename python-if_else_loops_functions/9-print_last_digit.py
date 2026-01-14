#!/usr/bin/python3
def print_last_digit(number):
	""" Print the last digit of a number """
	number = number % 10 if number >= 0 else -(number % -10)
	print(number, end="")
	return number

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
