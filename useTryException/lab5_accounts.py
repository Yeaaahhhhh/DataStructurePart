#----------------------------------------------------
# Lab 5, Exercise 2:
# Purpose of code:display transactions of each client
# Author: Dexter Dai
# Collaborators/references:
#----------------------------------------------------
def readAccounts(infile):
    global dic
    dic = {}
    for line in open(infile):
        dicList = line.split(">")
        name = dicList[0]
        money = dicList[1]
        try:
            money = money.strip()
            if money == float(money):
                raise ValueError
            else:
                dic[name] = float(money)
        except ValueError:
            print('Warning! Account for '+ name +' not added: illegal value for balance')
    return dic

def processAccounts(accounts):
    acName = input("Enter account name, or 'Stop' to exit:")
    if acName != 'Stop':
        try:
            if acName in accounts:
                try:
                    transaction = float(input('Enter transaction amount for ' + acName + ':'))
                    if transaction < 0:
                        if abs(transaction) > accounts[acName]:
                            print('You are so poor, the transaction cannot be made')
                        else:
                            accounts[acName] += transaction
                            print('New balance for account ' + acName + ': ' + str(accounts[acName]))
                    else:
                        accounts[acName] += transaction
                        print('New balance for account ' + acName + ': ' + str(accounts[acName]))
                except ValueError:
                    print('Warning! Incorrect amount. Transaction cancelled')
            else:
                raise KeyError
        except KeyError:
            print('Warning! Account for ' + acName + ' does not exist. Transaction cancelled')
        processAccounts(accounts)
    else:
        print('Exiting program...goodbye.')      

def main():
    file= input('Enter filename > ')
    try:  
        readAccounts(file)
        processAccounts(dic)
    except OSError:
        print('File error:'+ file +' does not exist. \nExiting program...goodbye.')
main()