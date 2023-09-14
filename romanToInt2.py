
class Solution:
    roman_nums = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
      

    def romanToInt(self, symbols:str) -> int: 
        totalSum = 0
        symbols = symbols.replace('IV','IIII').replace('IX','VIIII')
        symbols = symbols.replace('XL','XXXX').replace('XC','LXXXX')
        symbols = symbols.replace('CD','CCCC').replace('CM','DCCCC')
        print(symbols)
        for current in symbols:
            totalSum += self.roman_nums[current]
        return totalSum;

    
sol = Solution()

print("Result : ", sol.romanToInt("DCXXI"))
