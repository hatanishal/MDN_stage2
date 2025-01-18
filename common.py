"""
Author:     Nishal Joseph
Date:       18/01/25
Description:The file contains all the functions that will be needed for functionality of the project
"""
########################
#Required modules
import objects as ob

########################
#Set up / Initialisation of the application
########################

def create_user():
    """
    Author:     Nishal Joseph
    Date:       18/1/25
    Function:   Reads through the configuration file to create a user. If a user is not saved, it will create
                a user with a name and an empty set of habits and skills. Otherwise, it will read through and
                create a profile with past skills and habits already stored.
    
    Args:
                None

    Return:
                A "user" object
    
    """

    #Opens the configuration file
    with open("config.txt","r") as f:

        #Checks file can be accessed
        try:
            #Checks whether a profile has been previously set up or not.
            initial = f.readline()
            check = "".join(initial.split()[1:])

            #If it returns false OR file is empty, it will create a blank user
            if (check == "False") or (not initial):
                print("Enter your name:")
                name = input("")

                user = ob.user(name,[],[],0)

                return user
            
            #If file is not empty and True is returned from check
            else:
                #Initialise empty lists
                habits = []
                skills = []
                
                #Finds user's name
                line = f.readline()
                name = "".join(line.split()[1:])

                #Check if habits have been saved previously
                line = f.readline()
                check = "".join(line.split()[1:])

                if check == "True":
                    while line != "END OF HABITS":
                        line = f.readline()
                        habitName = "".join(line.split()[1:])

                        line = f.readline()
                        habitStreak = "".join(line.split()[1:])

                        line = f.readline()
                        habitPriority = "".join(line.split()[1:])

                        habit = ob.habit(habitName,habitStreak,habitPriority)
                        habits.append(habit)

                        line = f.readline()
                
                #Check if skils have been saved previously
                line = f.readline()
                check = "".join(line.split()[1:])

                #If true, it will iterate through and get details for each skill until end is specified
                if check == "True":
                    while line != "END OF SKILLS":
                        del_prac = []

                        line = f.readline()
                        skillName = "".join(line.split()[1:])

                        line = f.readline()
                        skillStreak = "".join(line.split()[1:])

                        line = f.readline()
                        skillPriority = "".join(line.split()[1:])
                        
                        #Checks for a list of deliberate practice 
                        line = f.readline()
                        check = "".join(line.split()[1:])

                        #Iterates through the practice list and appends it to an empty list
                        if check == "True":
                            line = f.readline()
                            while line != "END OF PRAC":
                                del_prac.append(line)
                                line = f.readline()

                        #Creates instance of skill and appends it a list of skills
                        skill = ob.skills(skillName,skillStreak,skillPriority, del_prac)
                        skills.append(skill)

                #Creates user and returns it
                user = ob.user(name,habits,skills)
                return user

                            

        except:
            pass #TODO