
#Rolling the dice
import random
min = 1
max = 6
global k
k=0
roll_again = "yes"
global b
while roll_again == "yes" or roll_again == "y":
    b=int(input("place your bet between 1-6 :  "))
    print ("Rolling the dices... ")
    a=random.randint(min, max)
    print ("The values is.... {}".format(a))
    print('/n')
    if b == a:
        print("YOU WIN")
        k=k+1
        print("your score is.....",k)
    else:
        print("YOU LOST")
        print("your score is ",k) 
    roll_again =input("Roll the dices again? ""yes""/no ")
print("YOUR TOTAL SCORE IS :-" ,k)
