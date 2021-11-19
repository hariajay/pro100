cardno = input('Enter your 8digit card number: ')
length1 = len(cardno)

if length1 == 8:
    pinno = input("Enter your 4 digit pin: ")
elif length1 != 8:
    print('invalid card number')
    cardno = input('Enter your 8digit card number: ')

length2 = len(pinno)
if length2 == 4:
    withdrawl = input('Enter amount you want to withdrawl: ')
elif length2 != 4:
    print('invalid pin')
    pinno = input('Enter your 4digit pin: ')

class ATM:
    def __init__(self,withdrawl,money):
        self.withdraw = withdrawl
        self.money = money

cash = 20000
f = int(cash) + int(withdrawl)
person1 = ATM(f,cash)

print("Before: "+str(person1.money))
print("After: "+str(person1.withdraw))


    
