# Python Program to Delete an Element From a Dictionary if it exist
def delete_key(dict,key):
    if key in dict:
        print("delete done")
        return  dict.pop(key)
    else:
        print(f" {key} key not found")

my_dict={"a":7,"b":2,"c":1}
print(delete_key(my_dict,"a"))
print(delete_key(my_dict,"a"))

# Python Program to Merge Two Dictionaries
def merge_dict(dict1,dict2):
    merged_dict={}
    for key1 in dict1.keys():
         merged_dict[key1]=dict1[key1]
    for key2 in dict2.keys():
         merged_dict[key2]=dict2[key2]
    return merged_dict

dict1={"a":7,"b":1}
dict2={"c":7,"d":1}
print(merge_dict(dict1,dict2),'my function')
merged_dict={**dict1,**dict2}
print(merged_dict,"using unpack")
dict1.update(dict2) 
print(dict1,'use update')
