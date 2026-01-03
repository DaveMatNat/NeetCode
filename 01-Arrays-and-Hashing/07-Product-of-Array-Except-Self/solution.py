"""
Product of Array Except Self
LeetCode 238

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(1) extra space, O(n) space for output array
"""

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        t_prod = 1
        count_zeroes = 0
        for i in nums:
            if i == 0:
                count_zeroes += 1
                if count_zeroes > 1:
                    return [0] * len(nums)
            else:
                t_prod *= i
        # 1 Zero
        if count_zeroes == 1:
            res = []
            for i in nums:
                if i == 0:
                    res.append(t_prod)
                else:
                    res.append(0)
            return res
        # No Zero
        return [t_prod//i for i in nums]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.productExceptSelf([1,2,4,6]))
    print(solution.productExceptSelf([-1,0,1,2,3]))
    # TODO: Add test cases
    pass
