class xfrac:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self):
        # 연분수 계산
        numerator = self.a * self.b + self.c
        denominator = self.b

        # 최대공약수를 이용하여 약분
        common_divisor = self.gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        return numerator, denominator

    def gcd(self, a, b):
        # 최대공약수 계산
        while b:
            a, b = b, a % b
        return a
    
    def calculate(self):
        if isinstance(self.a, xfrac):
            self.a = self.a.calculate()
        if isinstance(self.b, xfrac):
            self.b = self.b.calculate()
        if isinstance(self.c, xfrac):
            self.c = self.c.calculate()
        
        return self.evaluate()
        
        
        
print(xfrac(*[2,7,3]))