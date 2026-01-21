"""
Binary Search
LeetCode 704

Problem: 

Approach:

Time Complexity: O(log(n))
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums: list, target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()

    print(solution.search([-1,0,2,4,6,8],4))
    
    # Test case 1
    # TODO: Add test cases
    pass
