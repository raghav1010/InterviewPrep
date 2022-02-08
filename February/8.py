#258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        ans = num%9
        if ans==0:
            return 9
        else:
            return ans