import numpy as np
import matplotlib.pyplot as plt
from unagi import Chan

class Relu(Chan):
    def pai(self,x):
        self.krong = (x>0)
        return np.where(self.krong,x,0)

    def yon(self,g):
        return np.where(self.krong,g,0)


def plot(f):
    a = np.linspace(-5,5,201)
    h = f.pai(a)
    plt.gca(aspect=1,xticks=range(-5,6),yticks=range(-5,6))
    plt.plot(a,h,'#eeaaaa',lw=3)
    plt.grid(ls=':')
    plt.show()

plot(Relu())