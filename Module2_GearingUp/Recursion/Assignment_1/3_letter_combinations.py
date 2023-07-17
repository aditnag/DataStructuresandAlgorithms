class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {
            0: ['a', 'b', 'c'],
            1: ['d', 'e', 'f'],
            2: ['g', 'h', 'i'],
            3: ['j', 'k', 'l'],
            4: ['m', 'n', 'o'],
            5: ['p', 'q', 'r', 's'],
            6: ['t', 'u', 'v'],
            7: ['w', 'x', 'y', 'z']
        }
        if len(digits) == 0:
            return
        temp = []
        idx = 0
        return self.all_combination(temp, digits, idx, digit_map)

    def all_combination(self, temp, digits, idx, digit_map):
        if idx == len(digits):
            return ["".join(temp)]

        combination = []
        for j in range(len(digit_map[int(digits[idx]) - 2])):
            combination.extend(self.all_combination(temp + [digit_map[int(digits[idx]) - 2][j]], digits, idx + 1, digit_map))
        return combination
