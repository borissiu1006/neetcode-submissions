class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boat = 0
        while l <= r: # = : handle last one
            if people[l] == limit:
                return len(people[l:r + 1]) + boat
            elif people[r] == limit:
                boat += 1
                r -= 1
            elif people[l] + people[r] == limit:
                boat += 1
                l += 1
                r -= 1
            elif people[l] + people[r] < limit:
                boat += 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                boat += 1
                r -= 1
            elif l == r:
                boat += 1
        
        return boat


