class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for i in strs:
            string += i
            string += '👍'
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        current = ''

        for alphabet in s:
            if alphabet == '👍':
                result.append(current)
                current = ''
                continue
            else:
                current += alphabet
        
        return result

