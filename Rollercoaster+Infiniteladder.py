
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


