"""
Number of Islands
LeetCode 200

Problem: 

Approach:

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def numIslands(self, grid: list) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        num_islands = 0
        visited = set()

        def dfs(start):
            visited.add(start)
            curr_x, curr_y = start
            for x,y in directions:
                new_x,new_y = curr_x + x, curr_y + y
                if new_x in range(rows) and new_y in range(cols) and grid[new_x][new_y] == "1" and (new_x, new_y) not in visited:
                    dfs((new_x,new_y))

        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == "1":
                    dfs((row,col))
                    num_islands += 1
        return num_islands

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    g1 = [["0","1","1","1","0"],
          ["0","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]]
    
    g2 = [["1","1","0","0","1"],
          ["1","1","0","0","1"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]]
    
    print(solution.numIslands(g1))
    print(solution.numIslands(g2))
    # TODO: Add test cases
    pass
