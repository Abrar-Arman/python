# Python Program to Read and write to a fi

with open('test.txt') as f:
    print(f.read())

# keep content
with open('test.txt','a') as f:
    f.write("write done")
# read
with open('test.txt') as f:
    print(f.read())

with open('test.txt','w') as f:
    f.write("write done")


