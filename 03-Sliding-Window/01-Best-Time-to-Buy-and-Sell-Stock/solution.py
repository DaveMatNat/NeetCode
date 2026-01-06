"""
Best Time to Buy and Sell Stock
LeetCode 121

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1 
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([7,6,4,3,1]))
    # TODO: Add test cases
    pass
