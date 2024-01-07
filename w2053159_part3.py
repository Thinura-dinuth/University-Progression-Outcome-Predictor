# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230773
# Date: 30/11/2023

# assign global variables
allCredits = []


def multiple_outcome():    
    def value_check(progression_level):
        # loop until input valid
        while True:                                                                           
            try:
                # get user input as intiger
                credit_score = int(input(f"Please enter your credits at {progression_level} : "))
                # check the input is valid
                if(0 <= credit_score<=120 and (credit_score % 20) == 0):               
                    return credit_score                                                         
                else:                                                                          
                    print("Out of range")                                                      
            except ValueError:                                                                 
                print("Integer required")                                                      
                       
    def progression_outcome(Pass, Fail):
        progression_outcome_1 = "Progress"                                    
        progression_outcome_2 = "Progress (module trailer)"                   
        progression_outcome_3 = "Module retriever"                            
        progression_outcome_4 = "Exclude"

        # check and return progression outcome
        if(Pass == 120):                                          
            return progression_outcome_1                                   
        elif(Pass == 100):                                        
            return progression_outcome_2                                   
        elif(Fail >= 80):                                         
            return progression_outcome_4                                    
        else:                                                   
            return progression_outcome_3

    def check_total(total, instanceCredits):
        # use allCredits as a global variable
        global allCredits

        # check the total credits are valid
        if(total == 120):
            # get the progression outcome
            progress_level = progression_outcome(instanceCredits[0], instanceCredits[2])
            # append progression lvl to 'instanceCredits'
            instanceCredits.append(progress_level)
            # append the list of validated credits to 'allCredits'
            allCredits.append(instanceCredits)
            # print the prograss lvl
            print(progress_level)                                                   
        else:                                                                       
            print("Total incorrect")                                                
            total_score()                                        

    def total_score():
        # assign varibale to store user inputs temporary
        instanceCredits = []

        # get & append user inputs
        instanceCredits.append(value_check("pass"))
        instanceCredits.append(value_check("defer"))
        instanceCredits.append(value_check("fail"))

        # calculate total credits
        total = instanceCredits[0] + instanceCredits[1] + instanceCredits[2]
        # check validation of total credits
        check_total(total, instanceCredits)

    # call total score to get user inputs and check the total is valid
    total_score()
multiple_outcome()

while True:
    user_input = input("Would you like to enter another set of data?\n"
                 + "Enter 'y' to continue or 'q' to quit and view results:").lower()
    if user_input == 'q':
    # function to save list to a txt file
        def save_to_txt(allCredits):
            with open('credits.txt', 'w') as f:
                f.write("Part 3:\n")
                for credits in allCredits:
                    # write in the text file with formating
                    f.write(credits[3] + " - " + str(credits[0]) + ", " + str(credits[1]) + ", " + str(credits[2]) + '\n')
        save_to_txt(allCredits)
       
        with open('credits.txt', 'r') as f:
            # read the text file
            content = f.read()
            print(content)
            break
    elif user_input == 'y':
        multiple_outcome()
        continue
    else:
        print("Input not valid")
        

        

