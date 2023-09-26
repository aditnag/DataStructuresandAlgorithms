from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        itr, jtr = 0, len(people) - 1
        ans = 0
        while itr <= jtr:
            weight = people[itr] + people[jtr]
            ans += 1
            if weight <= limit:
                itr += 1
            jtr -= 1
        return ans
