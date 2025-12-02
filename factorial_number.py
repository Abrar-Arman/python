def factorial(num : int) -> int | None:
    if num<0:
        print(f"factorial does not exist for {num}")
        return None
    result=1
    for i in range(1,num+1):
             result*=i

    return result

print(factorial(-1))
print(factorial(2))
print(factorial(5))