while(True):
    print("please enter a number")
    try:
        num=int(input("What number are you practicing: "))
    except ValueError:
        print("That is not a number!!! please enter a valid number")
    #print(isinstance(num,int))
