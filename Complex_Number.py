from sympy import symbols, pi, Eq, solve, simplify, Rational, cos, sin
import pandas as pd

# define symbols
theta, n = symbols('theta n', real=True)

# Define expression
theta_expr = (pi + 2 * pi * n) / 3

# Try different integer values of n to find which thetas are in [0, 2pi]
data = []

for i in range(-3, 4):
    theta_val = simplify(theta_expr.subs(n, i))
    if 0 <= theta_val <= 2*pi:
        cos_val = simplify(cos(theta_val))
        sin_val = simplify(sin(theta_val))
        data.append({
            'n': i,
            'theta': theta_val,
            'cos(theta)': cos_val,
            'sin(theta)': sin_val
        })

df = pd.DataFrame(data)

print(df)
