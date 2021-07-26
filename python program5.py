#Create a list that stores the employee name ,their age,position and when they joined in the company
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266] 



#create a class Dog 
class Dog:
# Class attribute
   species = "Canis familiaris"
   def __init__(self, name, age):#Define a constructor
#Assign self.name=name
        self.name = name
#Assign self.age=age
        self.age = age



#Raising error due to assigning values to name and age      
 class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
#Instance method
#create a class
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instance method

    def description(self):

        return f"{self.name} is {self.age} years old"

# Another instance method

    def speak(self, sound):

        return f"{self.name} says {sound}" 
        
        
#create a list oblect
  names = ["Fletcher", "David", "Dan"]
 print(names)
#output['Fletcher', 'David', 'Dan']  




#print the miles object
print(miles)
#output is looking a crptic message <__main__.Dog object at 0x00aeff70>


#change the name of  dog's class
class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
  miles = Dog("Miles", 4)
print(miles)
#output'Miles is 4 years old'   


#Inherit from other class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed #adding breed
#Initiating a different kinds of dogs
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
 jack = Dog("Jack", 3, "Bulldog")
 jim = Dog("Jim", 5, "Bulldog")
 
 
 #Definition of dog class
 #Parent class
 class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
#Child class
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
#Initiate   some dogs of specific breed
miles = JackRussellTerrier("Miles", 4)
 buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
 jim = Bulldog("Jim", 5)
    
        


#Extend the Functionality of a Parent Class
#override a method
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
        
miles = JackRussellTerrier("Miles", 4)
 miles.speak()#calling the instance without passing the argument
#output'Miles says Arf'

#super() :  access the parent class from inside a method of a child class 
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
miles = JackRussellTerrier("Miles", 4)
miles.speak()
#'Miles barks: Arf'








#Tic-Tac-Toe Program 
# importing all necessary libraries 
import numpy as np 
import random 
from time import sleep 
# Creates an empty board 
def create_board(): 
  return(np.array([[0, 0, 0], 
                     [0, 0, 0], 
                     [0, 0, 0]]))   
# Check for empty places on board 
def possibility(board): 
    l = []      
    for i in range(len(board)): 
        for j in range(len(board)):              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l)   
# Select a random place for the player 
def random_place(board, player): 
    selection = possibility(board) 
    current_loc = random.choice(selection) 
    board[current_loc] = player 
    return(board)   
# Checks whether the player has three  of their marks in a horizontal row 
def row_win(board, player): 
    for x in range(len(board)): 
    win = True          
        for y in range(len(board)): 
            if board[x, y] != player: 
                win = False
                continue                 
        if win == True: 
            return(win) 
    return(win)   
# Checks whether the player has three of their marks in a vertical row 
def col_win(board, player): 
    for x in range(len(board)): 
        win = True          
        for y in range(len(board)): 
            if board[y][x] != player: 
                win = False
                continue                  
        if win == True: 
            return(win) 
    return(win)   
# Checks whether the player has three of their marks in a diagonal row 
def diag_win(board, player): 
    win = True
    y = 0
    for x in range(len(board)): 
        if board[x, x] != player: 
            win = False
    if win: 
        return win 
    win = True
    if win: 
        for x in range(len(board)): 
            y = len(board) - 1 - x 
            if board[x, y] != player: 
                win = False
    return win   
# Evaluates whether there is 
# a winner or a tie  
def evaluate(board): 
    winner = 0     
    for player in [1, 2]: 
        if (row_win(board, player) or
            col_win(board,player) or 
            diag_win(board,player)):                 
            winner = player               
    if np.all(board != 0) and winner == 0: 
        winner = -1
    return winner   
# Main function to start the game 
def play_game(): 
    board, winner, counter = create_board(), 0, 1
    print(board) 
    sleep(2)      
    while winner == 0: 
        for player in [1, 2]: 
            board = random_place(board, player) 
            print("Board after " + str(counter) + " move") 
            print(board) 
            sleep(2) 
            counter += 1
            winner = evaluate(board) 
            if winner != 0: 
                break
    return(winner)   
# Driver Code 
print("Winner is: " + str(play_game())) 














        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
