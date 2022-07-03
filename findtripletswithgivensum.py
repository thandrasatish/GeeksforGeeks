def findTriplets(arr, n,sum):
    for i in range(n):
        s=set()
        curr_sum=sum-arr[i]
        for j in range(i+1,n):
            x=curr_sum-arr[j]
            if(x in s):
                print(x,arr[i],arr[j])
            else:
                s.add(arr[j])

arr = [0, -1, 2, -3, 1]
n = len(arr)
sum=1
findTriplets(arr, n,sum)
