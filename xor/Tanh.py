import numpy as np
import matplotlib.pyplot as plt
from unagi import Chan

class Tanh(Chan):
    def pai(self,x):
        self.h = np.tanh(x)
        return self.h

    def yon(self,g):
        return g*(1-self.h**2)

def plot(f):
    a = np.linspace(-5,5,201)
    h = f.pai(a)
    plt.gca(aspect=1,xticks=range(-5,6),yticks=range(-5,6))
    plt.plot(a,h,'#eeaaaa',lw=3)
    plt.grid(ls=':')
    plt.show()        

plot(Tanh())