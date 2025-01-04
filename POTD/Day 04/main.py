
class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        mp = {}
    
        for i in range(n):
            if arr[i] not in mp:
                mp[arr[i]] = []
            mp[arr[i]].append(i)
    
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                sum_pair = arr[i] + arr[j]
            
                if target - sum_pair in mp:
                    for k in mp[target - sum_pair]:
                        if k > j:
                            count += 1
    
        return count

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends
