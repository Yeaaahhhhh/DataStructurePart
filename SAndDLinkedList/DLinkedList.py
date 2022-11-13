#----------------------------------------------------
# Lab 7, Exercise 2: Doubly Linked Lists
# TO DO: complete mandatory methods in DLinkedList class
# TO DO (optional): complete optional methods in DLinkedList class
# to get better understanding of manipulating linked lists
#
# Author: 
# Collaborators/references:Xinqi Zhou, a 2nd year CE student
#   - CMPUT 175 provided complete DLinkedListNode
#   - CMPUT 175 provided init, search, index methods for DLinkedList
#   - CMPUT 175 provided tests for DLinkedList
#----------------------------------------------------


class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious

class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
        
    def insert(self, pos, item):
        # TODO: mandatory
        
        assert isinstance(pos,int), 'Error:pos should be type int'
        assert pos >= 0, 'Error: pos should be a positive number (or zero)'
        if pos == 0:      #insert from head
            newNode = DLinkedListNode(item, self.__head, None)
        elif pos == self.__size:  # insert from end
            newNode = DLinkedListNode(item, None, self.__tail)
        else:
            if pos > 0 and pos < self.__size:# insert between head and end 
                index = 0
                current = self.__head
                while current != None:
                    if index == pos:
                        break
                    else:
                        current = current.getNext()
                        index += 1
            newNode = DLinkedListNode(item, current, current.getPrevious())
        if self.__size == 0:
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
        else:
            if pos == 0:
                self.__head = newNode
                self.__size += 1  
            elif pos == self.__size:
                self.__tail = newNode
                self.__size += 1            
        
    def searchLarger(self, item):
        # TODO: mandatory
        current = self.__head               # THIS  part is a combination of search method and index method
        found = False
        index = 0
        while current != None and not found:
            if current.getData() > item: #check if it is greater
                found = True
            else:
                current = current.getNext()
                index = index +1
        if not found:
            index = -1
        return index
    
    def getSize(self):
        # TODO: mandatory
        assert self.__size >= 0, 'the size is out of range'
        return self.__size
    
    def getItem(self, pos):
        # TODO: mandatory  
        assert isinstance(pos,int),'position must be an integer'
        if pos > self.__size:
            raise Exception("The position is outside of the list")
        if pos >= 0:
            index = 0
            current = self.__head
            while current != None:
                if index != pos:
                    current = current.getNext()
                    index += 1
                else:
                    return current.getData()
                   
        else:
            index = -1
            current = self.__tail
            while current != None:
                if index == pos:
                    return current.getData()
                else:
                    current = current.getPrevious()
                    index -= 1
        
    def __str__(self):
        # TODO: mandatory  
        s = ""
        current = self.__head
        while current != None:
            s += str(current.getData())+" "  # for the int_list test, change int to str
            current = current.getNext()
        s = s[:-1]
        return s



    def add(self, item):
        # optional exercise
        pass
        
    def remove(self, item):
        # optional exercise
        pass
        
    def append(self, item):
        # optional exercise
        pass
        
    def pop1(self):
        # optional exercise
        pass
    
    def pop(self, pos=None):
        # optional exercise
        # Hint - incorporate pop1 when no pos argument is given
        pass
        
    

def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.insert(0, "Hello")
    linked_list.insert(1, "World")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    '''
    OPTIONAL TESTS FOR OPTIONAL EXERCISE - do not need to demo
    '''
    '''
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
    '''
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(9, -1, -1):
        int_list.insert(0,i)      
    is_pass = (int_list.getSize() == 10)
    assert is_pass == True, "fail the test"            
            
    is_pass = (int_list.searchLarger(8) == 9)
    assert is_pass == True, "fail the test"
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
                  
    is_pass = (int_list.getItem(-1) == 9)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 801)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")
                
if __name__ == '__main__':
    test()
