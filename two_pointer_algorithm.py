#to find twosum problem
arr=[2,4,5,7,8]
h=1
t=12
l=0
r=len(arr)-1
while(l<r):
    asum=arr[l]+arr[r]
    if asum==t:
        print(l,r)
        h=0
        break
    elif asum<t:
        l+=1
    elif asum>t:
        r-=1
if h==1:
    print("no match found")
       