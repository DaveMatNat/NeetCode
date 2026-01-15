"""
Daily Temperatures
LeetCode 739

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:
        # Result list to store how many days until a warmer temperature
        res = [0] * len(temperatures)

        # Stack to store pairs of (temperature, index)
        # We'll use this to find the next warmer day
        stack = []

        # Go through each day and its temperature
        for i, t in enumerate(temperatures):

            # While the current temperature is warmer than the last one in the stack:
            # It means we've found a "next warmer day" for that earlier day
            while stack and t > stack[-1][0]:
                prevTemp, prevIdx = stack.pop()
                res[prevIdx] = i - prevIdx  # Calculate how many days it took to get warmer

            # Add the current day to the stack to find its next warmer day later
            stack.append((t, i))

        # Return the final result list
        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.dailyTemperatures([30,38,30,36,35,40,28]))
    print(solution.dailyTemperatures([22,21,20]))
    # TODO: Add test cases
    pass
