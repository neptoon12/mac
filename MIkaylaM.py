import time
def mprint(num1,num2):
    print("****")
    print("  "+str(num1))
    print("+ "+str(num2))
    print("****")

numbers=[0,1,2,3,4,5,6,7,8,9,10]
Manswer=False
num=3
Cans=0

for i in range(4):#up to 10
    #non num eval
    while(True):
        try:
            mprint(num,i)
            Mnum=int(input("Please enter the answer: "))
            break
        except ValueError:
            print("That is not a number!!! please enter a valid number")
    if(num+i==Mnum):
        print("Good Job")
        Cans=Cans+1
        print()
    else:
        print("Incorrect!!")
        print()
        print(str(num)+"+"+str(i)+" is: "+str(num+i))
        print("__________")
        time.sleep(4)
        print()
    
    
    

    
