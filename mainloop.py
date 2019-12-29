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
    for x in range(11):#11 is 0 to 10 and produces 11 numbers
        numbers.append(x)
    #randomize
    ran=[]
    for i in range(len(numbers)):
        y=random.randint(0,len(numbers)-1)
        ran.append(numbers[y])
        numbers.pop(y)
        #print(numbers)
        #print(ran)
    return ran

print("***Welcome to the TT math test***")
print()
run=True
#mainloop
while(run):
    Cans=0#correct answers
    #handing non 0 loop
    print("What number are you practicing with?")
    #handing non 0 loop
    while(True):
        try:
            num=int(input("Please enter a number: "))
            break
        except ValueError:
            print("That is not a number!!! please enter a valid number")
    ran=ranpop()
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
    print("You have Completed the "+str(num)+" test!\n")
    print("You Got "+str(Cans)+" Correct")
    if (Cans==len(ran)):
        print("YOU GOT THEM ALL CORRECT!!!!!")
    else:
        print("Try to get them all right next time.\n")
    Continue=str(input("Would You like to continue?\n"))
    if (Continue=="n"):
        run=not run
    print("\n"*40)
    
    
    
#greetings
#take in number
#print question
#take in answer
#evaluate
#increment correct number
#loop
#print correct
