"""
Encode and Decode Strings
LeetCode 271

Problem: 

Approach:

Time Complexity: O(m)
Space Complexity: O(m + n)

Where m is the sum of lengths of all the strings and n is the number of strings.
"""

class Solution:

    def encode(self, strs: list) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = j + 1 + length
            res.append(s[i:j])
            i = j
        return res



# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    texts = ["Happy","New","Year"] 
    encoded_text = solution.encode(texts)
    print(encoded_text)
    print(solution.decode(encoded_text))
    # TODO: Add test cases
    pass
