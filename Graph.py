import numpy as np
import matplotlib.pyplot as plt

# Define time
t = np.linspace(0, 2*np.pi, 1000)  # Time from 0 to 2π (one full cycle)

# Define voltage as a cosine wave
V = np.cos(t)  

# Capacitor: Current leads voltage by 90° (sin wave)
I_capacitor = np.sin(t)  

# Inductor: Current lags voltage by 90° (-sin wave)
I_inductor = -np.sin(t)  

# Plotting
plt.figure(figsize=(10,5))

# Plot capacitor voltage and current
plt.subplot(1,2,1)
plt.plot(t, V, label="Voltage (V)", color='blue')
plt.plot(t, I_capacitor, label="Current (I) - Capacitor", color='red', linestyle='dashed')
plt.title("Capacitor: Current Leads Voltage")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Plot inductor voltage and current
plt.subplot(1,2,2)
plt.plot(t, V, label="Voltage (V)", color='blue')
plt.plot(t, I_inductor, label="Current (I) - Inductor", color='green', linestyle='dashed')
plt.title("Inductor: Current Lags Voltage")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Show plot
plt.tight_layout()
plt.show()
# %%

