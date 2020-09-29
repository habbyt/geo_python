#Challenge #2
#function takes a single string parameter and
#extract and return the middle letter
#If there is no middle letter,return the empty string
def mid(word):
    if len(word)%2==0:
        print("")
    else:
        x=int((len(word)+1)/2-1)
        print(word[x])
mid('abcde') 
