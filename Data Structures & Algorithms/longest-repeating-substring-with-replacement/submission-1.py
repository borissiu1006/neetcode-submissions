class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window
        mp = {}
        l = max_freq = max_len = 0
        
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            max_freq = max(max_freq, mp[s[r]])

            window = r - l + 1
            replace = window - max_freq
            
            if replace > k:
                mp[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len

        