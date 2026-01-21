#problem 5
#write a class complex to represent complex numbers along with overloaded operators - and / to subtract and divide two complex numbers respectively.
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
# Example usage:
c1 = Complex(5, 6)
c2 = Complex(2, 3)
diff_complex = c1 - c2
quotient_complex = c1 / c2
print(f"Difference: {diff_complex}")