#----------------------------------------------------
# Lab 4, Exercise 2: Web browser simulator
# Purpose of code: simulate the website
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    userInput = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
    if userInput not in ['=','<','>','q']:
        print('Invalid entry')
    else:
        return userInput        
def goToNewSite(current, bck, fwd):
    newSite = input('URL: ' ) #let user
    bck.push(current) #append a new website
    return newSite
    
def goBack(current, bck, fwd):
    try:
        newSite = bck.pop() #default delete the last one
        fwd.push(current) #append a new website
        return newSite
    except:
        print("Cannot go back.")
        return current
def goForward(current, bck, fwd):   
    try:
        website = fwd.pop() #default delete the last one
        bck.push(current) #append a new website
        return website              
    except:
        print("Cannot go forward.")
        return current         
def main():
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    current = HOME
    quit = False
    while not quit:
        print('\nCurrently viewing', current)
        action = getAction()
        
        if action == '=':         
            current = goToNewSite(current, back, forward)
        elif action == '<':
            current = goBack(current, back, forward)
        elif action == '>':
            current = goForward(current, back, forward)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    