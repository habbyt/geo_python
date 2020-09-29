#Challenge #3
#function takes one parameter
#The parameter is a dictionary that maps names and online status
#return the number of people who are online
statuses= {"Alice":"online","Bob":"offline","Eve":"online"}
def online_count (statuses):
    x=0
    for i in statuses:
        if statuses[i]=="online":
            x+=1
    print(x)
