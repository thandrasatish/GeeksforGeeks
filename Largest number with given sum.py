
class Solution:
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,n,s):
        if(n * 9 < s):
            return -1
        if(s <= 9):
            return(str(s) + (n-1) * '0')
        nines = s // 9
        rest = s % 9
        if rest==0:
            return(nines * '9'+ (n-nines) * '0')
        else:
            return(nines * '9' + str(rest) + (n-nines-1) * '0')
            
        # code here
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends
