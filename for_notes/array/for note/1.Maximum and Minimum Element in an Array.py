# Write a python function to return minimum and maximum in an array. 
# Your program should make the minimum number of comparisons.


#written below is my process: but here the number of search is high resulting is huge time complexity


class Solution:
    def findSum(self,A,N): 
        #code here
        A.sort()
        min = A[0]
        max = A[-1]
        return (min + max)

# here basically we sort the array and the first element is obvisoisly the min and last element is the max
# A is the array and N is the size of the array 








#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends