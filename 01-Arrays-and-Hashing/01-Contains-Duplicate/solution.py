"""
Contains Duplicate
LeetCode 217

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def hasDuplicate(self, nums) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.hasDuplicate([1,2,3,3]))
    # Test case 2
    print(solution.hasDuplicate([1,2,3,4]))
    # TODO: Add test cases
    pass
