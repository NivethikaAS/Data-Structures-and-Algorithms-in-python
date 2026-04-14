import random
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=random.choice(arr)
    left=[i for i in arr if i<pivot]
    right=[i for i in arr if i>pivot]
    middle=[i for i in arr if i==pivot]
    return quicksort(left)+middle+quicksort(right)
arr=[3,6,2,8,9,5,4,3,1]
print(quicksort(arr))