class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(start):
            if grid[start[0]][start[1]] == 0:
                return 0
            if grid[start[0]][start[1]] == -1:
                return -1
                
            visited = []
            distances = {}
            distance = 0
        
            queue = deque()
            queue.append(start)
            distances[start] = 0

            while queue:
                current_vertex = queue.popleft()
                visited.append(current_vertex)

                for dx,dy in directions:
                    new_x,new_y = current_vertex[0] + dx, current_vertex[1] + dy
                    if new_x in range(rows) and new_y in range(cols) and (new_x,new_y) not in distances and grid[new_x][new_y] != -1:
                        distances[(new_x,new_y)] = distances[current_vertex] + 1
                        if grid[new_x][new_y] == 0:
                            return distances[(new_x,new_y)]
                        queue.append((new_x,new_y))

            return 
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        rows, cols = len(grid), len(grid[0])
        res = [[0 for i in range(cols)] for j in range(rows)]

        for r in range(rows):
            for c in range(cols):
                grid[r][c] = bfs((r,c))
                # do bfs on grid[r][c]
                