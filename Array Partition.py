#User function Template for python3
from collections import deque
class Solution:
    def partitionArray(self,N,K,M,arr):
        arr.sort()
        q = deque([0])
        for i in range(K-1,N):
            while(i-q[0]+1 >=K):
                if(arr[i]-arr[q[0]]<=M):
                    q.append(i+1)
                    break
                q.popleft()
                if not q:
                    return False
        return q[-1] == N

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,k,m=map(int,input().split())
        arr=list(map(int,input().strip().split()))
        obj=Solution()
        ans=obj.partitionArray(n,k,m,arr)
        if ans:
            print('YES')
        else:
            print('NO')
# } Driver Code Ends
