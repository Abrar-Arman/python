# Python Program that calculates the difference in memory address in list objects
list1=[10,20,30]
list2=[40,50,60]
# use id method
list1_address=id(list1)
list2_address=id(list2)
print(f"list1 addresss {list1_address}, list2 address {list2_address}")
print(abs(list1_address - list2_address))
print(list1 == list2,'diffrent memory location ')

# python Program to read user input and print it
number=int(input("please enter number "))
print(number)