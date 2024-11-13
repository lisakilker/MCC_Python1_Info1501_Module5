#Program asks user to enter a sentence or quit the program
def main():
    file_name = "test.rtf"
    
    #List to store user input
    user_data = []
    
    while True:
        #Asks the user to enter a string
        user_input = input("Please enter a sentence (or Q to quit): ")
        
        #Allows the user to quit the program
        if user_input.strip().upper() == "Q":
            break
        
        #Adds the user input to the list
        user_data.append(user_input)
    
    #Opens the file and appends the data to the file without overriding the original data
    with open(file_name, "a") as write_file:
        
        #Writes each input to the file
        for user in user_data:
            write_file.write(user + "\n")
    
    print("Saved!")
    
#Calls the main function
if __name__ == "__main__":
    main()