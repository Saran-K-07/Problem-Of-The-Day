# Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
# Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]

from collections import defaultdict

def group_anagrams(strs):
        anagrams = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anagrams[key].append(s)
            
        return list(anagrams.values())
        
arr = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
ans = group_anagrams(arr)
print(ans)