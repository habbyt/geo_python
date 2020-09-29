#challenge 10
#function takes one parameter(listoflists)
#return a one dimensional list containing ites of listoflists

def flatten(to_flat):
    x=[]
    for i in to_flat:
        x.extend(i)
    print(x)
flatten([[1, 2], [3, 4]])
#challenge 11
#function takes one parameter(listofnumbers)
#return difference of the max and min number in the list

def largest_difference(num_list):
    print(max(num_list)-min(num_list))
    
largest_difference([1, 2, 3])
