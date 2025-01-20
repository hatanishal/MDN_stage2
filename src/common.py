"""
Author:     Nishal Joseph
Date:       18/01/25
Description:The file contains all the functions that will be needed for functionality of the project
"""
########################
#Required modules

import objects as ob
import random
########################


########################
#Set up / Initialisation of the application
########################

def create_user(file_dir):
    """
    Author:     Nishal Joseph
    Date:       19/1/25
    Function:   Reads through the configuration file to create a user. If a user is not saved, it will create
                a user with a name and an empty set of habits and skills. Otherwise, it will read through and
                create a profile with past skills and habits already stored.
    
    Args:
                file_dir: String directory path to the config file

    Return:
                A "user" object
    
    Usecase:    
                create_user("src/config.txt")

    Time-Complexity: O(n)
    
    """

    #Checks file can be accessed
    try:

        #Opens configuration file with all saved information
        with open(file_dir,"r") as f:
            #Checks whether a profile has been previously set up or not.
            initial = f.readline()
            check = "".join(initial.split()[1:])

            #If it returns false OR file is empty, it will create a blank user
            if (check == "False") or (not initial):
                print("Enter your name:")
                name = input("")

                user = ob.user(name,[],[],200)

                return user
            
            #If file is not empty and True is returned from check
            else:
                #Initialise empty lists
                habits = []
                skills = []
                
                #Finds user's name
                line = f.readline()
                name = "".join(line.split()[1])
                #gets user's coins
                line = f.readline()
                coins = int("".join(line.split()[1]))

                #Check if habits have been saved previously
                line = f.readline()
                check = "".join(line.split()[1])

                if check == "True":
                    line = f.readline()
                    while not (line.strip() == "END OF HABITS".strip()):
                        habitName = line.split()[1]

                        line = f.readline()
                        habitStreak = "".join(line.split()[1])

                        line = f.readline()
                        habitPriority = "".join(line.split()[1])

                        habit = ob.habit(habitName,habitStreak,habitPriority)
                        habits.append(habit)

                        line = f.readline()
                
                #Check if skils have been saved previously
                line = f.readline()
                check = "".join(line.split()[1])

                #If true, it will iterate through and get details for each skill until end is specified
                if check == "True":
                    while not (line.strip() == "END OF SKILLS".strip()):
                        del_prac = []

                        line = f.readline()
                        skillName = "".join(line.split()[1])

                        line = f.readline()
                        skillStreak = "".join(line.split()[1])

                        line = f.readline()
                        skillPriority = int("".join(line.split()[1]))
                        
                        #Checks for a list of deliberate practice 
                        line = f.readline()
                        check = "".join(line.split()[1])

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
                user = ob.user(name,habits,skills,coins)
                return user           

    except FileNotFoundError:
        print("Configuration file was not found :(")


########################
# Exit / Writing to Config File
########################

def save_user(file_dir,user):
    """
    Author:         Nishal Joseph
    Last modified:  20/1/25
    Function:       To save the user's data to the config file so that the saved data can be used next time

    Args:
                    file_dir: The file directory to config.txt
                    user: Instance of class "user"
    
    Returns:
                    None
    
    Usecase:        
                    save_user("src/config.txt")
    
    Time-Complexity: O(n)
                    
    """

    #Checks if the file directory is correct
    try:
        with open(file_dir,"w") as f:

            #Get user details
            name =  user.name #String
            coins = user.coins #int
            habits = user.habits #list
            skills = user.skills #list

            #Writes down name and coins saved
            f.write("SETUP_CHECK: True\n")
            f.write(f"NAME: {name}\n")
            f.write(f"COINS: {coins}\n")

            #Cycles through all habits and saves it
            if len(habits) == 0:
                f.write("SAVED_HABITS: False\n")
            else:
                f.write("SAVED_HABITS: True\n")

                #For each habit being tracked, write down individual details
                for i in range(len(habits)):
                    habit = habits[i]
                    habitName = habit.name
                    habitStreak = habit.streak
                    habitPriority = habit.priority

                    f.write(f"habit: {habitName}\n")
                    f.write(f"streak: {habitStreak}\n")
                    f.write(f"prio: {habitPriority}\n")

                    #Divide the habits with "-"" if it is not the last habit
                    if i != (len(habits) - 1):
                        f.write("-\n")
                    else:
                        #If it is the last, state the end
                        f.write("END OF HABITS\n")

            #Cycles through all the skills and saves it
            if len(skills) == 0:
                f.write("SAVED_SKILLS: False\n")
            else:
                f.write("SAVED_SKILLS: True\n")
                
                for i in range(len(skills)):
                    skill = skills[i]
                    skillName = skill.name
                    skillStreak = skill.streak
                    skillPriority = skill.priority
                    skillPractice = skill.del_prac

                    f.write(f"skill: {skillName}\n")
                    f.write(f"streak: {skillStreak}\n")
                    f.write(f"prio: {skillPriority}\n")
                    
                    if len(skillPractice) == 0:
                        f.write("DEL_PRAC: False\n")
                    else:
                        f.write("DEL_PRAC: True\n")

                        for j in range(len(skillPractice)):
                            f.write(f"{skillPractice[j]}\n")
                    
                        f.write("END OF PRAC\n")
            
            f.write("END OF SKILLS\n")              


    except FileNotFoundError:
        print("config.txt file does not exist")


