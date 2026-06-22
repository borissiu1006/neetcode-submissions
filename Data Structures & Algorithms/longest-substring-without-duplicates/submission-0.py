class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ''
        maxlen = 0
        for i in range(len(s)):
            if s[i] in window:
                window = window[window.index(s[i]) + 1:]
            window += s[i]
            maxlen = max(maxlen, len(window))
        
        return maxlen