#Challenge #4
#function takes no parameter
#generate a random integer between 1 and 100 both inclusive
#return numbers
import random 
def random_number():
    print(random.randint(1,101))

#random_number()


#Challenge #5
#function that takes two parameters
#return True if both parameters are integers, and False otherwise.
def only_ints(a,b):
    if type(a)==int and type(b)==int:
        return True
    else:
        return False
only_ints(3,4)
