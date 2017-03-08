import sys


class ComplexNumber:
    _eps = 1e-8

    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real + 0.0
        self.imaginary = imaginary + 0.0

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real -
                             self.imaginary * other.imaginary,
                             self.real * other.imaginary +
                             self.imaginary * other.real)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __truediv__(self, other):
        divider = float((other.imaginary ** 2 + other.real ** 2))

        new_real_part = ((self.real * other.real +
                         self.imaginary * other.imaginary)) / divider

        new_imaginary_part = (self.imaginary * other.real -
                              self.real * other.imaginary) / divider

        return ComplexNumber(new_real_part, new_imaginary_part)

    def __str__(self):
        symbol = " + " if self.imaginary > 0 else " - "

        if abs(self.real) >= self._eps <= abs(self.imaginary):
            return "%.2f" % self.real + symbol + \
                   "%.2f" % abs(self.imaginary) + "i"

        if abs(self.real) <= self._eps < abs(self.imaginary):
            return "%.2f" % self.imaginary + "i"

        if abs(self.real) >= self._eps > abs(self.imaginary):
            return "%.2f" % self.real

        if abs(self.real) <= self._eps and abs(self.imaginary) <= self._eps:
            return "0.00"

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print(eval(line.strip()))
