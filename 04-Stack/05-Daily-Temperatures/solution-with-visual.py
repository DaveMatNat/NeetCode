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
        """
        Find how many days until a warmer temperature for each day.
        Uses a monotonic decreasing stack to track unresolved temperatures.
        
        Example: [73, 74, 75, 71, 69, 72, 76, 73]
                  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
                 [1,  1,  4,  2,  1,  1,  0,  0]
        
        Time: O(n) - each element pushed/popped once
        Space: O(n) - stack can hold all elements in worst case
        """
        
        # Initialize result array - defaults to 0 (no warmer day found)
        res = [0] * len(temperatures)
        
        # Stack stores (temperature, index) pairs
        # Maintains decreasing temperatures from bottom to top
        # Represents days still waiting for a warmer day
        stack = []
        
        # Process each day's temperature
        for i, current_temp in enumerate(temperatures):
            
            # While we have unresolved days AND current day is warmer
            # Resolve all cooler days by calculating days until warmth
            #
            # Visual: Stack before popping (temps decreasing ↓)
            #         [(75, 2), (73, 1), (71, 0)] ← top
            #         Current: 76 at index 3
            #         → Pop all since 76 > all of them
            #
            while stack and current_temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                
                # Calculate days waited: current_index - previous_index
                res[prev_index] = i - prev_index
            
            # Add current day to stack (may be resolved by future warmer day)
            stack.append((current_temp, i))
        
        # Remaining items in stack never found a warmer day (already 0 in res)
        return res


"""
WALKTHROUGH EXAMPLE: [73, 74, 75, 71, 69, 72, 76, 73]

i=0, temp=73:  stack=[]              → push (73,0)  → stack=[(73,0)]
i=1, temp=74:  stack=[(73,0)]        → 74>73, pop, res[0]=1  → push (74,1)  → stack=[(74,1)]
i=2, temp=75:  stack=[(74,1)]        → 75>74, pop, res[1]=1  → push (75,2)  → stack=[(75,2)]
i=3, temp=71:  stack=[(75,2)]        → 71<75, just push  → stack=[(75,2),(71,3)]
i=4, temp=69:  stack=[(75,2),(71,3)] → 69<71, just push  → stack=[(75,2),(71,3),(69,4)]
i=5, temp=72:  stack has (69,4),(71,3)
               → 72>69, pop, res[4]=1
               → 72>71, pop, res[3]=2
               → 72<75, push  → stack=[(75,2),(72,5)]
i=6, temp=76:  stack has (72,5),(75,2)
               → 76>72, pop, res[5]=1
               → 76>75, pop, res[2]=4
               → push (76,6)  → stack=[(76,6)]
i=7, temp=73:  stack=[(76,6)]        → 73<76, push  → stack=[(76,6),(73,7)]

Final: res = [1, 1, 4, 2, 1, 1, 0, 0]
       Items left in stack never found warmer day (remain 0)
"""

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.dailyTemperatures([30,38,30,36,35,40,28]))
    print(solution.dailyTemperatures([22,21,20]))
    # TODO: Add test cases
    pass
