"""
in_range.py

Check if a given integer is inside a given range.

Programmer: your_name_here, Date: date_modified_here
"""

def in_range(n, low, high)
    """
    Check whether given integer n is between low and high, inclusive.

    Parameters: 
        n, number to be checked
        low, low end of range
        high, high end of range

    Preconditions: high is greater than low

    Postconditions: None

    Returns: Boolean whether n is between low and high, inclusive. 
    """
    # your code here


def main():
    """
    Get user input for n, low, and high and display whether n is in range.

    Preconditions: None

    Postconditions: 
        - If n is in the range between low and high, print "n is in range!"
        - If not print "n is not in range..."
    """
    # Get user input
    n = int(input('n: '))
    
    # Your code here:
    # Get the other inputs
    # Pass all of them as arguments in a call to in_range()
    # Print message based on the return from in_range()
    
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()