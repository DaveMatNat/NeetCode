"""
Container With Most Water
LeetCode 11

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, r = 0, len(heights) - 1
        while l < r:
            currA = (r-l) * min(heights[l],heights[r]) # Area = width * height
            maxA = max(currA,maxA)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxA



# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    # TODO: Add test cases
    pass
