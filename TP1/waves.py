import struct
import wave
import math

# Assuming tp1_0 and noise are custom modules that you have created or been provided with
import tp1_0_stud
import tp1_1

def write_a_wave_file(x, y, fn="son.wav"):
    nbCanal = 2  # stereo
    nbOctet = 1  # size of a sample: 1 byte = 8 bits
    fe = 44100  # sampling frequency
    nbEchantillon = len(x)  # number of samples
    
    wave_file = wave.open(fn, 'w')
    parametres = (nbCanal, nbOctet, fe, nbEchantillon, 'NONE', 'not compressed')
    wave_file.setparams(parametres)
    
    for i in range(nbEchantillon):
        val = y[i]
        if val > 1.0:
            val = 1.0
        elif val < -1.0:
            val = -1.0
        val = int(127.5 + 127.5 * val)
        try:
            # 'BB' indicates unsigned char, for stereo the same value is used for both channels
            fr = struct.pack('BB', val, val)
        except struct.error as err:
            print(err)
            print(f"Sample {i} = {y[i]}/{val}")
        wave_file.writeframes(fr)
    
    wave_file.close()

def make_anoisysignal(a, f, fe, ph, d):
    x1, y1 = tp1_0_stud.make_sin(a, f, fe, ph, d)
    m = 0.0  # mean
    e = 0.05  # standard deviation
    x2, y2 = tp1_1.noise_white(x1, m, e)
    m1 = 0.0  # mean
    e1 = 1.6 * a  # standard deviation
    x3, y3 = tp1_1.noise_impulse(2, 1000, x1, m1, e1)
    x4, y4 = tp1_1.signal_add(x1, y1, x2, y2)
    x4, y4 = tp1_1.signal_add(x4, y4, x3, y3)
    return x4, y4

if __name__ == '__main__':
    # Generate the noisy signal
    x, y = make_anoisysignal(a=0.2, f=440.0, fe=44100.0, ph=0, d=5)
    
    # Write the noisy signal to a WAV file
    write_a_wave_file(x, y)
