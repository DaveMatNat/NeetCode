"""
Top K Frequent Elements
LeetCode 347

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        # Frequency Map: { Number -> Count }
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        # Based on frequency, add the number to the corresponding bucket
        for n,c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.topKFrequent([1,2,2,3,3,3,4,4,4,4],2))
    # TODO: Add test cases
    print(solution.topKFrequent([1,2,2,3,3,3,4,4,4,4],3))
    print(solution.topKFrequent([67],1))
    pass
