class Solution:
    def isPalindrome(self, s: str) -> bool:
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

        