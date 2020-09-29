#challenge 24
#function takes one parameter(+number)
#return after converting the number to a string and add commas as a thousands separator.
def format_number(pos):
    b=str(pos)
    x=[]
    y=[]
    re=0
    result=""
    for i in range(len(b)):
        x.append(b[len(b)-1-i])
        if i==re+2 and i<len(b)-1:
            x.append(",")
            re=re+3
    for k in range(len(x)):
        result=result+(x[(len(x)-1)-k])
    print(result)
format_number(1000000)


