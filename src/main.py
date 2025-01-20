"""
Author:         Nishal Joseph
Date:           20/1/25
Description:    This is the main script that the user will interact with.
"""
######################
# Imports
import sys
sys.path.append('.src/') #Adding folder src

import common as co
import time
######################

def main():
    """
    Author:     Nishal Joseph 
    Date:       20/1/25
    Function:   This is the interactive menu that the user will be interacting with

    Args:
                None
    
    Returns:    
                None
    
    Time Complexity: O(n^2)
    """
    
    #Create the user
    file_dir = "src/config.txt"
    user = co.create_user(file_dir)

    #Loop of the main menu
    while True:
        main_response = co.go_main(user)

        #Branch off to different  pages
        if main_response == 0:
            #Display all items
            co.go_update_progress(user)

            #Habit or Skill
            print("Select option by entering a digit:")
            print("0. Habit")
            print("1. Skills")
            print("3. Return to menu")
            response = int(input(""))

            #Return to menu
            if response == 3:
                continue

            #Item's index
            print("Enter your item's number:")
            index = int(input(""))

            #Gain or loss
            print("Did you keep up your streak or no?")
            print("0. No :(")
            print("1. Yes :)")
            gainOrLose = int(input(""))

            #Update item based on response
            co.update_streak(user,gainOrLose,response,index)
            
        elif main_response == 1:
            #Habit or skill
            response = co.go_add_skill_or_habit()

            #Habit
            if response == 0:
                name = input("Name your habit:\n") #NAME

                print("Prioritise your item. Enter a number:") #PRIORITY
                print("1. Urgent\n2. Moderate\n3. Calm")
                priority = int(input(""))

                #Add
                co.add_habit(user,name,priority)

            #Skill
            elif response == 1:
                name = input("Name your skill:\n") #NAME

                print("Prioritise your item. Enter a number:") #PRIORITY
                print("1. Urgent\n2. Moderate\n3. Calm")
                priority = int(input(""))

                #EXERCISES
                print("Add some exercises for you to practice. Eg. Jog for 10 minutes\nPress enter to save each exercise\nType'Done' to finish. ")
                del_prac = []
                item = ""
                while True:
                    item = input("Enter: ").lower()
                    if item.strip().lower() == "done":
                        break
                    del_prac.append(item)
                
                #Creates skill
                co.add_skill(user,name,priority,del_prac)

        #Remove
        elif main_response == 2:
            co.go_update_progress(user)
            print("Select option by entering a number:")
            print("0. Habit")
            print("1. Skill")
            response = int(input(""))

            #Habit
            if response == 0:
                index = int(input("Enter the number of your item: "))
                co.remove_habit(user,index)
            
            #Skill
            elif response == 1:
                index = int(input("Enter the number of your item: "))
                co.remove_skill(user,index)

        #Settings
        elif main_response == 3:
            #Settings page
            response = co.go_settings()
            
            #Check if user data needs to be deleted
            if response == 0:
                #Change SETUP_CHECK to False
                try:

                    with open(file_dir,"w") as f:
                        f.write("SETUP_CHECK: False")
                
                except FileNotFoundError:
                    print("file not found :(")
            else:
                pass
        
        #Quitting
        elif main_response == 4:
            #Double checking
            response = co.go_exit()

            #Exiting the program
            if response == 0:
                co.save_user(file_dir=file_dir,user=user)
                print("User saved...")
                time.sleep(0.5)
                print("Exiting...")
                time.sleep(0.5)
                break
            #Cancelling exit
            else:
                print("Returning to menu...")


if __name__ == "__main__":
    main()