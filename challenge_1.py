#Challenge #1
#function takes a single string parameter and
#return a list of all the indexes in the string that have capital letters.
def capital_indexes(word):
    word="HeLlO"
    x=[]
    for i in range(len(word)):
        if word[i].isupper()==True:
            x.append(i)
    return x