########################
# Functionality
########################

def update_streak(user,loss_gain, habit_skill,index):
    """
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   To update the streak of habit/skill based on the input of the user

    Args:
                user: The instance of the object "user"
                loss_gain: Whether the streak is kept or lost, 0 for loss and 1 for saved
                habit_skill: specify the intention with 0 for habit, 1 for skill
                index: The index of the skill/habit on the saved list

    Returns:
                None
    
    Time-Complexity: O(1)
                
    """
    #Chooses action depending on ehether habit or skill needs updating
    if habit_skill == 0:

        habit = user.habits[index]
        #Decides whether to reset or continue streak
        if loss_gain == 0:
            habit.reset_streak()
            user.coins -= habit.penalty
            print("Streak reset...")
            print(f"You lost {habit.penalty} coins\nYou have {user.coins} remaining.")
            return
        elif loss_gain == 1:
            habit.continue_streak()
            user.coins += habit.reward
            print("Streak continued!")
            print(f"You gained {habit.penalty} coins!\nYou have {user.coins} remaining.")
            return
        else:
            print("Invalid response, choose between 0 and 1 to reset or continue streak.")
            return
    elif habit_skill == 1:

        skill = user.skills[index]
        #Decides whether to reset or continue streak
        if loss_gain == 0:
            skill.reset_streak()
            user.coins -= skill.penalty
            print("Streak reset...")
            print(f"You lost {skill.penalty} coins\nYou have {user.coins} remaining.")

            return
        elif loss_gain == 1:
            skill.continue_streak()
            user.coins += skill.reward
            print("Streak continued...")
            print(f"You gained {skill.penalty} coins!\nYou have {user.coins} remaining.")

            return
        else:
            print("Invalid response, choose between 0 and 1 to reset or continue streak.")
            return 
        
    else:
        print("Invalid response, choose between 0 and 1 for habit or skill")
        return


def add_skill(user,name, priority, del_prac):
    """"
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Create a new instance of a skill and add it to the user's attributes

    Args:
                user: The instance of the class "user"
                name: Name of the skill
                priority: priority of the skill
                del_prac: exercises for deliberate practice
    
    Return:
                None

    Time-Complexity: O(1)
    
    """

    skill = ob.skills(name,0,priority,del_prac)

    user.skills.append(skill)

def add_habit(user,name, priority):
    """"
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Create a new instance of a habit and add it to the user's attributes

    Args:
                user: The instance of the class "user"
                name: Name of the habit
                priority: priority of the habit
    
    Return:
                None
    
    Time-Complexity: O(1)
    
    """

    habit = ob.habit(name,0,priority)

    user.habits.append(habit)

def remove_skill(user,index):
    """"
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Removes a new instance of a skill from the user's attributes

    Args:
                user: Instance of the class "user"
                index: index of the item to be removed
    
    Return:
                None
    
    Time-Complexity: O(1)
                
    """

    user.skills.pop(index)

