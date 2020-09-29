#challenge 12
#function takes one parameter(int)
#return true if its divided by 3 and false otherwise
def div_3(n):
    if n%3==0:
        print(True)
    else:
        print(False)
div_3(2455959)


#challenge 13
#function takes one parameter(string+int)
#returns its corresponding tuple from 2D list
def get_row_col(n):    
    c=n[0]
    r=n[1]
    if n[0]=='A':
        c=0    
    elif n[0]=='B':
        c=1
    else:
        c=2
    r=int(n[1])-1
    result=(r,c)
    print(result)
get_row_col('A3')
