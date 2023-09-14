
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
        previous = ""
        for index ,current in enumerate(symbols):
            
            if index >1:
                previous = symbols[index-2]  

            #IV OR #IX
            if previous == 'I' and current == 'V' or previous == 'I' and current == 'X':
                totalSum = self.sumIt('I',totalSum)
            
            #XL OR #XC
            if previous == 'X' and current == 'L' or previous == 'X' and current == 'C':
                totalSum = self.sumIt('X',totalSum)
            
            if previous == 'C' and current == 'D' or previous == 'C' and current == 'M':
                totalSum = self.sumIt('C',totalSum)

            totalSum += self.roman_nums[current]
        return totalSum;

    def sumIt(self, prev, total):
        return total-(2*self.roman_nums[prev])
    
sol = Solution()
print("Result : ", sol.romanToInt("XDCXXI"))

