import random
import string 



'''
    Ranker function that ranks the password based on the assigned criteria
    Input: pwd -> character or string
    The following are the requirements for POOR / MODERATE / STRONG password.
    Passwords can contain (not required) any of the following requirements:  
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).  
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )
    1. A POOR Password is defined as: 
    a. Contains less than 3 from the above 4 items ( i – iv ).  
    b. Less than 8 characters in length.
    2. A MODERATE Password is defined as:  
    a. Contains 3 from the above 4 items ( i – iv )  
    b. Between 8 to 10 characters in length.
    3. A STRONG Password is defined as:  
    a. Meets all 4 of the above items ( i – iv )  
    b. Greater than 10 characters in length.
    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here
def rank(pwd: str) -> str:
    rank = 'POOR'
    counter = 0
    for c in pwd:
        if c.islower():
            counter += 1
        elif c.isupper():
            counter += 1
        elif c.isdigit():
            counter += 1
        elif c in string.punctuation:
            counter += 1
    if counter >= 3 and len(pwd) >= 8 and len(pwd) <= 10:
        rank = 'MODERATE'
    if counter == 4 and len(pwd) > 10:
        rank = 'STRONG'
    return rank
    
    ## End code here
    return rank

def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds. 
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values. 
    # 5. Close necessary files and print to terminal.
    
    ## START CODE HERE



    # Prompt the user to enter the name of the file containing the username and password pairs

    # Prompt the user to enter the name of the file containing the username and password pairs
    filename = input("Enter the name of the file containing the username and password pairs (e.g. Users-Pwds.txt): ")

    try:
        # Open the file containing username and password in each line
        with open(filename, "r") as f:
            # Store the list of username,passwords in a variable called usrpwds
            usrpwds = [line.strip().split(",") for line in f]

        # Open the file to store the ranked password information
        with open("Users-Pwds-Chked.txt", "w") as f:
            # Iterate through the list of username,password pairs
            for usr, pwd in usrpwds:
                # Use the rank() function to rank the password
                rank = rank(pwd)
                # Write to the file (username,password,rank) as a string
                f.write(f"{usr},{pwd},{rank}\n")

    except FileNotFoundError:
        # Print an error message if the file could not be found
        print("Error: the file could not be found. Please check the file name and try again.")

 # Close necessary files
    f.close()

 # Print to terminal
    print("Password ranking complete!")




    print('#'*80)
        # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    print('[INFO] '+'Number of passwords checked:',str(len(usrpwds))) 
    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
    print('#'*80)

def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    
    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    '''

    def generate() -> str:
            '''
            Helper function to generate password.
            Returns: A string pwd with strong ranking in our ranking system.
            '''
            # Starter code, Ualphabets contains all upper case alphabets
            # Lalphabets condains all lowercase alphabets
            # chars contains all special characters and digits contains all numeric digits
            Ualphabets = string.ascii_uppercase
            Lalphabets = string.ascii_lowercase
            chars = string.punctuation
            digits = string.digits
            pwd = ''
            # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
            # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
            
            ## START CODE HERE
    def generate_password():
    # Prompt the user for a username
        username = input("Enter a username (no more than 20 characters): ")
        if len(username) > 20:
            print("Error: username must be 20 characters or less.")
            return
        
        # Generate a strong password
        password_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(password_chars, k=16))
        print("Your password is:", password)
        
        # Ask the user if they want to save the password
        save_password = input("Would you like to save this password? (Y/N) ")
        if save_password.lower() == 'y':
        # Open the Users-Pwds.txt file and append the username and password to the end of the file
         with open('Users-Pwds.txt', 'a') as f:
          f.write(f"{username},{password}\n")
         print("Password saved successfully.")
        elif save_password.lower() == 'n':
        # Ask the user if they want to generate a different password for this user
         different_password = input("Would you like to generate a different password for this user? (Y/N) ")
         if different_password.lower() == 'y':
          generate_password()
         else:
          print("Password not saved.")
        else:
         print("Invalid input. Password not saved.")

    # Test the generate_password function
    generate_password()



def main():

    print('Welcome to my password ranking program')
    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = input("Enter your option here:")
            
            # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
            # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 

            ## START CODE HERE
        try:
            inp = int(inp)
        except ValueError:
            print("Conversion error, Please enter valid option")

            # task handling
        if inp == 3:
            break
        elif inp == 1:
            option1()
            
        elif inp == 2:
            option2()

        ## END CODE HERE


# DONOT TOUCH THESE LINES
if __name__=='__main__':
    main()