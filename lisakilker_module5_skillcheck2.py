#Displays the data entered from the user in program 1
def main():
    filename = "test.rtf"
    
    while True:
        #Asks the user if they want to read the file or quit
        user_input = input("Enter 'R' to read the file or 'Q' to quit: ").strip().upper()
        
        if user_input == "R":
            #Opens and reads the file
            with open(filename, "r") as file:
                data_exists = file.read().strip()
                if data_exists:
                    print(data_exists)
                else:
                    #If the file is empty this will display
                    print("The file is empty!")
            #Ends the program and doesn't ask the user for more input
            break

        #User can enter Q to quit
        elif user_input == "Q":
            print("I quit!")
            break
        else:
            #If the user doesn't enter a valid option, it re-asks them
            print("That's not right! Please enter 'R' to read the file or 'Q' to quit.")
    
#Calls the main function
if __name__ == "__main__":
    main()