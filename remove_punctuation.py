text=input("Enter String")
punctuations = set("!()-[]{};:'\"\\,<>./?@#$%^&*_~")
result=''
for char in text:
    if char not in punctuations:
        result+=char

print(result)