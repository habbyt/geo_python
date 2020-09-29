
#challenge 14
#function takes one parameter(string)
#return true if it is same when read backwards and false otherwise
def palindrome(word):
    x=len(word)-1
    result=[]
    for i in range(len(word)):
        if word[i]==word[x]:
            x=x-1
            result.append(True)
        else:
            result.append(False)
    print(all(result))
palindrome("abbMa")


#challenge 15
#function takes one parameter(number)
#return tuple containing number 1 lower and 1 higher than the number

def up_down(n):
    tup=(n-1,n+1)
    print(tup)

up_down(56)
