class Solution:
    def numSquares(self, n: int) -> int:
        while n%4==0:
            n//=4
        if n%8==7:
            return 4

        if n==int(math.sqrt(n))*int(math.sqrt(n)):
            return 1
        i=1
        while i*i<=n:
            if n-i*i==int(math.sqrt(n-i*i))*int(math.sqrt(n-i*i)):
                return 2
            i+=1

        return 3
        
