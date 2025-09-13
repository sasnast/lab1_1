def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = 48
y = 18
print(f"НОД чисел {x} и {y} равен {gcd(x, y)}")