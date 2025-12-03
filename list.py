# Python Program to Remove Duplicate Element From a List

def remove_duplicate_from_list1(list_of_number: list[int]) -> list[int]:
    seen=set()
    for num in list_of_number:
        if num not in seen:
            seen.add(num)
    return list(seen)

my_list=[1,2,4,2,6,5,6]

print(remove_duplicate_from_list1(my_list),'using set')

# Python Program to Remove Duplicate Element From a List
def remove_duplicate_from_list2(list_of_number: list[int]) -> list[int]:
    list_of_number.sort()
    i=0
    result=[]
    while i < len(list_of_number) :
        if i==0 or  list_of_number[i] != list_of_number[i-1]:
            result.append(list_of_number[i])
        i+=1
    return result

my_list1=[1,2,4,2,6,5,6]
print(remove_duplicate_from_list2(my_list1))


# Python Program to Differentiate Between del, remove, and pop on a List
my_list=[1,2,3,6,7]

my_list.remove(2) # delete by value (first occurrence)
print(f"remove {my_list}")
deleted_element=my_list.pop(0) # delete by index return element delete
print(f"pop {my_list}")
del my_list[0] #delete by index not return element delete
print(f"del {my_list}")

# Python Program to Convert Two Lists Into a Dictionary both list have same length
def convert_list_to_dictionary(list1,list2):
    my_dict={}
    for i in range(len(list1)):
        my_dict[list1[i]]=list2[i]
    return my_dict

student_list=['abrar','Hour']
grade_list=[40,80]
print(convert_list_to_dictionary(student_list,grade_list), 'convert_list_to_dictionary')
# use Dictionary Comprehension
my_dict={student_list[i] :grade_list[i] for i in range(len(student_list))}
print(my_dict,"use Dictionary Comprehension")

# Python Program to Make a Flattened List from Nested List only work for one level nested
def flatten_list1(my_list: list[int | list[int]]) -> list[int]:
    flatten_list=[]
    for num in my_list:
        if type(num).__name__ == 'list':
            for x in num:
                flatten_list.append(x)

        else:
            flatten_list.append(num) 

    return  flatten_list

result=[]
def flatten_list2(my_list: list[int | list[int]]) -> list[int]:
    global result
    for num in my_list:
     if isinstance(num,list):
        flatten_list2(num)
     else:
         result.append(num)
    return result

list1=[1,4,[7,9],7,[3,6,9]]
print(flatten_list1(list1),'flatten list v1')
print(flatten_list2(list1),'flatten list v2 must reset resut after use')

# Python Program to Merge Two Lists and inverse the merged list 
def merge_list(list1: list[int],list2: list[int])-> list[int]:
    merged_list=[]
    i=0
    j=0
    while i < len(list1) or j <len(list2):
        if i < len(list1):
            merged_list.append(list1[i])
            i+=1
        if j < len(list2):
            merged_list.append(list2[j])
            j+=1
    return  merged_list
def invert_list(my_list: list[int]) -> list[int]:
    left=0
    right=len(my_list) - 1
    while left <right:
        temp=my_list[left]
        my_list[left]=my_list[right]
        my_list[right]=temp
        left+=1
        right-=1
    return my_list

first_list=[1,2,3]
second_list=[7,8,9]
print(merge_list(first_list,second_list),'merge list')
# or this
merged_list=first_list + second_list
print(merged_list,'merged_list')
# in place
print(invert_list(merged_list), "my function")




          

