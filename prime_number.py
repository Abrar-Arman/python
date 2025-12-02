
import math

def is_prime(number: int) -> bool:
    if number<=1:
        return False
    for i in range(2,int(math.sqrt(number)) + 1):
        if number%i ==0:
            return False
    return True
        
print(is_prime(3)) 
print(is_prime(8)) 
