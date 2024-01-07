# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230773
# Date: 30/11/2023

# import module for histogram
from graphics import *

# assign global variables
allCredits = []
progress_count=0
exclude_count=0
module_retriver_count=0
module_trailer_count=0

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
        global allCredits, progress_count, module_trailer_count, module_retriver_count, exclude_count

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
            if (progress_level== "Progress"):
                progress_count+=1
            elif (progress_level== "Progress (module trailer)"):
                module_trailer_count+=1
            elif (progress_level == "Module retriever"):
                module_retriver_count+=1
            elif (progress_level == "Exclude"):
                exclude_count+=1
                                                             
        else:                                                                       
            print("Total incorrect")                                                
            total_score()
        global total_count 
        total_count=progress_count+module_trailer_count+module_retriver_count+exclude_count                                         

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

def printCredits():
    print("Part 2:")
    # iterate over allCredits list
    for i in allCredits:
        # print course information with formatting
        print(i[3] + " - " + str(i[0]) + ", " + str(i[1]) + ", " + str(i[2]))
        
def histogram():
    win=GraphWin("Histogram", 800, 600)
    win.setBackground(color_rgb(232, 245, 233))

# draw line
    
    pt1 = Point(50, 500)
    pt2 = Point(700, 500)
    ln = Line(pt1, pt2)
    ln.setOutline(color_rgb(100, 100, 100))
    ln.setWidth(0.625)
    ln.draw(win)

# display histogram resultd
    
    txt = Text(Point(168, 50), "Histogram Results")
    txt.setTextColor(color_rgb(55, 71, 79))
    txt.setStyle('bold')
    txt.setSize(17)
    txt.setFace("times roman")
    txt.draw(win)

# display outcomes in total
    
    outcome="{} Outcomes in total".format(total_count)
    txt= Text(Point(180,550),outcome)
    txt.setTextColor(color_rgb(55, 71, 79))
    txt.setStyle('bold')
    txt.setSize(15)
    txt.setFace("times roman")
    txt.draw(win)

# display progress,trailler,retriever,excluded
    
    txt = Text(Point(128, 513), "Progress")
    txt.setTextColor(color_rgb(55, 71, 79))
    txt.setStyle('bold')
    txt.setSize(10)
    txt.setFace("times roman")
    txt.draw(win)
    
    txt = Text(Point(246, 513), "Trailer")
    txt.setTextColor(color_rgb(55, 71, 79))
    txt.setStyle('bold')
    txt.setSize(10)
    txt.setFace("times roman")
    txt.draw(win)
    
    txt = Text(Point(364, 513), "Retriever")
    txt.setTextColor(color_rgb(55, 71, 79))
    txt.setStyle('bold')
    txt.setSize(10)
    txt.setFace("times roman")
    txt.draw(win)

    txt = Text(Point(482, 513), "Excluded")
    txt.setTextColor(color_rgb(55, 71, 79))
    txt.setStyle('bold')
    txt.setSize(10)
    txt.setFace("times roman")
    txt.draw(win)

# display count

    txt=Text(Point(128,500-((progress_count*20)+10)),progress_count)
    txt.draw(win)

    txt=Text(Point(246,500-((module_trailer_count*20)+10)),module_trailer_count)
    txt.draw(win)

    txt=Text(Point(364,500-((module_retriver_count*20)+10)),module_retriver_count)
    txt.draw(win)

    txt=Text(Point(482,500-((exclude_count*20)+10)),exclude_count)
    txt.draw(win)

# draw bars
    
    bar1 = Rectangle(Point(75,500),Point(185,(500-progress_count*20)))
    bar1.setFill(color_rgb(144, 238, 144))
    bar1.draw(win)

    bar2 = Rectangle(Point(193,500),Point(303,(500-module_trailer_count*20)))
    bar2.setFill(color_rgb(147, 197, 114))
    bar2.draw(win)

    bar3 = Rectangle(Point(311,500),Point(421,(500-module_retriver_count*20)))
    bar3.setFill(color_rgb(138, 154, 91))
    bar3.draw(win)

    bar4 = Rectangle(Point(429,500),Point(539,(500-exclude_count*20)))
    bar4.setFill(color_rgb(224, 191, 184))
    bar4.draw(win)

    win.getMouse()
    win.close()
   
while True:
    user_input = input("Would you like to enter another set of data?\n"
                 + "Enter 'y' to continue or 'q' to quit and view results:").lower()
    if user_input == 'q':
        # call histogram
        histogram()
        printCredits()
        break
    elif user_input == 'y':
        multiple_outcome()
        continue
    else:
        print("Input not valid")
        

