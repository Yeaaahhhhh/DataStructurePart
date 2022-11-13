#******************
# Lab 9: Exercise 2
# Author: Dexter
# Collaborators/References:
#******************
import math

class Student():
    def __init__(self, idNum, name, mark):
        '''Initialize the object properties'''
        self.__id = idNum
        self.__name = name
        self.__mark = mark
	
    def getMark(self):
        '''Returns the value of the Student's mark'''
        return self.__mark    

    def __str__(self):
        '''Informal string representation of Student'''
        return ' - {}, {}, {}'.format(self.__id, self.__name, self.__mark)

    def __lt__(self, anotherStudent):
        ''' 
        Checks if the mark of the student is less than the mark of another 
        Student object
        Input: anotherStudent (Student)
        Returns: boolean
	'''
        # TODO - remove the pass and complete the function
        if self.getMark() >= anotherStudent.getMark():
            return False
        else:
            return True



def recursive_merge_sort(data):  
    '''
    Uses MergeSort to sort the list of data in INCREASING order
    Returns: the sorted list of Students  
    '''
    # TODO - remove the pass and complete the function
    # Hint: modify your merge sort from exercise 1
    dataLen = len(data)
    if not dataLen > 1:
        return data
    else:
        midNum = dataLen // 2
        left = recursive_merge_sort(data[:midNum])
        right = recursive_merge_sort(data[midNum:])
        return mergeThem(left, right)

def mergeThem(left, right):
    stuList = []
    leftF = 0
    rightF = 0
    leftLen = len(left)
    rightLen = len(right)
    while not leftF >= leftLen and not rightF >= rightLen:
        if left[leftF].__lt__(right[rightF]):
            stuList.append(left[leftF])
            leftF += 1
        else:
            stuList.append(right[rightF])
            rightF += 1
    while not leftF >= leftLen:  # make sure the rest of (every element in the original list) elements appended
        stuList.append(left[leftF])
        leftF += 1
    while not rightF >= rightLen:
        stuList.append(right[rightF])
        rightF += 1
    return stuList
    


if  __name__== "__main__":
    # Read the data
    students_file = open('student_list.txt', 'r')
    students_data = students_file.readlines()
    student_list = []
    
    # Create a Student object corresponding to each line in input file
    for student in students_data:
        fields = student.split(', ')
        ID = fields[0]
        name = fields[1]
        mark = fields[2]
        student_list.append(Student(ID, name, int(mark)))

    # Print the original data
    print('Original data:')
    for student in student_list:
        print(student)

    # Sort the students
    sorted_students = recursive_merge_sort(student_list)

    # Print the sorted data
    print('Sorted data:')
    for student in sorted_students:
        print(student)
