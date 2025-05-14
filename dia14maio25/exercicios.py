#1
from random import randint
from math import inf

nums = [randint(1,100) for i in range(20)]

menor = float('inf')
menor2 = float('inf')

for num in nums:
    if(menor > num):
        menor2 = menor
        menor = num
    elif(menor2 > num and num != menor):
        menor2 = num
    else:
        pass
        
print(nums)
print(f"o menor é {menor} e o segundo menor é {menor2}")

#1
from random import randint

nums = [randint(1,100) for i in range(20)]
maior = 0
maior2 = 0

for num in nums:
    if(maior < num):
        maior2 = maior
        maior = num
    elif(maior2 < num and num != maior):
        maior2 = num
    else:
        pass
        
print(nums)
print(f"o maior é {maior} e o segundo maior é {maior2}")