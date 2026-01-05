"""
3Sum
LeetCode 15

Problem: 

Approach:

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        res = []
        for i in range(len(nums)-2):
            l,r = i+1, len(nums) - 1
            target = -(nums[i])
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                sums = nums[l] + nums[r]
                if sums == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sums < target:
                    l += 1
                else:
                    r -= 1
        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0,1,1]))
    # TODO: Add test cases
    pass
