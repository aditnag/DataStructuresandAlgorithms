class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}  # stores string : idx
        count = 0
        n = len(s)
        start_idx = 0
        for i in range(n):
            if s[i] in mp:
                start_idx = max(start_idx, mp[s[i]] + 1)

            count = max(count, i - start_idx + 1)

            mp[s[i]] = i

        return count


if __name__ == "__main__":
    solution = Solution()
    s = input()
    length = solution.lengthOfLongestSubstring(s)
    print(length)

