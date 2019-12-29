def ranpop():
    #import rando    #populate
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
import random
x=ranpop()
print(x)
        
