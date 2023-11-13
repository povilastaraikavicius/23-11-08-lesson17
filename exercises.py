# create a program which takes random sequence of numbers and letters (example: 'dfssdfsdfsdf655sdf2654fs6d4646'). 
# The program sgould return (All stages requires separate functions, with logging all necessary data to file and error handling):
# 1) list of letters ordered
# 2) list of letters of reversed order
# 3) funtion which return list with only uniques letters (Can't repeat)
# 4) the same do with numbers
# 5)the sum of amount of letters and numbers are provided
# Rules:
# The program after text entered, should provide options list of actions:
# 1) Get list ordered
# 2) Get list ordered reversed etc...

# If there is special symbols,gaps - they should be added to special data structure , as we will have option :
# n) Show special symbols if provided.
# After any option is being used, terminal should ask if we want to use another option or to exit the program.
# If we choose to use another option, the option we already choose should be marked as `checked`:
# 1) Get list ordered[checked]
# sequence length should be nor less than 25 characters 

# numbers_and_letters = input("Enter min 25 random numbers and letters: ")

# def order_letters(input_string):
#     letters = []
#     for char in input_string:
#         if char.isalpha():
#             letters.append(char)
    
#     sorted_letters = sorted(letters)
#     return sorted_letters

# input_string = input("Enter min 25 random numbers and letters: ")
# ordered_letters = order_letters(input_string)
# print("letters ordered: ",ordered_letters)
# print("reversed letters: ",ordered_letters[::-1])
import logging 

logging.basicConfig(level=logging.DEBUG, filename='exercises.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def letters(input_string):
    letters = [char for char in input_string if char.isalpha()]
    return sorted(letters)

def reverse_letters(letters):
    return sorted(letters, reverse=True)

def unique_letters(letters):
    return list(set(letters))

def numbers(input_string):
    numbers = [char for char in input_string if char.isdigit()]
    return sorted(numbers)

def unique_numbers(numbers):
    return list(set(numbers))

def count_letters_and_numbers(input_string):
    letters = [char for char in input_string if char.isalpha()]
    numbers = [char for char in input_string if char.isdigit()]
    return len(letters) + len(numbers)

try:
    input_string = input("Enter min 25 random numbers and letters: ")
    
    if input_string.isalnum() and len(input_string) >= 25:
       
        ordered_letters = letters(input_string)
        # print("ordered letters:", ordered_letters)
        reversed_ordered_letters = reverse_letters(ordered_letters)
        # print("reversed letters:", reversed_ordered_letters)
        unique_ordered_letters = unique_letters(ordered_letters)
        # print("unique letters:", unique_ordered_letters)
        ordered_numbers = numbers(input_string)
        # print("ordered numbers:", ordered_numbers)
        unique_ordered_numbers = unique_numbers(ordered_numbers)
        # print("unique numbers:", unique_ordered_numbers)
        count = count_letters_and_numbers(input_string)
        # print("Sum of letters and numbers:", count)

        while True:
            print("\nOptions:")
            print("1) Get letters")
            print("2) Get reversed letters")
            print("3) Get unique letters")
            print("4) Get numbers")
            print("5) Get unique numbers")
            print("6) Get sum of letters and numbers")
            print("7) Exit")


            choice = input("Enter your choice: ")

            if choice == '1':
                print("letters:", letters(input_string))
            elif choice == '2':
                ordered_letters = letters(input_string)
                print("Reversed letters:", reverse_letters(ordered_letters))
            elif choice == '3':
                ordered_letters = letters(input_string)
                print("Unique letters:", unique_letters(ordered_letters))
            elif choice == '4':
                print("numbers:",numbers(input_string))
            elif choice == '5':
                numbers = numbers(input_string)
                print("Unique numbers:", unique_numbers(numbers))
            elif choice == '6':
                print("Sum of letters and numbers:", count_letters_and_numbers(input_string))
            elif choice == '7':
                break
            else:
                print("Please enter a number between 1 and 7")
    else:
        raise ValueError("Input must be alphanumeric and at least 25 characters long.")
except Exception as err:
    logging.error(f"Error: {err}")
    print("Error, check input:")


   