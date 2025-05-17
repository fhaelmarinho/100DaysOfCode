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
    # Generate the graph of the quadratic function
    x_vertex = -b / (2 * a)
    
    x = np.linspace(x_vertex - 10, x_vertex + 10, 500)
    y = a * x**2 + b * x + c
    
    plt.figure(figsize=(10, 6))
    plt.title("Graph of the quadratic function")
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Eixo x
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Eixo y

    d = delta(a, b, c)
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        plt.scatter([x1, x2], [0, 0], color='red', label=f'Roots: {x1:.2f}, {x2:.2f}')
        
    # Graph settings
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    plt.xticks(np.arange(round(x_vertex - 10), round(x_vertex + 11), 1))

    plt.legend()
    plt.show()

def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    
    result = bhaskara(a, b, c)
    print(f"Delta: {delta(a, b, c)}")
    print(result)

    graph(a, b, c)

if __name__ == "__main__":
    main()
