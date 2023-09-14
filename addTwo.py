class Solution:
    
    def addTwoNumbers(self, l1, l2):
        l1 = self.reverseIt(l1)
        l2 = self.reverseIt(l2)
        sumAll = int("".join(map(str, l1))) + int("".join(map(str, l2)))
        res = [int(x) for x in str(sumAll)]
        
        return self.reverseIt(res)
    
    def reverseIt(self,arr):
        ree = []
        for ar in reversed(arr):
            ree.append(ar)
        return ree
    
solution = Solution()
print(solution.addTwoNumbers([1,3,1],[1,9,1]))