
### Code to demonstrate

import numpy as np
import matplotlib.pyplot as plt
import math

def f(n):
    return 2**n * math.sin(math.pi / 2**n)

n_values = range(1, 100)
y_values = [f(n) for n in n_values]

plt.plot(n_values, y_values, label='$2^n \\sin(\\frac{\\pi}{2^n})$')
plt.axhline(y=math.pi, color='r', linestyle='--', label='$\\pi$')
plt.xlabel('n')
plt.ylabel('y-coordinate')
plt.legend()
plt.show()

approaches_pi = math.isclose(y_values[-1], math.pi, rel_tol=1e-6)

approaches_pi, y_values[-1]
