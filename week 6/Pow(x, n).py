class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:         
            return 1.0 / self.myPow(x, -n)
        elif n == 1:
            return x
        else:
            if n%2 == 0:
                return self.myPow(x*x, n//2)
            else:
                return x * self.myPow(x*x,n//2)