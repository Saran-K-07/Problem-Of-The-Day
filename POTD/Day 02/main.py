#User function Template for python3
from collections import defaultdict

class Solution:
    def countSubarrays(self, arr, k):
        n = len(arr)
        ref = defaultdict(int)
        preSum = 0
        cnt = 0

        ref[0] = 1 
        for i in range(n):
            preSum += arr[i]
            remove = preSum - k
            cnt += ref[remove]
            ref[preSum] += 1

        return cnt



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends