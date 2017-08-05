import sys
import re
import getpass


def password_check(password):
	"""
	Set values for the password strenght checker
	"""

	# Calculate length
	length_error = len(password) < 8

	# Search for digits
	digit_error = re.search(r"\d", password) is None

	# Search uppercase
	uppercase_error = re.search(r"[A-Z]", password) is None

	# Search lowercase
	lowercase_error = re.search(r"[a-z]", password) is None

	# Search symbols
	symbol_error = re.search(r"[ !£$%^&*()_+-=<,>.:;@'~#[\\\]/{|}?¬"+r'"]', password) is None

	# Overall result
	password_ok = not ( length_error or digit_error or lowercase_error or uppercase_error or symbol_error)

	return {
		'password_ok' : password_ok,
		'length_ok' : length_error,
		'upper_error' : uppercase_error,
		'lower_error' : lowercase_error,
		'digits_error' : digit_error,
		'symbols_error' : symbol_error,
	}


def main():
	password = getpass.getpass("Enter the password to test: ")
	check_dict = password_check(password)
	for k, v in check_dict.items():
		print(k, '\t-->\t', v)

	# Check if the password is acceptable
	if check_dict['password_ok'] != True:
		print("\nNOT ACCEPTABLE")
	else:
	    print("\nIS ACCEPTABLE")

	# Deletes the password from memory
	del password

if __name__ == '__main__':
	main()
