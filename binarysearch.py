#get a sorted array
arr=[int(x) for x in input().split()]
front=0
last=len(arr)-1
target=5
while(front<=last):
    mid=(front+last)//2
    if target==arr[mid]:
        print(mid)
        break
    elif arr[mid]>target:
        last=mid-1
    else:
        front=mid+1
else:
    print("element not found")


