#challenge 22
#function that takes 3 parameters(a number and 2 lists)
#return False if n is in both lists or in none of the lists and true otherwise
 
def list_xor(n,list1,list2):
    if n in list1 or n in list2:
        if n in list1 and n in list2:
            print(False)
        else:
            print(True)
    else:
        print(False)
            
    
list_xor(1, [1, 2, 3], [1, 5, 6])


#challenge 23
#function takes multiple parameters(unknown)
#return how many parameters are passed
def param_count(*param):
    print(len(param))

param_count(1,3,4,8)
