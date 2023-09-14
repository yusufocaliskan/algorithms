import re
class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = re.search("[[\(.*\)]\[.*\]{.*}]",s)
        print(result)
        
Solution().isValid("(")