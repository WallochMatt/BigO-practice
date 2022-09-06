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

print(is_it_even())