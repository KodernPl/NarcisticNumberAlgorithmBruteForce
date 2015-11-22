# Krzysztof Kuziel www.krzykustudio.pl
# Python 3.5
# Narcistic Numbers Finder Brute Force Algorithm

from datetime import datetime
from decimal import Decimal
import decimal

def find_armstrong_numbers_bruteforce(number_of_digits):
    """ 
    Founds and returns narcistic Numbers in given range 
    @param max_finding_value upper range 
    """
    # range of number to check
    low_value = 10**(number_of_digits - 1) 
    max_value = 10**number_of_digits - 1
      
    def is_Armstrong(number):
        """
        Find in number is Narcistic number
        @param number to check
        @return true if Number is Narcistic 
        """
        string_number = str(number)     #number to string
        n = len(string_number)          #get the pow from number of digits
        summed_number = 0               #starting sum
        for chars in string_number:     
            summed_number += int(chars)**n

        if summed_number == number:
            return True

        return False

    def search(low_value, max_value):
        """
        Number Generator
        Serarch if numbers in given range are narcistic
        """
        for idx in range(low_value, max_value + 1):
            if(is_Armstrong(idx)):
                yield idx

    yield from search(low_value,max_value)

# Start Time
start_time = datetime.now()
# Starting number of digits
number_of_digits = 0
# Sum of find Narcistic numbers
total_numbers = 0

while True:
	number_of_digits += 1
	print("Number of digits:", number_of_digits)

	#Finds and prints numbers that have number_of_digits
	for number in find_armstrong_numbers_bruteforce(number_of_digits):
		print(number)
		total_numbers += 1
	end_time = datetime.now()
	print("Total numbers Found:", total_numbers, " Total time:" , end_time - start_time, "\n")

