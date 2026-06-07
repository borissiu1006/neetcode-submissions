class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        return True
    '''
        holder = []
        for i in s:
            if i.isalpha():
                holder.append(i.lower())
            elif i.isdigit():
                holder.append(i)
        
        reverse = holder.copy()

        for i in range(len(reverse) // 2):
            reverse[i], reverse[- (i + 1)] = reverse[- (i + 1)], reverse[i]

        if holder == reverse:
            return True
        
        return False
    '''

        