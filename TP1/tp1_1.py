import math
import random
import matplotlib.pyplot as plt
import numpy as np 
import tp1_0_stud

# Function to generate Gaussian noise
def generate_gaussian_noise(time_array, sigma):
    return np.random.normal(0, sigma, len(time_array))

# Function to generate impulsive noise
def generate_impulsive_noise(time_array, magnitude, frequency):
    noise = np.zeros(len(time_array))
    for i in range(len(time_array)):
        if random.random() < frequency:
            noise[i] = random.choice([-1, 1]) * magnitude
    return noise

# Function to add one signal to another
def add_signals(signal1, signal2):
    return signal1 + signal2
# Function to add one signal to another
def add_signalsBETA(signal1, signal2):
    return [signal1[i] + signal2[i] for i in range(len(signal1))]

# Parameters for the signals
a = 2.0  # Amplitude of the sinusoidal signal
f = 50.0  # Frequency of the sinusoidal signal
fe = 800.0  # Sampling frequency
d = 0.08  # Duration of the signals
ph = 0  # Phase of the sinusoidal signal
sigma_noise = 0.2  # Standard deviation of the Gaussian noise

# Generate the time base
time_base = np.linspace(0, d, int(fe * d))

# Generate the sinusoidal signal
_,sinusoidal_signal = tp1_0_stud.make_signal(a, f, fe, ph, d, tp1_0_stud.func_sin)

# Generate Gaussian noise
gaussian_noise = generate_gaussian_noise(time_base, sigma_noise)

# Generate impulsive noise
impulsive_noise = generate_impulsive_noise(time_base, magnitude=0.5, frequency=0.05)

# Combine the sinusoidal signal with Gaussian noise
noisy_signal = add_signalsBETA(sinusoidal_signal, gaussian_noise)

# Plot the results
plt.figure(figsize=(15, 10))

# Plot clean sinusoidal signal
plt.subplot(4, 1, 1)
plt.plot(time_base, sinusoidal_signal, '-bo', label='Sinusoidal Signal')
plt.title('Clean Sinusoidal Signal')
plt.legend()

# Plot Gaussian noise signal
plt.subplot(4, 1, 2)
plt.plot(time_base, gaussian_noise, 'g-', label='Gaussian Noise')
plt.title('Gaussian Noise Signal')
plt.legend()

# Plot impulsive noise signal
plt.subplot(4, 1, 3)
plt.plot(time_base, impulsive_noise, 'g-', label='Impulsive Noise')
plt.title('Impulsive Noise Signal')
plt.legend()

# Plot sinusoidal signal with Gaussian noise
plt.subplot(4, 1, 4)
plt.plot(time_base, noisy_signal, 'm-', label='Sinusoidal Signal with Gaussian Noise')
plt.title('Sinusoidal Signal with Gaussian Noise')
plt.legend()

# Adjust layout
plt.tight_layout()
plt.show()

if __name__ == '__main__':
    pass