"""
Group Anagrams
LeetCode 49

Problem: 

Approach:

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Where m is the number of strings and n is the length of the longest string.
"""

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        res = {}
        for w in strs:
            freq = [0]*26
            for c in w:
                idx = ord(c) - ord('a')
                freq[idx] += 1
            freq = tuple(freq)
            if freq not in res:
                res[freq] = [w]
            else:
                res[freq].append(w)
        return list(res.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
    # TODO: Add test cases
    pass
