class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # !!! Prefix only starts from the 1st letter

        # ez - pick first word, compare with 2nd word
        # find longest prefix and put in a set
        # O(n)

        if len(strs) <= 1:
            return strs[0]

        first_word = strs[0]
        second_word = strs[1]
        dummy = ""
        char = ""

        min_length = min(len(s) for s in strs)
        for i in range(min_length):
            if first_word[i] == second_word[i]:
                dummy += first_word[i]
                char += first_word[i]

            else:
                break

        # search all words to see if the prefix is in it
        # if prefix is too long in any word, reduce the size of the prefix

        for i in range(len(dummy)):
            for s in strs:
                if dummy[i] != s[i]:
                    char = char[:-1]
                    
        return char
