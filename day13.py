# ✨ 100 Days of Code Challenge - Day 13/100 💻
from math import sqrt

def delta(a, b, c):
    d = b**2 - (4*a*c)
    return d
    
    
def bhaskara(a, b, c):   
    d = delta(a, b, c)
    if d < 0:
        return "Delta is negative, no real roots"
    elif d == 0:
        x = -b/(2*a)
        return f"Delta is zero, one real root x = {x}"
    else:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        return f"Delta is positive, two real roots: X1 = {x1}, e X2 = {x2}"

def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    
    result = bhaskara(a, b, c)
    print(f"Delta: {delta(a, b, c)}")
    print(result)

if __name__ == "__main__":
    main()