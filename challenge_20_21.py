#challenge 20
#function that takes 2 parameters(lists)
#return a list of tuples. 
#each tuple should contain one item form each input list 
def zap(a,b):
    result=[]
    for i in range(len(a)):
        result.append((a[i],b[i]))
    print(result)    zap([0, 1, 2, 3],[5, 6, 7, 8])

    
#challenge 21
#function that takes 1 parameter(function as a string)
#return a true if conditions are met. 
def validate(c):
    if c.find('def')==-1:
        print("missing def")
    elif c.find(':')==-1:
        print("missing :")
    elif c.find('(')==-1 or c.find(')')==-1 :
        print("missing paren")
    elif c.find('()')!=-1 and c.find('"()"')==-1 :
        print("missing param")
    elif c.find('    ')==-1:
        print("missing indent")
    elif c.find('validate')==-1:
        print("wrong name")
    elif c.find('return')==-1:
        print("missing return")
    else:
        print(True)
validate('\r\n#challenge 21\r\n#function that takes 1 parameter(function as a string)\r\n#return a true if conditions are met. \r\ndef validate(c):\r\n if c.find("def")==-1:\r\n return "missing def"\r\n elif c.find(\':\')==-1:\r\n return "missing :"\r\n elif c.find(\'(\')==-1 or c.find(\')\')==-1 :\r\n return "missing paren"\r\n elif c.find("()")!=-1:\r\n return "missing param"\r\n elif c.find(\' \')==-1:\r\n return "missing indent"\r\n elif c.find(\'validate\')==-1:\r\n return "wrong name"\r\n elif c.find(\'return\')==-1:\r\n return "missing return"\r\n else:\r\n return True') 
#validate('def foo():\n print(123)')

        #conditions
#the code must contain the def keyword
#otherwise return "missing def"
#the code must contain the : symbol
#otherwise return "missing :"

#the code must contain ( and ) for the parameter list
#otherwise return "missing paren"

#the code must not contain ()
#otherwise return "missing param"

#the code must contain four spaces for indentation
#otherwise return "missing indent"

#the code must contain validate
#otherwise return "wrong name"

#the code must contain a return statement
#otherwise return "missing return"
