#Challenge #8
#function takes one parameter(string)
#return true if there are two identical letters in a row in the string,
#and False otherwise. print(True) print(false)


def count(word):
    for i in word:
        x=word.count("-")
    print(x+1)
    

count("min-a-tor")


#Challenge #9
#function takes tro parameter(strings)
#return true if word 1 can make word 2 rearranging the letters.
#and False otherwise.
#def is_anagram(word1,word2):    
word1="worred"
word2="drrowt"
def is_anagram(word1,word2):
    w1={}
    w2={}
    x=[]
    if len(word1)==len(word2):
        for i in range(len(word1)):
            w1[word1[i]]=word2.count(word1[i])
            w2[word2[i]]=word1.count(word2[i])
        for i in w1:
            if w1.get(i)==w2.get(i):
                x.append(True)
            else:
                x.append(False)
        print(all(x))
    else:
        print(False)
    
is_anagram("worrd", "drrow")
