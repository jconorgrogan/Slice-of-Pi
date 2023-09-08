## Theorem
Let \( R = 2^n \) for some positive integer \( n \). Consider a circle of radius \( R \) centered at the origin. Divide the circle into \( 2R \) equal slices. The \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \).

## Proof
1. The \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis is:
   \[
   y = R \sin\left(\frac{\pi}{R}\right)
   \]

2. Substituting \( R = 2^n \):
   \[
   y = 2^n \sin\left(\frac{\pi}{2^n}\right)
   \]

3. We want to find the limit as \( n \rightarrow \infty \):
   \[
   \lim_{{n \to \infty}} 2^n \sin\left(\frac{\pi}{2^n}\right)
   \]

4. Utilizing the limit identity \( \lim_{{x \to 0}} \frac{\sin(x)}{x} = 1 \), multiply and divide by \( \frac{\pi}{2^n} \):
   \[
   \lim_{{n \to \infty}} \left(2^n \frac{\pi}{2^n}\right) \left(\frac{\sin\left(\frac{\pi}{2^n}\right)}{\frac{\pi}{2^n}}\right)
   \]

5. As \( n \rightarrow \infty \), \( \frac{\pi}{2^n} \rightarrow 0 \), making the second term approach 1. The first term is \( \pi \).

6. Therefore, the limit is \( \pi \times 1 = \pi \).

This proves that the \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \).

Each of these horizontal lines approaches a multiple of pi as R goes to infinity
![image](https://github.com/jconorgrogan/Grogans-Slice-of-Pi/assets/130090573/2a204d04-0238-44ed-a5f4-a91fe5c68617)


As R increases, each 2nd node y coordinate moves towards 2pi, 3rd node 3pi, etc. 
How each point converges to these multiples of pi creates some extremely interesting fractals which are worthy of future research

The infinite prime ladder, and the Grogan Rollercoaster 
![image](https://github.com/jconorgrogan/Grogans-Slice-of-Pi/assets/130090573/f45b1293-16f1-41fd-abdf-ead3df0f4284)


##Here is the code:

import matplotlib.pyplot as plt
import numpy as np

# Initialize variables
n_values = np.arange(1, 21)  # n from 1 to 20
R_values = 2 ** n_values  # Calculate R = 2^n

# Further extend the nodes to investigate up to 250
highest_extended_nodes = np.arange(1, 251)  # from node 1 to node 250

# Initialize new dictionaries for y-coordinates and deltas for the highest extended nodes
y_values_highest_extended = {}
deltas_highest_extended = {}

# Calculate y-coordinates and their deltas for the highest extended nodes
for node in highest_extended_nodes:
    y_values_highest_extended[node] = []
    deltas_highest_extended[node] = []
    for R in R_values:
        y = R * np.sin(node * np.pi / R)
        y_values_highest_extended[node].append(y)
        delta = node * np.pi - y  # Calculate the delta from node*pi for each node
        deltas_highest_extended[node].append(delta)

# Initialize a new figure for the highest extended graph
plt.figure(figsize=(30, 15))

# Plot the y-coordinates for the highest extended nodes
plt.subplot(1, 2, 1)
for node in highest_extended_nodes:
    plt.plot(R_values, y_values_highest_extended[node], marker='o', label=f'Node {node}' if node % 100 == 0 else "")
plt.xlabel('R')
plt.ylabel('y-coordinate')
plt.title('Convergence of y-coordinates to nπ (Nodes 1-250)')
plt.xscale('log')
plt.legend()

# Plot the deltas for the highest extended nodes
plt.subplot(1, 2, 2)
for node in highest_extended_nodes:
    plt.plot(R_values, deltas_highest_extended[node], marker='o', label=f'Delta from {node}π' if node % 100 == 0 else "")
plt.xlabel('R')
plt.ylabel('Delta')
plt.title('Convergence of Deltas to Zero (Nodes 1-250)')
plt.xscale('log')
plt.legend()

# Show the highest extended graph
plt.tight_layout()
plt.show()


