class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window - store freq for each char in window, then compare with mp_s1. not match >> slide
        l, r = 0, len(s1) - 1
        mp_s1 = {}
        mp_s2 = {}
        for i in range(len(s1)):
            mp_s1[s1[i]] = mp_s1.get(s1[i], 0) + 1

        for r in range(len(s2)):
            mp_s2[s2[r]] = mp_s2.get(s2[r], 0) + 1
            if mp_s2 == mp_s1:
                return True
            elif r - l + 1 == len(s1):
                mp_s2[s2[l]] -= 1
                if mp_s2[s2[l]] == 0:
                    del mp_s2[s2[l]]
                l += 1

        return False       