class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # !!! Prefix only starts from the 1st letter

        # ez - pick first word, compare with 2nd word
        # find longest prefix and put in a set

        if len(strs) <= 1:
            return strs[0]

        first_word = strs[0]
        second_word = strs[1]
        prefix = set()
        dummy = []

        min_length = min(len(s) for s in strs)
        for i in range(min_length):
            if first_word[i] == second_word[i]:
                prefix.add(first_word[i])
                dummy.append(first_word[i])
            else:
                break
        
        # if cant find whole prefix in any word, return ""
        if prefix == None:
            return ""

        # search all words to see if the prefix is in it
        # if prefix is too long in any word, reduce the size of the prefix
        for i in prefix:
            for s in strs:
                if i not in s:
                    dummy.remove(i)

        result = ""
        for i in dummy:
            result += i
        return result
