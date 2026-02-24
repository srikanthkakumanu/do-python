from decimal import Decimal
from fractions import Fraction


def int_operations():
    a = 10
    b = int(23)
    c = int('323')
    d = int('FACE', 16) # 16 is Hexadecimal base
    e = int('0xface', 0)
    f = int('0o12', 8)
    g = int('011101110011', base=2)
    h = int('      -12345\n')
    print(a, b, c, d, e, f, g, h)

def float_operations():
    a = +1.24
    b = float('+1.23')
    c = float('   -12345\n')
    d = float('1e-003')
    e = float('+1E6')
    # Case is not significant, “inf”, “Inf”, “INFINITY”, and “iNfINity” are all acceptable spellings for positive infinity.
    f = float('-Infinity')

    print(a, b, c, d, e, f)

def decimal_operations():
    """
    Decimal objects cannot generally be combined with floats or instances of fractions.
    Fraction in arithmetic operations: an attempt to add a Decimal to a float, for example, will raise a TypeError.
    """

    a = Decimal('0.1')
    b = Decimal('0.2')
    c = a + b
    # For Decimal, % is the result is the sign of the dividend rather than the sign of the divisor
    d = 8 % 3
    e = (-7) % 4
    f = Decimal(-7) % Decimal(4)
    g = -7 // 4
    h = Decimal(-7) // Decimal(4)
    i = Decimal('-3.14').as_integer_ratio()

    print(a, b, c, d, e, f, g, h, i)

def fraction_operations():
    a = Fraction(16, -10)
    b = Fraction(123)
    c = Fraction()
    d = Fraction('3/7')
    e = Fraction(' -3/7 ')
    f = Fraction('1.414213 \t\n')
    g = Fraction('-.125')
    h = Fraction('7e-6')
    i = Fraction(2.25)
    j = Fraction(1.1)
    k = Fraction(Decimal('1.1'))
    l = Fraction(22, 7)

    print(a, b, c, d, e, f, g, h, i, j, k, l)


def main():
    int_operations()
    float_operations()
    decimal_operations()
    fraction_operations()


if __name__ == "__main__":
    main()
