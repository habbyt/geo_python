#challenge 16
#function takes one parameter(string)
#return the biggest number of consecutive zeros in the string

def consecutive_zeros(b):
    a=0
    m=[]
    if b.find('0')==-1:
        print(0)  
    elif b!='0':
        for i in range(len(b)-1):
            m.append(a+1)
            if b[i]=="0":
                if b[i]==b[i+1]:
                    a=a+1                
                else:
                    a=a*0
        print(max(m))
    else:
         print(1)
      
consecutive_zeros("0100101010")

#challenge 17
#function takes one parameter(list)
#return true if all elements are the same and false otherwise

def all_equal(a):
    if a==[]:
        print(True)
    else:
        result=[]
        x=a[0]
        for i in a:
            result.append(i==x)
        print(all(result))

all_equal([1,2,3])
