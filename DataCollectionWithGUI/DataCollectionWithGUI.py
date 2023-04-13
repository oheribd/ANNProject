import matplotlib
matplotlib.use("TkAgg")
import time
from time import sleep
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
import matplotlib.animation as animation
from matplotlib import  style
import serial
import numpy as np
import scipy.fftpack

data = []
adcData = serial.Serial('com3',1000000,timeout=1)
style.use("dark_background")
f = Figure(figsize=(1, 1), dpi=100)
g = f.add_subplot(111)

def Filter(data,fco):
    from scipy.signal import lfilter
    fs = 1000
    b = 20
    fl = fco-b/2
    fh = fco+b/2
    w = 40
    n = np.arange(-w, w + 1)
    h = (1 / (n * np.pi)) * (np.sin(fl / fs * 2 * np.pi * n) - np.sin(fh / fs * 2 * np.pi * n))
    h[w] = 1 - (fh / fs * 2 * np.pi - fl / fs * 2 * np.pi) / np.pi
    filtered_data = lfilter(h,1,data)
    return filtered_data

def animate(i):
    xList = []
    yList = []
    for n in range(500):
        while (adcData.inWaiting() == 0):  # Wait here until there is data
            pass  # do nothing
        try:
            emgData = float(adcData.readline().decode())
            xList.append(n * 0.001)
            yList.append(emgData)
            #print (emgData)
        except ValueError:
            print ("ValueError")

    yList = Filter(yList,100)
    yList = Filter(yList,50)
    offset = np.average(yList[100:500])
    yList = yList-offset
    g.clear()
    g.plot(xList[100:500], yList[100:500])
    g.set_yticks(np.arange(-2, 2.5, 0.5))
    g.grid(True)

class Main_Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_state('zoomed')
        self.configure(bg='#FFFFFF')
        self.title('DATA Logger')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage,LoggerPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        if frame == StartPage:
            close_animation(self)
            frame.tkraise()
        else:
            frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#B22222')
        p0 = tk.PanedWindow(self, bd=100, bg='#FFFFFF')
        p1 = tk.PanedWindow(self, bd=10, bg='#000000')
        p2 = tk.PanedWindow(p1, bg='#000000')
        p3 = tk.PanedWindow(p1, bd=10, bg='#000000')
        l1 = tk.Label(p0, text="Artificial Neural Network", font=("Arial", 80), fg='#000000', bg='#FFFFFF').pack()
        l2 = tk.Label(p0,
                      text=" for Muscular Signal Recognition in Device Controlling Application ",font=("Arial", 30), fg='#000000', bg='#FFFFFF').pack()
        l3 = tk.Label(p2, text="First Name", bd=10, font=("Arial", 20), fg='#FFFFFF', bg='#000000').grid(row=0,column=0,sticky=tk.W)
        e1 = tk.Entry(p2, width=20, font=("Arial", 18))
        e1.grid(row=0, column=1)
        l4 = tk.Label(p2, text="Last Name", bd=10, font=("Arial", 20), fg='#FFFFFF', bg='#000000').grid(row=1, column=0,sticky=tk.W)
        e2 = tk.Entry(p2, width=20, font=("Arial", 18))
        e2.grid(row=1, column=1)
        l5 = tk.Label(p2, text="ID Number", bd=10, font=("Arial", 20), fg='#FFFFFF', bg='#000000').grid(row=2, column=0,sticky=tk.W)
        e3 = tk.Entry(p2, width=20, font=("Arial", 18))
        e3.grid(row=2, column=1)
        b1 = tk.Button(p3, text="OK", font=("Arial", 19), bg='#7FFF00', fg='#000000', width=5, height=4, bd=5,command=lambda:registor(self)).pack()
        p0.pack(fill=tk.X)
        p1.pack()
        p2.grid(row=0, column=0)
        p3.grid(row=0, column=1)

        def registor(self):
            dbf = open('User.txt', 'a')
            dbf.write(e3.get()+','+e1.get()+','+e2.get()+'\n')
            dbf.close()
            e1.delete(0, tk.END)
            e2.delete(0, tk.END)
            e3.delete(0, tk.END)
            controller.show_frame(LoggerPage)

class LoggerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        var = tk.StringVar()
        var.set('                    ')
        p1 = tk.PanedWindow(self)
        p2 = tk.PanedWindow(self)
        l1 = tk.Label(p1, textvariable = var, font=("Arial", 19))
        b0 = tk.Button(p1, text="Test Signal", font=("Arial", 19), bg='#7FFF00', fg='#000000', width=10, bd=5,command=lambda: animate_start(self))
        b1 = tk.Button(p1, text="Record", font=("Arial", 19), bg='#FFFF00', fg='#000000', bd=5, command=lambda: switch_to_record(self,ani))
        b2 = tk.Button(p1, text="Back to Login", font=("Arial", 19), bg='#FF0000', fg='#FFFFFF', bd=5, command=lambda: animation_stop(self,ani))
        b0.grid(row=0,column=1)
        canvas = FigureCanvasTkAgg(f, p2)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        p1.pack()
        p2.pack(fill=tk.BOTH,expand=True)
        self.ani = None
        self.state = False
        def animate_start(self):
            if self.state == False:
                self.state = True
                l1.grid(row=0,column=0)
                b1.grid(row=0,column=2)
                b2.grid(row=0,column=3)
            global ani
            ani = animation.FuncAnimation(f, animate, interval=1)
            f.canvas.show()
            dbf = open('Data.txt', 'a')
            var.set('    Testing       ')

        def animation_stop(self,ani):
            ani.event_source.stop()
            var.set('                    ')
            p1.update_idletasks()
            controller.show_frame(StartPage)

        def switch_to_record(self,ani):
            ani.event_source.stop()
            dbf = open('Data.txt', 'a')
            record(dbf)

        def record(dbf):
            var.set('    Preparing       ')
            p1.update_idletasks()
            for i in range(3100):
                j = i+1
                while (adcData.inWaiting() == 0):  # Wait here until there is data
                    pass  # do nothing
                try:
                    emgData = float(adcData.readline().decode())
                    dbf.write(str(emgData)+',')
                except:
                    dbf.write(0 + ',')
                if j == 1100 :
                    var.set('       ACTIVE       ')
                    p1.update_idletasks()
                print(j)
            var.set('     THANK  YOU     ')
            p1.update_idletasks()
            dbf.write('\n')
            dbf.close()
            j=0

if __name__ == '__main__':
    app = Main_Application()
    app.mainloop()
