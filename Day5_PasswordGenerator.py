## DAY 5
## 100 DAYS OF PYTHON
## https://100daysofpython.dev/

## Password Generator Project
## CODE START:  https://replit.com/@appbrewery/password-generator-start
## CODE END: https://replit.com/@appbrewery/password-generator-end

## IMPORT MODULES
import random

## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTION
def fn_PasswordCreate(ListOfLetters, ListOfSymbols, ListOfNumbers):

    ## DECLARE VARIABLE
    password = ""

    ## BEGIN FOR LOOP
    for each in range(1, (nr_letters + 1)):
        password += random.choice(ListOfLetters)

    ## END FOR LOOP

    ## BEGIN FOR LOOP
    for each in range(1, (nr_symbols + 1)):
        password += random.choice(ListOfSymbols)

    ## END FOR LOOP

    ## BEGIN FOR LOOP
    for each in range(1, (nr_numbers + 1)):
        password += random.choice(ListOfNumbers)

    ## END FOR LOOP

    ## RETURN
    return(password)

## END DEFINE FUNCTION

## BEGIN DEFINE FUNCTION
def fn_PasswordShuffle(password):

    ## DECLARE VARIABLE
    password_shuffled = ""

    ## CREATE LIST FROM THE PASSWORD STRING
    password = list(password)

    ## SHUFFLE ORDER OF LETTERS IN PASSWORD
    random.shuffle(password)

    ## BEGIN FOR LOOP
    for each in password:
        password_shuffled += each

    ## END FOR LOOP

    ## RETURN
    return(password_shuffled)

## END DEFINE FUNCTION
## END DEFINE FUNCTIONS

## BEGIN MAIN PROGRAM

## DECLARE VARIABLES
ListOfLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ListOfNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ListOfSymbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

## TEST PRINT OUTPUT
print("\n")
print("Welcome to the PyPassword Generator!")

## GET USER INPUT
nr_letters= int(input("How many letters would you like in your password\n")) 
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))

## - First Password - Easy Level - Order not randomised:
## e.g. 4 letter, 2 symbol, 2 number = JduE&!91

## CALL FUNCTION
password = fn_PasswordCreate(ListOfLetters, ListOfSymbols, ListOfNumbers)

## TEST PRINT OUTPUT
print("First Password - Your randomly-generated, non-shuffled password is: ", password)

## Second Password - Hard Level - Order of characters randomised:
## e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

## CALL FUNCTION
password = fn_PasswordShuffle(password)

## TEST PRINT OUTPUT
print("Password - Your randomly-generated, shuffled password is: ", password)
print("GAME OVER")
print("\n")

## END MAIN PROGRAM
