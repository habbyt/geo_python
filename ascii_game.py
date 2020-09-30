import random
import string
#user score starts at zero.
score=0
while score>-30:
#random selected alphabet
    letter=random.choice(string.ascii_uppercase)
#show to user and ask the ascii value
    print("what is the ASCII value for?", letter)
#get the value
    
    u_answer=int(input())
#check if it is  correct
    if u_answer==ord(letter):
#give score based on performance
        score=score+10
        print("your answer is correct")
    else:
        score=score-10
        print("your answer is incorrect! The ASCII value for",letter,"is",ord(letter))

    print("your total score is:",score)
print('Game Over')
    
