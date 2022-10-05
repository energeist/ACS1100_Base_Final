'''
Online banking app for final assessment in ACS1100
Data.txt has a list of users and information that will be parsed by the program
The user will be prompted to input their username/password combo and if either are not found or the combination is not correct they will be denied access without exposing which element was incorrect.
If a correct username and password combination is entered, the user will be shown their account information and granted access to extra functions.
'''
# define the data file as a variable for file read-in
user_file = "./data.txt"

account_info = {}

def get_accounts(user_file):
    '''
    A funciton that opens data.txt and creates a dictionary of with usernames as keys and password, full_name, and balance as associated values
    Input - user_info (string): location of the data.txt file as a string
    Return - account_info (dict): compiled dict of usernames as keys + associated info as values
    '''
    file_lines = open(user_file, "r").readlines()
    for line in file_lines:
        split_line_list = line.rstrip().split(",")
        username = split_line_list[0]
        password = split_line_list[1]
        full_name = split_line_list[2]
        balance = split_line_list[3]
        account_info[username] = password, full_name, balance

def authenticate():
    '''
    A function to get user input of username and password, which validates matching key/value pairs for username/password.  Allows access when given a correct un/pw pair
    Input - nothing
    Return - input_username (string): authenticated username
    '''

    input_username = input("Please input your username > ")
    input_password = input("Please enter your password > ")

    # nested conditionals to eliminate key errors on bogus username input

    if input_username in account_info:
        if input_password == account_info[input_username][0]:
            print("Access granted!")
            authenticated_user = input_username
            return authenticated_user     
        else:
            print("User name and password not found.")
    else:
        print("User name and password not found.")

     

def display_information(authenticated_user):
    '''
    A function to display full name and balance information for a successfully authenticated user
    Input - authenticated_user (string): validated username received as return from autheticate() function
    Return - none
    '''
    print(f'Full name: {account_info[authenticated_user][1]}')
    print(f'Current balance: {account_info[authenticated_user][2]}')

# Program are calls here, currently infinitely loops until force close

get_accounts(user_file)
while True:
    authenticated_user = authenticate()
    if authenticated_user in account_info:
        display_information(authenticated_user)
