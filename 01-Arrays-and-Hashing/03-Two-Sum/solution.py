"""
Two Sum
LeetCode 1

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target: int) -> list:
        hmap = {} # val -> index
        for i,val in enumerate(nums):
            diff = target - val
            if diff in hmap:
                return [hmap[diff],i]
            hmap[val] = i


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.twoSum([3,4,5,6],7))
    # TODO: Add test cases
    print(solution.twoSum([4,5,6],10))
    pass
