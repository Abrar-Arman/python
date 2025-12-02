import random as ran

# generate random integer both include
random_int1=ran.randint(1,9)

# generate random integer 9 not include
random_int2=ran.randrange(1,9)

# generate random float
random_float=ran.random() 

# choosing random element from list
my_number=[2,6,9]
my_random_number=ran.choice(my_number)

# test
print(random_int1)
print(random_int2)
print(random_float)
print(my_random_number)