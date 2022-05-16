class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, k) : 
        sm=0
        ans=0
        m=dict()
        m[0]=-1
        for i in range(n):
            sm+=arr[i]
            rem=sm%k
            if rem<0:
                rem+=k
            if rem in m:
                idx=m[rem]
                ans=max(ans,i-idx)
            else:
                m[rem]=i
        return ans 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends
