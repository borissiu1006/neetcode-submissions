class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Counting sort
        m = max(people)
        count = [0] * (m + 1)
        for i in people:
            count[i] += 1

        i, c = 0, 1 # i: overwrite [people], c: move in [count]
        while i < len(people):
            while count[c] == 0: # No more people in that weight > move to next
                c += 1
            people[i] = c
            count[c] -= 1
            i += 1

        # people.sort()
        l, r = 0, len(people) - 1
        boat = 0
        while l <= r: # = : Handle last one
            if people[l] + people[r] <= limit: # Both onboard
                l, r = l + 1, r - 1
            elif people[l] + people[r] > limit: # Heavy guy onboard only
                r -= 1 
            boat += 1
        
        return boat
        