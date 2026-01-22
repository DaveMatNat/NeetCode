"""
Koko Eating Bananas
LeetCode 875

Problem: 

Approach:

Time Complexity: O(m * n)
Space Complexity: O(1)
"""
import math
class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:
        speed = 1
        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/speed)
            
            if totalTime <= h:
                return speed
            speed += 1
        return speed
            


# Test cases
if __name__ == "__main__":
    solution = Solution()

    print(solution.minEatingSpeed([1,4,3,2],9))
    
    # Test case 1
    # TODO: Add test cases
    pass
