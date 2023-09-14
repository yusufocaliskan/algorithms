class Solution:
    def reverse(self, x):
        inta = [int(n) for n in str(x)]
        re = []
        for x in reversed(inta):
            re.append(x)
        return int("".join(map(str, re)))
print(Solution().reverse(123))