#----------------------------------------------------
# Lab 5, Exercise 1: Exceptions and inheritance
# Purpose of code:
#
# Author: Dexter Dai
# Collaborators/references:
#----------------------------------------------------



# Write your TransitionError class definition here.
class TransitionError(Exception):
    def __init__(self,beginning,final):     #This new method will have two parameters (besides the self parameter):beginning and final. 
        self.previousState = beginning      #Inside the method, you should assign beginning and final to the new attributes previousState and nextState, respectively.
        self.nextState = final              
        self.msg = "Not normal to transition from {} to {}".format(self.previousState,self.nextState)   # Inside the method, you will also create a third new attribute: msg
        
    def printMsg(self):                     #This class should have a new method called printMsg(). It simply prints the value of the msg attribute
        print(self.msg)
# It is derived from the Exception base class, but has 3 unique properties that 
# need to be initialized in a custom __init__ method:
#   self.previousState - state at beginning of transition
#   self.nextState - attempted state at end of transition
#   self.msg - message explaining why specific transition is not allowed
#   HINT for __init__: look to see how this exception is raised
# It also has one unique behaviour (i.e. method): printMsg()



# DO NOT CHANGE THIS growingOld FUNCTION
def growingOld(name, start, end): 
    '''
    Checks to see if a person grows old in the conventional way.
    Raises a custom exception if they do not.
    
    Inputs:
       name (str): Name of the person
       start (str): Stage that the person starts life
       end (str): Stage that the person ends life
    
    Returns: None
    '''
    print(name, 'started life as a(n)', start, 'and ended as a(n)', end)
    if start == 'adult':
        raise TransitionError(start, end)
    print('This is the transition we expect as people grow old')
    

# DO NOT CHANGE THIS main FUNCTION
def main():  
    '''
    Looks at two different people and how they grow old.
    Inputs: n/a
    Returns: None
    '''
    print('Checking first person...')
    try:
        person1 = ['Pebbles Flintstone', 'baby', 'adult']
        growingOld(person1[0], person1[1], person1[2])
    except TransitionError as myError:
        print('Transition error:', end = ' ')
        myError.printMsg() 
    except Exception:
        print('General error')
    
    print('\nChecking second person...')
    try:
        person2 = ['Benjamin Button', 'adult', 'baby']
        growingOld(person2[0], person2[1], person2[2])
    except TransitionError as myError:
        print('Transition error:', end = ' ')
        myError.printMsg() 
    except Exception:
        print('General error')  
        
    print('\nChecking second person again...')
    try:
        fictionalPerson = ['Benjamin Button', 'adult', 'baby']
        growingOld(realPerson[0], realPerson[1], realPerson[2])   # There is no realPerson list, so 'try' line will not be excecuted
    except Exception:
        print('General error')
    except TransitionError as myError:
        print('Transition error:', end = ' ')
        myError.printMsg()  
        
    print('\nGoodbye...')


if __name__ == '__main__':    
    main()
    