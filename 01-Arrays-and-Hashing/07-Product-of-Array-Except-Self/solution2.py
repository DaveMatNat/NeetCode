"""
(FOLLOW UP WITHOUT DIVISION)

Product of Array Except Self 
LeetCode 238

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(1) extra space, O(n) space for output array
"""

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.productExceptSelf([1,2,4,6]))
    print(solution.productExceptSelf([-1,0,1,2,3]))
    # TODO: Add test cases
    pass
