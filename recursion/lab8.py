
def mylen(some_list):
    if some_list == []:
        return 0
    else:
        return 1 + mylen(some_list[1:])
    
def intDivision(dividend, divisor):
    if not isinstance(dividend,int) or not isinstance(divisor,int):
        raise Exception('Input should be integer')
    else:
        if divisor <= 0 or dividend < 0:
            raise ZeroDivisionError('divisor cannot be zero or negative')
        if dividend < divisor :
            return 0
        return 1 + intDivision(dividend - divisor, divisor)
    
def sumdigits(num):
    if not isinstance(num,int) or num < 0:
        raise Exception('the user does not provide a positive integer number.')
    if num == 0:
        return 0
    else:
        return num % 10 + sumdigits(num//10) # take mod first and plus the rest X0 digits mod 10        
        
def reverseDisplay(number):
    if not isinstance(number,int) or number < 0:
        raise Exception('the user does not provide a positive integer number.')    
    if number < 10:
        print(number)
    else:
        print(number % 10,end='') # the output will be in seperate line, so use end=
        reverseDisplay(number// 10)

def binary_search2(key,alist,lowerBound,upperBound):
    if lowerBound > upperBound: # finish the binary search
        return -1
    cut = (lowerBound + upperBound) // 2
    if key > alist[cut]: # then focus on the first half of the list
        index = binary_search2(key,alist,lowerBound,cut -1)
        if index == -1:
            return -1
        return index
    elif key == alist[cut]:
        return cut    # it is the index
    else: # then focus on the rest half of the list
        index = binary_search2(key,alist,cut +1, upperBound)
        if index == -1:
            return -1
        return index
    
    
def main():
    alist = [43, 76, 97, 86,1,1,1,1,1,14,1,1,1,1]
    print(mylen(alist))   
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', str(n), '//', str(m), '=' ,intDivision(n,m))
    number = int(input('Enter a number:'))
    print(sumdigits(number))
    number = int(input('Enter a number:'))
    reverseDisplay(number)
    some_list = [9,7,5,3,1,-2,-8]
    print(binary_search2(3,some_list,0,len(some_list)-1))
    print(binary_search2(-8,some_list,0,len(some_list)-1))
    print(binary_search2(4,some_list,0,len(some_list)-1))     
main()