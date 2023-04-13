import numpy as np
import matplotlib.pyplot as plt
from unagi import Chan

class Sigmoid(Chan):
    def pai(self,a):
        self.h = 1/(1+np.exp(-a))
        return self.h

    def yon(self,g):
        return g*(1.-self.h)*self.h

def plot(f):
    a = np.linspace(-5,5,201)
    h = f.pai(a)
    plt.gca(aspect=1,xticks=range(-5,6),yticks=range(-5,6))
    plt.plot(a,h,'#eeaaaa',lw=3)
    plt.grid(ls=':')
    plt.show()

plot(Sigmoid())