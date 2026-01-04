"""
Longest Consecutive Sequence
LeetCode 128

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: list) -> int:
        hashSet = set(nums)
        longest = 0
        for n in hashSet:
            # is n is the beginning of a sequence
            if (n-1) not in hashSet:
                curr = 1
                while (n+curr) in hashSet:
                    curr += 1
                longest = max(curr,longest)
            # if is n is NOT the beginning of a sequence, then we will loop to the beginning at some point
        return longest



# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.longestConsecutive([100,4,200,1,3,2]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(solution.longestConsecutive([1,0,1,2]))
    # TODO: Add test cases
    pass
