import random

#Difficulty Levels Function
def Difficulty(level,type):

    #Set Difficulty Levels
    num1 = []
    num2 = []
    if level == 1:
        num1 = [1,9]
        num2 = [1,9]
    else:
        num1 = [1,99]
        num2 = [1,99]

    #Use Numbers according to difficulty
    x = random.randint(num1[0],num1[1])
    y = random.randint(num2[1],num2[1])

    #Swap x and y for Divison and Subraction
    if (type == 2 or type == 4) and x < y:
        y,x = x,y
     
    return (x,y)


#Random Reply Function
def Reply(choice):

    #Dictonary for correct and wrong answers
    correct = ['Very good!','Nice work!','Keep up the good work!']
    wrong = ['No, Please try again.','Wrong. Try once more.','No, keep trying!']

    #Random Reply
    reply = random.randint(1,3)

    if choice:
        return correct[reply-1]
    else:
        return wrong[reply-1]


#Varying Types of Problems Function
def ProbType():
    print()
    print("1 = addition")
    print("2 = subraction")
    print("3 = multiplication")
    print("4 = divison")
    print("5 = mixed operations")
    
    #Users choice
    probtype = int(input("Enter the operation (1 to 5): "))
    return probtype

#Answer 
def Answer(n1,n2,t):

    #Difficult Possible Answers
    if t == 1:
        return n1 + n2
    elif t == 2:
        return n1 - n2
    elif t == 3:
        return n1*n2
    else:
        return n1//n2



#Pre Sets
numcorrect = 0
numwrong = 0
level = 1
probtype = 1
answer1 = 1

#Problem Type Symbol Dictionary
operation = ["+","-","*","//"]

#Chose Difficulty
level = int(input("Enter the difficulty leve(1/2): "))

#Run the program in loop
while answer1 != -1:
    probtype = ProbType()
    type = probtype
    if probtype == 5:

        type = random.randint(1,4)
        difficulty = Difficulty(level,type)
    else:
        type = probtype
        difficulty = Difficulty(level,type)



    print()
    answer1 = int(input("How much is {} {} {}?\nEnter your answer (-1 to exit): ".format(difficulty[0],operation[type-1],difficulty[1])))
    answer2 = Answer(difficulty[0],difficulty[1],type)

    #Stop if reply is -1 or Repeat if wrong answer
    if answer1 == -1:
        print("Number of correct answers: ",numcorrect)
        print("Number of wrong answers: ",numwrong)
        print("Thanks for playing!")
        break
    else:
        while answer1 != answer2:
            print(Reply(False))
            answer1 = int(input("How much is {} {} {}?\nEnter your answer (-1 to exit): ".format(difficulty[0],operation[type-1],difficulty[1])))
            numwrong += 1

        print(Reply(True))
        numcorrect += 1