"""
Author:         Nishal Joseph
Last Modified:  17/1/25
Description:    This file contains the definition of the classes involved in this project. This includes a
                a class for the user, desired habits and desired skills. It will keep track of the progress
                and any details related to each instance.
"""

class user:
    """
    Purpose:    To keep an instance of the user active so that experience can be personalised

    Last Modified:
                17/1/25

    Attributes:
                name: Name of the user
                habits: A list of habits to keep track of
                skills: A list of skills to keep track of
                coins: Number of coins the user has
    Methods:
                add_skill(newSkill): Appends a new skill to the list of stored skills
                add_habits(newHabits): Appends a new habit to the list of stored habits
                remove_skill(position): Removes the specified item from being stored
                remove_habit(position): Removes the specified item from being stored
    Use Case:
                object = user(name,habits,skills)
                object.add_skill(guitar)
    """
    
    def __init__(self, name, habits, skills, coins):
        """
        Function:   Initialises all the user details so that experience can be personalised.

        Args:       
                    name: Name of the user (string)
                    habits: List of desired habits to keep track of
                    skills: List of skills to keep track of
        Returns:
                    None
        """

        self.name = name
        self.habits = habits
        self.skills = skills
        self.coins = coins
    
    def add_skill(self, newSkill):
        """
        Function:   Adds a new skill to the user data to keep track of

        Args:       newSkill: An instance of the new skill and all details

        Returns:
                    None
        """
        self.skills.append(newSkill)
    
    def add_habit(self, newHabit):
        """
        Function:   Adds a new habit to the user data to keep track of

        Args:       newHabit: An instance of the new skill and all details

        Returns:
                    None
        """
        self.habits.append(newHabit)

    def remove_skill(self,position):
        """
        Function:   Removes a skill from being tracked

        Args:       position: The index of the item on the list

        Returns:
                    None
        """
        self.skills.pop(position)

    def remove_habit(self,position):
        """
        Function:   Removes a habit from being tracked

        Args:       position: The index of the item on the list

        Returns:
                    None
        """
        self.habits.pop(position)


class habit:
    """
    Purpose:    An instance of a specific habit with information about progress stored as attributes

    Last Modified:
                18/1/25
    
    Attributes:
                streak: Number of consistent days
                penalty: Cost if not completed
                reward: Reward once completed
    
    Methods:
                continue_streak(): Adds to the streak count
                reset_streak(): Resets streak to be 0

    Use case:
            habit = habit(newHabit, 1)
    """

    def __init__(self,name, streak, priority):
        """
        Function:   Initialises with the name of the habit and all data reset.

        Args:       
                    name: name of the habit (string)
        Returns:
                    None
        """

        #Initilises the name and sets the streak
        self.name = name
        self.streak = streak

        #Defines penalty and reward based on priority
        if priority == 1:

            self.penalty = 100
            self.reward = 20

        elif priority == 2:

            self.penalty = 50
            self.reward = 10

        elif priority == 3:

            self.penalty = 25
            self.reward = 5
    
    def continue_streak(self):
        """
        Function:  Adds to the streak so far by 1.

        Args:       
                    None
        Returns:
                    None
        """
        self.streak += 1
    
    def reset_streak(self):
        """
        Function:  Resets the streak back to zero

        Args:       
                    None
        Returns:
                    None
        """
        self.streak = 0




class skills:
    """
    Purpose:    An instance of a specific skill with information about progress stored as attributes

    Last Modified:
                18/1/25
    
    Attributes:
                streak: Number of consistent days
                deliberate_pract: Deliberate practice that needs to be blocked off   

    
    Methods:
                continue_streak():  Adds to the streak count
                reset_streak():     Resets streak to be 0
                add_practice()      Adds an exercise to the deliberate practice related to skill

    """
    def __init__(self,name, streak, priority, del_prac):
        """
        Function:   Initialises with the name of the habit and all data reset.

        Args:       
                    name: name of the habit (string)
                    streak: The number of streak so far
                    priority: level of importance and energy to give, range of 1 to 3
                    del_prac: The list of practices saved
        Returns:
                    None
        """

        #Initialises predetermined constants
        self.name = name
        self.streak = streak

        #Choose penalty and reward based on priority
        if priority == 1:

            self.penalty = 100
            self.reward = 20

        elif priority == 2:

            self.penalty = 50
            self.reward = 10
            
        elif priority == 3:

            self.penalty = 25
            self.reward = 5
    
    def continue_streak(self):
        """
        Function:  Adds to the streak so far by 1.

        Args:       
                    None
        Returns:
                    None
        """
        self.streak += 1
    
    def reset_streak(self):
        """
        Function:  Resets the streak back to zero

        Args:       
                    None
        Returns:
                    None
        """
        self.streak = 0
