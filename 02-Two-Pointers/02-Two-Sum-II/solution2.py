"""
Two Sum II - Input Array Is Sorted
LeetCode 167

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        l,r = 0,len(numbers)-1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return [l+1,r+1]    


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([2,3,4],6))
    print(solution.twoSum([-1,0],-1))
    # TODO: Add test cases
    pass
