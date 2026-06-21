class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boat = 0
        while l <= r: # = : handle last one
            if people[l] == limit:
                return len(people[l:r + 1]) + boat
            elif people[l] + people[r] <= limit: # <= : both get on, > : heavy get on
                l, r = l + 1, r - 1
            elif people[l] + people[r] > limit:
                r = r - 1
            boat += 1

        
        return boat


