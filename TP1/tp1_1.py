# Copyright (C) 2024 ABOU ORM Daniel
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation of the License.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# 
# For the full terms of the GNU GPL, please refer to the LICENSE.txt file.

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
def add_signals(signal1, signal2,signal3,signal4):
    return signal1 + signal2 +signal3+signal4
# Function to add one signal to another
def add_signalsBETA(signal1, signal2):
    return [signal1[i] + signal2[i] for i in range(len(signal1))]

def noise_white(x, mean=0.0, std_dev=1.0):
    """
    Generate a Gaussian noise signal (white noise) based on an existing time base.

    Parameters:
    - x: Array of time points (existing time base).
    - mean: Mean of the Gaussian distribution.
    - std_dev: Standard deviation of the Gaussian distribution.

    Returns:
    - x: The same input array of time points.
    - y: Array of noise values generated with Gaussian distribution.
    """
    y = np.random.normal(mean, std_dev, size=len(x))
    return x, y

def noise_impulse(x, num_impulses, impulse_interval, mean=0.0, std_dev=1.0):
    """
    Generate an impulsive noise signal based on an existing time base.

    Parameters:
    - x: Array of time points (existing time base).
    - num_impulses: Number of impulses to generate.
    - impulse_interval: Interval between impulses in terms of the number of samples.
    - mean: Mean amplitude of the impulses.
    - std_dev: Standard deviation of the impulse amplitudes.

    Returns:
    - x: The same input array of time points.
    - y: Array of impulsive noise values.
    """
    y = np.zeros_like(x)  # Initialize the noise signal with zeros
    for i in range(num_impulses):
        # Calculate the index for each impulse
        index = i * impulse_interval
        if index < len(x):
            # Generate an impulse with amplitude from a Gaussian distribution
            impulse_amplitude = np.random.normal(mean, std_dev)
            y[index] = impulse_amplitude
    return x, y
# Parameters
(a,f,fe,ph,d,sigma_noise)=(2,50,800,0,0.08,0.2)

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
#plt.show()

if __name__ == '__main__':
    pass