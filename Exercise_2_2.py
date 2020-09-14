#here are the months list and average temprature list
months=list(("January","February","March","April","May","June","July","August","September", "October", "November", "December"))
average_temp=list((-3.5,-4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, 11.5, 6.0, 2.0, -1.5))
#input desired month
selected_month_index= int(input("type the month in number to see its monthly average temperature : "))
#check if the input is correct(in range 1-12)
#for loop to go through the list 'i' is just and index
#if statement to check if the input is equal to the index
if selected_month_index<=12 and selected_month_index>0:
    for i in range(12):
        if i!=selected_month_index:
            continue
# Using the lists and their indices, generate the desired print statement:
        print_statement ="The average temperature in Helsinki in "+ months[i-1]+ " is " + str(average_temp[i-1])
        print(print_statement)
else:
    print("incorrect input")
#Validate the length of two lists are 12
assert len(months) == 12, 'Wrong length!'
assert len(average_temp) == 12, 'Wrong length!'
#Validate that variable months and average_temp are lists
assert isinstance(months, list), 'Variable months is not a list'
assert isinstance(average_temp, list), 'Variable average_temp is not a list'
#Validate the print statement is correct;
# Set selected_month_index to correspond with July before running this cell.
assert print_statement == 'The average temperature in Helsinki in July is 18.0'
