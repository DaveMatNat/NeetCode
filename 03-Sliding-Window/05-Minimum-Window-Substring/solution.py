"""
Minimum Window Substring
LeetCode 76

Problem: 

Approach:

Time Complexity: O(n + m)
Space Complexity: O(m)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}

        # create frequency map for t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # initialize have and needs (unique char in t)
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # if the counts for this new character are the same in both window and countT, then we have what we needed!
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1

                # pop from the left of our window
                window[s[l]] -= 1

                # if by removing s[l] made the count less than it needed to be, then we don't have enough of that char
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # no longer have what we need
                    have -= 1
                # shift window up by incrementing l by 1
                l += 1
        l,r = res
        # resLen can = float("infinity") when result doesn't exist
        return s[l: r + 1] if resLen != float("infinity") else ""


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases

    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    print(solution.minWindow("a","a"))
    print(solution.minWindow("a","aa"))
    print(solution.minWindow("SAVID","AD"))
    # TODO: Add test cases
    pass
