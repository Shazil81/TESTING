class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Binary exponential algorithm TC:O(logn)
        # Recursion se krte hain TC:O(logn)   SC:O(logn)
        if n == 0:
            return 1
        
        # Negative power ko handle karna
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # Binary Exponentiation (Divide and Conquer)
        half = self.myPow(x, n // 2)
        
        # Agar power even hai
        if n % 2 == 0:
            return half * half
        # Agar power odd hai
        else:
            return x * half * half
        