N = int(input())
K = int(input())
candies= list(map(int,input().split()))
candies.sort()
l,r,a,b=0,N-1,0,0
while(l<=r):
    a=a+candies[l]
    r=r-K
    b=b+candies[N-l-1]
    l=l+1
print(a,b)
