# ------------------------------------------------- #
# Title: Assignment 7- Pickling and Structured Error Handling
# Description: Demonstrates pickling data and handling exceptions
# ChangeLog: (Who, When, What)
# AShafique, 05.26.2022, Created
# ------------------------------------------------- #

# -- Data -- #
lstInt = []  # list
objFile = "example.dat"  # file where data will be stored
strChoice = ""  # empty string that will save user input
strEnd = ""  # empty string that will store whether the user wants to exit

# -- Processing -- #
import pickle

def read_file(file_name):
    '''
    Function unpickles and loads data from file_name.
    :param file_name: name of file to be read
    :return: file data
    '''
    try:
        file = open(file_name, "rb")
        file_data = pickle.load(file)
        file.close()
        print(file_data)
    except:
        print("File not found.")

def write_file(file_name, some_list):
    '''
    Function writes pickled data in some_list to the file file_name.
    :param file_name: name of file that data is written to
    :param some_list: list of data that will be written to file
    :return: nothing is returned
    '''
    try:
        file = open(file_name, "wb")
        pickle.dump(some_list, file)
        file.close()
        return 'Success!'
    except Exception as e:
        print("Error.")
        print(e)

def input_two_int():
    '''
    Asks for user input for 2 numbers
    :return: returns 2 integers that have been inputted by the user
    '''
    try:
        number1 = int(input("Enter an integer: "))
        number2 = int(input("Enter another integer: "))
    except ValueError as e:
        print("Please choose an integer!")
        print(e)
    except TypeError as e:
        print("Please choose an integer!")
        print(e)
    except Exception as e:
        print("There was an error!")
        print(e)
    else:
        return number1, number2


def math_menu_op():
    '''
    Gets user input on which operation to perform
    :return: returns user choice
    '''
    print(
        """
        1 = Addition
        2 = Subtraction
        3 = Multiplication
        4 = Division
        """
    )
    while True:
        try:
            choice = int(input("Which operation do you want to do? Choose 1,2,3, or 4:"))
            if choice > 4 or choice < 1:
                raise Exception("Choose only 1, 2, 3, or 4")
        except ValueError as e:
            print("Please choose an integer 1, 2, 3, or 4!")
            print(e)
            continue
        except TypeError as e:
            print("Please choose an integer 1, 2, 3, or 4!")
            print(e)
            continue
        except Exception as e:
            print("There was an error!")
            print(e)
            continue
        else:
            return choice


def math_op(number1, number2, operation):
    '''
    Perform basic arithmetic operations based on arguments passed into parameters.
    :param number1: first integer to be used for operation
    :param number2: second integer to be used for operation
    :param operation: the operation to be done on the numbers
    :return: the sum, difference, product, or quotient, depending on the arguments
    '''

    if operation == 1:
      return number1 + number2
    if operation == 2:
      return number1 - number2
    if operation == 3:
      return number1*number2
    if operation == 4:
        try:
            quotient = number1/number2
        except ZeroDivisionError as e:
            print("You can't divide by 0!")
            print(e)
        except Exception as e:
            print("Some error has occurred.")
            print(e)
        else:
            return quotient


def add_to_list(data, list_name):
      '''
      Appends data to a list
      :param data: Some integer values
      :param list_name: List that lists integer values
      :return: updated list after the data has been appended
      '''
      list_name.append(data)
      return list_name

def what_to_do():
    '''
    Asks user what s/he would like to do.
    :return: the (string) value choice
    '''
    todo = input("Which choice would you like to do from the menu? ")

    return todo

# -- Presentation (I/O) -- #

while True:  # main script
    print(
        """
        1 = Add numbers to the list
        2 = Save data
        3 = Load data
        4 = Exit
        """
    )
    strChoice = what_to_do()
    if strChoice == "1":
        intA, intB = input_two_int()  # capturing the return from the functions into variables
        intOp = math_menu_op()
        intData = math_op(intA, intB, intOp)
        add_to_list(intData, lstInt)
        print(f"You add {intData} to the list {lstInt}")
        continue  # return to the beginning of the while loop

    if strChoice == "2":
        write_file(objFile, lstInt)
        print("Data Saved!")
        continue

    if strChoice == "3":
        read_file(objFile)
        continue

    if strChoice == "4":
        strEnd = input("Do you wish to continue? Answer 'y' or 'n'")
        if strEnd.lower() == 'y':
            print("Unsaved data will be lost!")
            break  # break out of the while loop and end the program
        else:
            continue

    else:
        print("Please Choose one of the 4 integer choices from the menu.")


