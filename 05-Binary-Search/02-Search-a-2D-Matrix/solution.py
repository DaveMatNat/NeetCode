"""
Search a 2D Matrix
LeetCode 74

Problem: 

Approach:

Time Complexity: O(logm + logn) = O(log(mn))
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        # find row
        rows, cols = len(matrix), len(matrix[0])
        top,bot = 0, rows - 1

        likely_row = -1

        while top <= bot:
            mid = (top+bot) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                likely_row = mid
                break
        
        if not (top <= bot):
            return False

        # for in each of that row's column
        l,r = 0, cols - 1
        while l <= r:
            mid = (l+r) //2
            if matrix[likely_row][mid] == target:
                return True
            elif matrix[likely_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False



# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 67))
    # Test case 1
    # TODO: Add test cases
    pass
