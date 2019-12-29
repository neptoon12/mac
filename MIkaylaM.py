import time
import random

def mprint(num1,num2):
    print("****")
    print("  "+str(num1))
    print("+ "+str(num2))
    print("****")
    
def ranpop():
    #import random
    #populate
    numbers=[]
    for x in range(11):
        numbers.append(x)
    print(numbers)
    #randomize
    ran=[]
    for i in range(len(numbers)):
        y=random.randint(0,len(numbers)-1)
        ran.append(numbers[y])
        numbers.pop(y)
        #print(numbers)
        #print(ran)
    return ran

Manswer=False
num=3
Cans=0
ran=ranpop()
print(ran)
for i in ran:
    #non num eval
    while(True):
        try:
            mprint(num,i)
            Mnum=int(input("Please enter the answer: "))
            break
        except ValueError:
            print("That is not a number!!! please enter a valid number")
    if(num+i==Mnum):
        print("Good Job!!!!")
        Cans=Cans+1
        print()
    else:
        print("Incorrect!!")
        print()
        print(str(num)+"+"+str(i)+" is: "+str(num+i))
        print("__________")
        time.sleep(4)
        print()
    
    
    

    
