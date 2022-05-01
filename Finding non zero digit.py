def satish(N,arr):
    sum1=1
    for i in range(N):
        sum1=sum1*arr[i]
    sum1=str(sum1)
    print(sum1)
    for i in range(len((sum1))-1,-1,-1):
        if(sum1[i]!='0'):
            return sum1[i]
    return -1
N = 5
arr = [1, 2, 3, 4, 5]
print(satish(N,arr))
