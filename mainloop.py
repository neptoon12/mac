import time
import random
def mprint(num1,num2):
    print("****")
    print("  "+str(num1))
    print(str(sign)+" "+str(num2))
    print("****")
    
def ranpop(default,rangefloor):
    #populate
    numbers=[]
    for x in range(rangefloor,default+1):#inclusive of rangefloor exclusive default+1
        numbers.append(x)
    #randomize
    ran=[]
    for i in range(len(numbers)):
        y=random.randint(0,len(numbers)-1)#picks random thing from numbers to put in ran
        ran.append(numbers[y])
        numbers.pop(y)
        #print(numbers)
        #print(ran)
    return ran

#CFlag=True# Choice or normal flag

print("***Hello Mikayla, Welcome to the TT math test***")
print()
run=True
#mainloop
while(run):
    Flag=False# true for doubles # modify structure for future use
    SFlag=False
    sign="+"
    Cans=0#correct answers
    #handing non 0 loop
    print("What number are you practicing with?")
    #handing non 0 loop
    while(True):
        try:
            num=input("Please enter a number: ")
            if (num=="D"):#for doubles #add HERE FOR FUTURE MODES
               print("You Have entered Doubles Mode")
               Flag=True
               break
            if (num=="S"):#for subtraction #add HERE FOR FUTURE MODES
               print("You Have entered Subtraction Mode")
               SFlag=True
               break
            num=int(num)
            break
        except ValueError:
            print("That is not a number!!! please enter a valid number")
    #Essentially Number of Questions
    while(True):
        try:
            tlength=int(input("How High would you Like to go: "))
            break
        except ValueError:
            print("That is not a number!!! please enter a valid number")
    #Lowest Feature
    while(True):
        try:
            lowest=int(input("How Low would you Like to go: "))
            if(lowest>=tlength):
                print("\nLowest must be LESS than your Highest\n")
                continue
            break
        except ValueError:
            print("That is not a number!!! please enter a valid number")
    
    ran=ranpop(tlength,lowest)
    #print(ran)
    for i in ran:
        #non num eval
        while(True):
            try:
                if(Flag):#signal nonstandard FOR DOubles
                    num=int(i)
                if(SFlag):#signal subtraction
                    num=int(tlength)
                    sign="-"
                mprint(num,i)
                Mnum=int(input("Please enter the answer: "))
                break
            except ValueError:
                print("That is not a number!!! please enter a valid number")
        #for adding
        if(not SFlag):
            if(num+i==Mnum):
                print("Good Job Mikayla!!!!")
                Cans=Cans+1
                print()
            else:
                print("Incorrect!!!")
                print()
                print(str(num)+"+"+str(i)+" is: "+str(num+i))
                print("__________")
                time.sleep(4)
                print()
        #for subtracting
        if(SFlag):
            if(num-i==Mnum):
                print("Good Job Mikayla!!!!")
                Cans=Cans+1
                print()
            else:
                print("Incorrect!!!")
                print()
                print(str(num)+"-"+str(i)+" is: "+str(num-i))
                print("__________")
                time.sleep(4)
                print()
    print("Mikayla Completed the test!\n")
    print("You Got "+str(Cans)+" out of "+str((tlength+1)-lowest)+" Correct")
    if (Cans==len(ran)):
        print("GREAT JOB MIKAYLA! YOU GOT THEM ALL CORRECT!!!!!")
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
