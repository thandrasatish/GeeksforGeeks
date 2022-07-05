#User function Template for python3
import string
class Solution:
    def count (self,s):
        p=0
        u=0
        l=0
        n=0
        for i in s:
            if(i in string.punctuation):
                p+=1
            if(i in string.ascii_uppercase):
                u += 1
            if(i in string.ascii_lowercase):
                l +=1
            if(i in string.digits):
                n+=1
        return u,l,n,p
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends
