#Even or Odd


#Constant O(1)
def is_it_even(number):
    """
    This function takes in an integer as a parameter
    The print statement is for display, place any integer in as an argument
    """
    if (number % 2) == 0:
        return True
    else:
        return False
#print(is_it_even())


#Less than 100


#Linear O(n)
def is_less_100(list_of_numbers):
    """
    Parameter:
    list_of_numbers : [int] -> The list of ints to check if less than 100

    Returns
    bool -> True if all are less, False if any are over 100
    """
    for number in list_of_numbers:
        if number >= 100:
            return False
    else:
        return True

print(is_less_100([]))#input a list of numbers to this argument

