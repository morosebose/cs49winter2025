"""
square_number.py

Prompt the user for a number. Display the square of the number.

Programmer: Surajit A. Bose, Date: 2024.05.03
"""

def main():
    """Get number from user and print out its square."""
    
    num = float(input('Type a number to see its square: '))
    print(f'{num} squared is {num * num}')

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()