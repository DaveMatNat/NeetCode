"""
Rotting Oranges
LeetCode 994

Problem: 

Approach:

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: list) -> int:
        rows,cols = len(grid), len(grid[0])
        fresh = 0
        rotten = []
        directions = [(1,0),(0,1), (-1,0), (0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        if fresh == 0:
            return 0
        time = 0
    
        queue = deque()

        for r in rotten:
            queue.append(r)

        while queue:
            rotten_this_round = 0
            for _ in range(len(queue)):
                popped_v = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = popped_v[0] + dx, popped_v[1] + dy
                    if new_x in range(rows) and new_y in range(cols) and (new_x, new_y) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh -= 1
                        rotten_this_round += 1
                        queue.append((new_x,new_y))
            if rotten_this_round > 0:
                time += 1
        
        return time if fresh == 0 else -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    Graphs = [[[1,1,0],[0,1,1],[0,1,2]], [[1,0,1],[0,2,0],[1,0,1]]]
    for g in Graphs:
        print(solution.orangesRotting(g))
    # TODO: Add test cases
    pass
