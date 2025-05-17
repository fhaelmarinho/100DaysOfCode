# ✨ 100 Days of Code Challenge - Day 13/100 💻
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

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

def graph(a, b, c):
    x_vertex = -b/(2*a)
    x = np.linspace(x_vertex - 5, x_vertex + 5, 500)
    y = a*x**2 + b*x + c
    plt.figure(figsize=(10, 6))
    plt.title("Graph of the quadratic function")
    plt.plot(x, y)
    plt.grid(True)

    d = delta(a, b, c)
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        plt.scatter([x1, x2], [0, 0], color='red', label=f'Roots: {x1:.2f}, {x2:.2f}')

def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    
    result = bhaskara(a, b, c)
    print(f"Delta: {delta(a, b, c)}")
    print(result)

# generate Graph
    graph(a, b, c)
    plt.show()

if __name__ == "__main__":
    main()