def remove_habit(user, index):
    """"
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Removes an instance of a habit from the user's attributes

    Args:
                user: The instance of the class "user"
                index: The index of the item to be removed
    
    Return:
                None
    
    Time-Complexity: O(1)
    
    """
    user.habits.pop(index)

########################
# Screens
########################

def go_main(user):
    """
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Displays the main screen message

    Args:
                User: The instance of the class "user"
    
    Returns:
                Integer

    Time-Complexity: O(n)
    
    """

    #Opening message
    print(f"Welcome {user.name},                Bank: {user.coins} [If you go bankrupt, system23.exe will be deleted]")
    print(f"Here are your goals for today:")

    #Displays challenges
    if user.skills:
        for i in range(len(user.skills)):
            exercises = user.skills[i].del_prac
            exercise = random.choice(exercises)

            print(f"{i}. {exercise}... Time remaining: {user.skills[i].priority}")
    else:
        print("[You are not working on any skills so far...]")
    
    #Displays options
    print("\nWhat would you like to do. Enter a number.")
    print("0. Update progress\n1. Add an item\n2. Remove an item\n3. Settings\n4. Exit")

    #Get response
    while True:
        try:
            response = int(input(""))
            return response
        except ValueError:
            print("Ensure you enter a numerical digit")

def go_update_progress(user):

    """
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Displays the screen to update a skill's progress

    Args:
                User: The instance of the class "user"
    
    Returns:
                None
    
    Time-Complexity: O(n)
    
    """
    print(50*"*")
    print("Update")
    print(50*"*")
    print("\n")

    #Displays skills and streak
    print("="*50)
    print("Skills")
    print("="*50)

    print("Name             Streaks")
    for i in range(len(user.skills)):
        print(f"{i}. {user.skills[i].name}          {user.skills[i].streak}")
    
    #Displays habit and streak
    print("\n")
    print("="*50)
    print("Habits")
    print("="*50)

    print("Name             Streaks")
    for i in range(len(user.habits)):
        print(f"{i}. {user.habits[i].name}          {user.habits[i].streak}")
    print("\n")
    return

def go_add_skill_or_habit():
    """
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Displays the screen to add a new item

    Args:
                None
    
    Returns:
                Integer
    
    Time-Complexity: O(1)
    
    """
    print(50*"*")
    print("Add page")
    print(50*"*")

    print("Do you want to add a skill or a habit? Enter a digit:")
    print("0. Habit\n1. Skill")
    response = int(input(""))
    return response

def go_remove_skill_or_habit(user):
    """
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Displays the screen to remove a new item

    Args:
                user: Instance of the class object "user"
    
    Returns:
                Integer
    
    Time-Complexity: O(n)
    
    """
    print(50*"*")
    print("Remove page")
    print(50*"*")

    print("Do you want to remove a skill or a habit? Enter a digit:")
    print("0. Habit\n1. Skill")
    response = int(input(""))

    #Displays all items and index depending on the input
    if response == 0:
        #Print all habits
        print("="*50)
        print("Habits")
        print("="*50)

        print("Name")
        for i in range(len(user.habits)):
            print(f"{i}. {user.habits[i].name}")

    elif response == 1:
        #Displays skills
        print("="*50)
        print("Skills")
        print("="*50)

        print("Name")
        for i in range(len(user.skills)):
            print(f"{i}. {user.skills[i].name}")
    
    #Select an item
    print("Select item. Enter a digit:")
    response = int(input(""))

    return response

def go_settings():
    """
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Displays the screen to change settings of the config file

    Args:
                None
    
    Returns:
                Integer

    Time-Complexity: O(1)
    
    """    
    print(50*"*")
    print("Settings")
    print(50*"*")

    print("0. Delete user data\n1.Go back to main")
    response = int(input(""))
    return response

def go_exit():
    """
    Author:     Nishal Joseph
    Date:       20/1/25
    Function:   Double check user wants to exit

    Args:
                None
    
    Returns:
                Integer
    
    Time-Complexity: O(1)
    
    """    
    print(50*"*")
    print("Exit")
    print(50*"*")

    print("Are you sure you want to exit?")
    print("0. Yes\n1. No")
    response = int(input(""))
    return response