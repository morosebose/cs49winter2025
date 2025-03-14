"""
list_parameter.py

Demonstrate difference between passing ints and lists as parameters:

Programmer: Surajit A. Bose, Date: 2025.03.14
"""

def add_two_elements(some_list):
    """Accept a list as an input argument and add two elements at the end"""
    some_list.extend([6, 7])
    print(f'List in add_two_elements() is: {some_list}')
    
    
def add_two_to_number(num):
    num += 2
    print(f'Number in add_two_to_number() is: {num}')
    

def main():

    # assign an integer to a variable
    my_num = 2
    # create original list
    my_list = [1, 2, 3]
    
    #print original values
    print('Before function calls:')
    print(f'Number in main() is: {my_num}')
    print(f'List in main() is: {my_list}')
    print()
    
    # call functions
    print('As functions execute:')
    add_two_to_number(my_num)
    add_two_elements(my_list)
    print()
    
    # print values in main list after functions are done executing
    print('After functions are done executing:')
    print(f'Number in main() is: {my_num}')
    print(f'List in main() is: {my_list}')
    print()
        
if __name__ == "__main__":
    main()