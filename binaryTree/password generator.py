
import random
import string
'''
pwList = []
pwLen = 18
for i in range(pwLen):
    myPW = random.choice(string.ascii_letters+string.digits)
    pwList.append(myPW)
    finalPW = ''.join(pwList)
print(finalPW)
'''

numList = ['1','2','3','4','5','6','7','8','9','0']

lowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

upperCase = []

symbols = ['~','!','@','#','$','%','^','&','*','(',')','-','+','=']
for i in lowerCase:
    upperCase.append(i.upper())

password = []
passLen = 20
currentLen = 0
while currentLen < passLen:
    aNum = random.choice(numList)
    currentLen += 1 
    numList.remove(aNum)
    lowerchar = random.choice(lowerCase)
    currentLen += 1
    lowerCase.remove(lowerchar)
    upperchar = random.choice(upperCase)
    currentLen += 1
    upperCase.remove(upperchar)
    syms = random.choice(symbols)
    currentLen += 1
    symbols.remove(syms)
    group = aNum + lowerchar + upperchar + syms
    password.append(group)

    
print(''.join(password))


'''
totalList = [numList,symbols,lowerCase,upperCase]
pwList = []
loop = 0
pwLength = 18
while loop < pwLength:
    ranSym = random.choice(totalList)
    if ranSym == totalList[0]:
        aNum = random.choice(numList)
        numList.remove(aNum)        
        loop += 1
        pwList.append(aNum)
        
    elif ranSym == symbols:
        aNum = random.choice(symbols)
        symbols.remove(aNum)        
        loop += 1
        pwList.append(aNum)
    elif ranSym == upperCase:
        aNum = random.choice(upperCase)
        upperCase.remove(aNum)        
        loop += 1
        pwList.append(aNum)
    elif ranSym == lowerCase:
        aNum = random.choice(lowerCase)
        lowerCase.remove(aNum)        
        loop += 1
        pwList.append(aNum)
newPassWord = ''.join(pwList)
print(newPassWord)
'''
'''
totalList = [numList,symbols,lowerCase,upperCase]
pwList = ['password: ']
loop = 0
pwLength = 19

while loop < pwLength:
    if len(totalList) == 0:
        totalList.append(numList)
        totalList.append(lowerCase)
        totalList.append(upperCase)
        totalList.append(symbols)
    ranSym = random.choice(totalList)
    if ranSym == totalList[0] and pwList[-1] not in ranSym:
        aNum = random.choice(totalList[0])
        totalList[0].remove(aNum)        
        loop += 1
        pwList.append(aNum)
        totalList.remove(totalList[0])
    elif ranSym == totalList[1] and pwList[-1] not in ranSym:
        aNum = random.choice(totalList[1])
        totalList[1].remove(aNum)        
        loop += 1
        pwList.append(aNum)
        totalList.remove(totalList[1])
    elif ranSym == totalList[2] and pwList[-1] not in ranSym:
        aNum = random.choice(totalList[2])
        totalList[2].remove(aNum)        
        loop += 1
        pwList.append(aNum)
        totalList.remove(totalList[2])
    elif ranSym == totalList[3] and pwList[-1] not in ranSym:
        aNum = random.choice(totalList[3])
        totalList[3].remove(aNum)        
        loop += 1
        pwList.append(aNum)
        totalList.remove(totalList[3])
        
newPassWord = ''.join(pwList)
print(newPassWord)
'''
'''
totalList = [numList,symbols,lowerCase,upperCase]
pwList = ['password: ']
loop = 0
pwLength = 19

def containPrevious(sym, cdList):
    if sym in cdList:
        return True
    else:
        return False
    
while loop < pwLength:
    ranSym = random.choice(totalList)
    aNum = random.choice(ranSym)
    if containPrevious(pwList[-1],) == True:
        continue
    else:
        ranSym.remove(aNum)        
        loop += 1
        pwList.append(aNum)
        
newPassWord = ''.join(pwList)
print(newPassWord)
'''