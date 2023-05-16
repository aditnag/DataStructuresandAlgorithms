class MaximumNumberofVowelsinSubstringofGivenLength:
    def find_max_vowels(self, s, k):
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_count = max(count, max_count)
        return max_count


obj = MaximumNumberofVowelsinSubstringofGivenLength()
t = int(input())
while t:
    inp = input()
    li = inp.split()
    s = li[0]
    k = int(li[1])
    print(obj.find_max_vowels(s, k), end="\n")
    t -= 1
