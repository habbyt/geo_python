#Challenge #6
#function takes one parameter(string)
#return true if there are two identical letters in a row in the string,
#and False otherwise. print(True) print(false)

word="helonowandthenmamm"
def double_letters(word):
    m=len(word)-1
    result=[]
    for i in range(m):
        if word[i]==word[i+1]:
            result.append(True)           
        else:
            result.append(False)
    if any(result)==True:
        print(True)
    else:
        print(False)

    
double_letters('dadnani')



#Challenge #7
#function #1 takes one parameter(string)
#returns word after adding "." in between each letter.
#function #2 takes one parameter(string)
#returns word after removing "." from in between each letter.



def add_dots(word):
    x=""
    for i in range(len(word)):
        if i!=len(word)-1:
            x=x+(word[i]+".")
        else:
            x=x+word[i]
    return x      
    
def remove_dots(word):
    y=""
    for i in range(len(word)):
        if word[i]!=".":
            y=y+word[i]
    print(y)

    
remove_dots(add_dots('abcde'))
    
    
