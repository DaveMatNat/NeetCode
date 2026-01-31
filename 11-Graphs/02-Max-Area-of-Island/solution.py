"""
Max Area of Island
LeetCode 695

Problem: 

Approach:

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def maxAreaOfIsland(self, grid: list) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        max_area = 0
        visited = set()

        def dfs(start):
            visited.add(start)
            area = 1

            curr_x, curr_y = start
            for x,y in directions:
                new_x,new_y = curr_x + x, curr_y + y
                if new_x in range(rows) and new_y in range(cols) and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    area += dfs((new_x,new_y))
            return area

        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == 1:
                    area = dfs((row,col))
                    max_area = max(max_area, area)
        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()

    g1 = [[0,1,1,0,1],
          [1,0,1,0,1],
          [0,1,1,0,1],
          [0,1,0,0,1]]
    
    # Test case 1
    print(solution.maxAreaOfIsland(g1))
    # TODO: Add test cases
    pass
