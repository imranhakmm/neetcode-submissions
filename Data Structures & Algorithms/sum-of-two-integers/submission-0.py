class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask,maxint=0xFFFFFFFF,0x7FFFFFFF
        while b!=0:
            carry=(a&b)<<1
            a=(a^b) & mask
            b=carry&mask
        return a if a<=maxint else ~(a^mask)

