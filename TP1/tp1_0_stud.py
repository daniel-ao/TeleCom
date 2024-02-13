'''
File : tp1_0_stud.py

Creer un signal numerique et l'afficher
RMQ : On utilise ici le B,A,BA de Python. 

     Si vous savez faire mieux : objets ?, numpy ? ... SURTOUT lachez vous !!!!!
     car la solution "pythonique" n'est pas là :-( 
'''

import math
import random
import matplotlib.pyplot as plt 

#---------------------------------------

def func_sin(t, a, f, ph):
    return a * math.sin((2 * math.pi * f * t) + ph)

def func_square(t, a, f, ph):
    value = math.sin(2 * math.pi * f * t + ph)
    return a * (1 if value >= 0 else -1)

def func_sawtooth(t, a, f, ph):
    T = 1 / f
    # Adjust the phase by pi to start at the bottom of the wave
    return 2 * a * ((t / T) - math.floor((t / T)) -1/2)

def func_triangle(t, a, f, ph):
    T = 1 / f
    # The phase shift is incorporated into the time calculation
    # The formula for the triangle wave adjusted to start at the correct phase
    return a * (4 * (abs(t/T - math.floor(t/T + 1/2))) - 1)

def make_signal(a, f, fe, ph, d, func):
    """
    Create a synthetic signal
    """
    N = int(d * fe)
    te = 1.0 / fe
    
    sig_t = [] 
    sig_s = []
    for i in range(N):
        t = te * i
        sig_t.append(t)
        sig_s.append(func(t, a, f, ph))
        
    return sig_t, sig_s
   
   # Generate Gaussian noise

#---------------------------------------

def plot_on_ax(ax, inx, iny, label, format='-bo'):
    ax.plot(inx,iny,format,label=label)
    ax.set_xlabel('time (s)')
    ax.set_ylabel('voltage (V)')

def decorate_ax(ax, title):
    ax.set_title(title)
    ax.grid(True)
    ax.legend()

#=======================================

def q1():
        (a,f,fe,ph,d)=(2,50,1000,0,0.08)
        # Generation du signal
        x,y=make_signal(a,f,fe,ph,d,func_sin)

        # Representation graphique
        _,ax = plt.subplots()
        legend_label = "Sin Wave : a={}, f={}, fe={}, ph={}, d={}".format(a, f, fe, ph, d)
        plot_on_ax(ax, x, y, legend_label,format='g*--')
        decorate_ax(ax,"Une sinusoide")

        plt.savefig("./basic_sin.png")
        plt.show()
    
def q2():
        # Parameters for the first sine wave (s1)
        (a1,f1,fe1,ph1,d1) = (1.4,50,500,0,0.04)

        # Parameters for the second sine wave (s2)
        (a2,f2,fe2,ph2,d2) = (0.5,50,1000,math.pi,0.04)

        # Create the figure and axes
        _, ax = plt.subplots()

        ((x1,y1),(x2,y2))=(make_signal(a1,f1,fe1,ph1,d1,func_sin)
                           ,make_signal(a2,f2,fe2,ph2,d2,func_sin))   

        # Plot the first sine wave with blue circles
        ax.plot(x1, y1, '-bo', linestyle='',markersize=6)  # No lines

        # Plot the second sine wave with red dots
        ax.plot(x2, y2, 'ro', linestyle='',markersize=4)  # No lines

        # Set the x-axis limit to match the left graph
        ax.set_xlim(0, 0.04)

        # Add the legend autoamtically
        (legend_label1,legend_label2) = ((f"s1 : f={f1}, fe={fe1}, ph={ph1}") , 
                                         (f"s2 : f={f2}, fe={fe2}, ph={ph2:.2f}"))
        ax.legend([legend_label1, legend_label2])

        # Add labels and title
        ax.set_xlabel('time (s)')
        ax.set_ylabel('voltage (V)')
        ax.set_title('Deux sinusoides')
        ax.grid(True)
        # Display the plot
        plt.show()

def q3a():
    # Define parameters for the square wave
    (a,f,fe,phi,d)=(3,50,800,0,0.08)
    # Generate square wave
    t, s = make_signal(a, f, fe, phi, d, func_square)

    t, s = make_signal(a, f, fe, phi, d, func_square)

    # Create the figure and axes
    _, ax = plt.subplots()

    # Plot the square wave using the plot_on_ax function
    legend_label = f"Square Wave: a={a}, f={f}, fe={fe}"
    plot_on_ax(ax, t, s, legend_label, format='-bo')  # Adjust the format as needed

    # Decorate the axes with the decorate_ax function
    decorate_ax(ax, "Un carre")

    # Display the plot
    plt.show()

def q3b():
    (a,f,fe,ph,d)=(3,50,250000,0,0.08) # Define parameters for the sawtooth wave
    t_sawtooth, s_sawtooth = make_signal(a, f, fe, ph, d, func=func_sawtooth)

    plt.plot(t_sawtooth, s_sawtooth, '-bo')
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title('Une dent de scie')
    legend_label1 =(f"f={f}, fe={fe}, ph={ph:.2f}")
    plt.legend([legend_label1])
    plt.grid(True)
    plt.show()
   
def q3c():
    # To create a triangle wave
    (a,f,fe,ph,d)=(3,50,800,0,0.08)
    t_triangle, s_triangle = make_signal(a, f, fe, ph, d, func=func_triangle)
    plt.plot(t_triangle, s_triangle, '-bo')
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title('Un triangle')
    legend_label1 = (f"f={f}, fe={fe}, ph={ph}")
    plt.legend([legend_label1])
    plt.grid(True)
    plt.show()   


if __name__ == '__main__':
    # Ask the user to input their choice
    user_choice = input("Choose an option (q1, q2, q3a, q3b): ")

    # Check the user's choice and execute the corresponding block of code
    if user_choice == 'q1':
        q1()
    elif user_choice == 'q2':
        q2()
    elif user_choice == 'q3a':
        q3a()
    elif user_choice == 'q3b':
        q3b()
    elif user_choice == 'q3c':
        q3c()
    else:
        '''q1()
        q2()
        q3a()
        q3b()
        q3c()'''
        print("All the questions")
