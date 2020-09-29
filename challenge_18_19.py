#challenge 18
#function that takes three parameters  
#returns True only if they are all True and False otherwise.
def triple_and(a,b,c):
    x=[a,b,c]
    print(all(x))
    
triple_and(1,0,1)

#challenge 19
#function that takes one parameter(listofnumbers) 
#returns list with the numbers changed to strings
def convert(a):
    print([str(i) for i in a])
    
convert([1, 2, 3])
