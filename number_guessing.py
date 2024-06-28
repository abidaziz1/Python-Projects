import random
import math
lower=int(input("Enter Lower Bound: "))
upper=int(input("Enter Upper Bound: "))
x= random.randint(lower,upper)
#print("Number is: ",x)
print("\n\tYou've only ",round(math.log(upper-lower+1,2))," chances to guess the integer!\n")
y=math.log(upper-lower+1,2)
count=0
while count<math.log(upper-lower+1,2):
    count+=1
    guess = int(input("Guess a number: "))
    if(x==guess):
        print("Congratulations! You found the number in ",count, " try. You beat 99% people!!")
    elif(x>guess):
        print("You guessed too low")
    elif(x<guess):
        print("You guessed too high")
if count>y:
        print("You've reached the maximum limit. Sorry you could not find the number!")
        print("The number is: %d"%x)
        print("\tBetter luck next time......")
