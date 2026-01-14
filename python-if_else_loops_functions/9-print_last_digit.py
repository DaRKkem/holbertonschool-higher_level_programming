#!/usr/bin/python3
def print_last_digit(number):
	""" Print the last digit of a number """
	number = number % 10 if number >= 0 else -(number % -10)
	print(number, end="")
	return number
