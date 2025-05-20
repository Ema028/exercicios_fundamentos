#1 with mergesort
from random import randint

def main():
    numbers = [randint(0,100) for i in range(20)]
    print(numbers)
    
    merge_sort(numbers)
    
    print(numbers)
    print(f" maior: {numbers[0]}, menor: {numbers[len(numbers) - 1]}")
    
def merge_sort(arr):
    n = len(arr)
    if (n > 1):
        middle = n//2
        l = n - middle
        r = n - l
        
        left = [0] * l
        right = [0] * r
        
        for i in range(l):
            left[i] = arr[i]
        for j in range(r):
            right[j] = arr[l + j]
            
        merge_sort(left)
        merge_sort(right)
        
        index = 0
        i = 0
        j = 0
        while (i < l and j < r):
            if (left[i] > right[j]):
                arr[index] = left[i]
                i += 1
                index += 1
            else:
                arr[index] = right[j]
                j += 1
                index += 1
                
        while (i < l):
            arr[index] = left[i]
            i += 1
            index += 1
                
        while(j < r):
            arr[index] = right[j]
            j += 1
            index += 1
                
main()

#2 
