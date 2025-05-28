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

#2 with bubble
from random import randint

def main():
    numbers = [randint(0,30) for i in range(20)]
    print(numbers)
    
    numbers = new_set(numbers)
    print(numbers)
    bubble_sort(numbers)
    
    print(numbers)
    
def new_set(arr):
    lista = []
    for i in range(len(arr)):
        if arr[i] not in lista:
            lista.append(arr[i])
    return lista
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for i in range(1, n):
            if (arr[i - 1] > arr[i]):
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
                
main()
#3 with selection
from random import randint
from math import inf

def main():
    numbers = [randint(0,100) for i in range(20)]
    print(numbers)
    
    selection_sort(numbers)
    n = len(numbers)//2
    
    if (n % 2 == 0):
        mediana = (numbers[n - 1] + numbers[n])/2
    else:
        mediana = numbers[n]
    
    print(numbers)
    print(mediana)
    
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = arr[i]
        index = i
        for j in range(i + 1, n):
            if (arr[j] < mini):
                mini = arr[j]
                index = j
        temp = arr[i]
        arr[i] = mini
        arr[index] = temp
main()

#7 with binary search
from random import randint

def main():
    numbers = [randint(-100,100) for i in range(15)]
    print(numbers)
    merge_sort(numbers)
    print(numbers)
    number = int(input("diga um número"))
    if binary_search(numbers, number):
        print("está na lista")
        return True
    print("não está")
    
def binary_search(arr, n):
    i = (len(arr) - 1) // 2
    while(arr[i] != n):
        if((i != 0 and arr[i] > n and arr[i - 1] < n) or (i != (len(arr) - 1) and arr[i] < n and arr[i + 1] > n)):
            return False
        if(arr[i] > n):
            i = i // 2
        else:
            i = i + (len(arr) - 1) // 2
    return True
    
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
            if (left[i] < right[j]):
                arr[index] = left[i]
                i += 1
                index += 1
            else:
                arr[index] = right[j]
                j += 1
                index += 1
                
        while (i < l):print(numbers)
            arr[index] = left[i]
            i += 1
            index += 1
                
        while(j < r):
            arr[index] = right[j]
            j += 1
            index += 1
                
main()
