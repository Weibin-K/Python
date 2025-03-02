import numpy as np
import matplotlib.pyplot as plt

# Define the nonlinear function b(a)
def b(a):
    return np.sin(a) + 0.2 * a  # Example nonlinear function

# Define the linear approximation at a specific operating point A
A = 1  # Operating point
b_A = b(A)  # Function value at A
k = np.cos(A) + 0.2  # Slope at A (derivative of b(a))
def b_lin(a):
    return b_A + k * (a - A)  # Linear approximation

# Generate data points
a_values = np.linspace(-1, 3, 400)  # Range of a values
b_values = b(a_values)  # Nonlinear function values
b_lin_values = b_lin(a_values)  # Linear approximation values

# Plot the nonlinear function and its linear approximation
plt.figure(figsize=(8, 5))
plt.plot(a_values, b_values, label=r'Nonlinear Function $b(a)$', color='black')
plt.plot(a_values, b_lin_values, label=r'Linear Approximation $b_{\text{lin}}(a)$', linestyle='dashed', color='blue')

# Highlight the operating point
plt.scatter(A, b_A, color='red', label='Operating Point $A$')

# Annotate the residual error
a_test = 2  # Example point where error is visible
plt.vlines(a_test, b_lin(a_test), b(a_test), linestyles='dotted', colors='red', label=r'Residual Error $r(a,A)$')

# Labels and legend
plt.xlabel(r'Input $a$')
plt.ylabel(r'Output $b(a)$')
plt.title('Linearization and Residual Error')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
