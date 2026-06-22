class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = longest = 0
        for r in range(len(s)):
            if s[r] in window:
                l = max(window[s[r]] + 1, l)
            window[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest
        '''
        window = ''
        maxlen = 0
        for i in range(len(s)):
            if s[i] in window:
                window = window[window.index(s[i]) + 1:]
            window += s[i]
            maxlen = max(maxlen, len(window))
        
        return maxlen
        '''