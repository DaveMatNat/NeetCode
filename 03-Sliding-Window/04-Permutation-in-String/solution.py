"""
Permutation in String
LeetCode 567

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s2 is shorter than s1, s1 cannot be a permutation substring
        if len(s2) < len(s1):
            return False
        
        # Frequency arrays for counting character occurrences (26 letters)
        chars_s1 = [0] * 26  # Character frequency of s1 (target permutation)
        chars_s2 = [0] * 26  # Character frequency of current window in s2
        
        # Build initial frequency counts for s1 and first window of s2
        for i in range(len(s1)):
            chars_s1[ord(s1[i]) - ord('a')] += 1
            chars_s2[ord(s2[i]) - ord('a')] += 1
        
        # Count how many character frequencies match between s1 and current window
        matches = 0
        for i in range(26):
            matches += 1 if chars_s1[i] == chars_s2[i] else 0
        
        # Sliding window: left pointer starts at 0
        l = 0
        
        # Slide the window across s2, starting from position len(s1)
        for r in range(len(s1), len(s2)):
            # If all 26 character frequencies match, we found a permutation
            if matches == 26:
                return True
            
            # Add the new character at right pointer to the window
            idx = ord(s2[r]) - ord('a')
            chars_s2[idx] += 1
            
            # Update match count based on new character
            if chars_s1[idx] == chars_s2[idx]:
                matches += 1  # Adding this char created a match
            elif chars_s1[idx] == chars_s2[idx] - 1:
                matches -= 1  # Adding this char broke a previous match
            
            # Remove the character at left pointer from the window
            idx = ord(s2[l]) - ord('a')
            chars_s2[idx] -= 1
            
            # Update match count based on removed character
            if chars_s1[idx] == chars_s2[idx]:
                matches += 1  # Removing this char created a match
            elif chars_s1[idx] == chars_s2[idx] + 1:
                matches -= 1  # Removing this char broke a previous match
            
            # Move left pointer forward to maintain window size
            l += 1
        
        # Final check: does the last window match?
        return matches == 26


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.checkInclusion("ab","lecabee"))
    print(solution.checkInclusion("abc","lecaabee"))
    pass
