#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

#User function Template for python3
from bisect import bisect_left
from typing import List

class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        count = 0
        for index, value in enumerate(arr):
            insertion_point = bisect_left(arr, target - value, hi=index)
            count += insertion_point
      
        return count 
    

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
