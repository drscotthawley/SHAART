# Python Qt5 bindings for GUI objects
from PyQt5 import QtGui, QtWidgets

# import the Qt5Agg FigureCanvas object, that binds Figure to
# Qt5Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt5agg \
import FigureCanvasQTAgg as FigureCanvas

# Matplotlib Figure object
from matplotlib.figure import Figure

from matplotlib import cm
import matplotlib.mlab as mlab
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar


import numpy as np
from mpl_toolkits.mplot3d import axes3d

#from scipy.misc import imresize
from scipy import ndimage


global color_axial, color_tangential, color_oblique
color_axial = 'r'
color_tangential = 'b'
color_oblique = 'purple'




class ModeGraphCanvas(FigureCanvas):
      """Class to represent the FigureCanvas widget"""
      def __init__(self):
           # setup Matplotlib Figure and Axis
           self.fig = Figure()

           # initialization of the canvas
           FigureCanvas.__init__(self, self.fig)

           self.ax = self.fig.clear()
           self.ax = self.fig.add_subplot(111)
           self.fig.subplots_adjust(left=0.12,right=0.98,bottom=0.105, top=.92)


           # we define the widget as expandable
           FigureCanvas.setSizePolicy(self,
                                      QtWidgets.QSizePolicy.Expanding,
                                      QtWidgets.QSizePolicy.Expanding)
           # notify the system of updated policy
           FigureCanvas.updateGeometry(self)


class ModeGraphWidget(QtWidgets.QWidget):
      """Widget defined in Qt Designer"""
      def __init__(self, parent = None):
           # initialization of Qt MainWindow widget
           QtWidgets.QWidget.__init__(self, parent)

           # set the canvas to the Matplotlib widget
           self.canvas = ModeGraphCanvas()

           # create a vertical box layout
           self.vbl = QtWidgets.QVBoxLayout()

           # add mode graph widget to vertical box
           self.vbl.addWidget(self.canvas)

           # add interactive navigation
           self.navi_toolbar = NavigationToolbar(self.canvas, self)
           self.vbl.addWidget(self.navi_toolbar)


           # set the layout to th vertical box
           self.setLayout(self.vbl)


      def plot_mode(self, f0, deltaf, modetype, sums):
           n = 200
           fplothalfwidth = 2.5*deltaf
           fstart = f0 - fplothalfwidth
           fend   = f0 + fplothalfwidth
           df = 2*fplothalfwidth / n
           f = np.arange( fstart, fend+df, df)
        #   modeshape = np.exp(-((f-f0)/deltaf)**2)      # gaussian
           dB = -10*((f-f0)/deltaf)**2      # log of a gaussian is a parabola
           if (2 == modetype):            # axial modes
             colorstr = color_axial
             dB = [x + 1 for x in dB]
           elif (1 == modetype):          # tangential modes
             colorstr = color_tangential
           else:                          # oblique modes
             colorstr = color_oblique
             dB = [x - 1 for x in dB]

           modeshape = [10.0**x for x in dB]

           #line, = ax.plot(f, np.ma.log10(modeshape), colorstr)  # plot the mode shape itself
           # make a tiny tick mark for the mode

           ticklen = 2
           tickfs = [f0,f0]
           if0 = len(f)/2
           tickstart = 7 - 2*modetype
           tickps = [tickstart, tickstart + ticklen]
           line2, = self.canvas.ax.plot(tickfs, tickps, colorstr)  # draw a tick at the mode frequency

           if sums is not None:
              #ifsave = 0           # this was used to prevent double-counting #TODO: <--- This is wrong! Double counting is good!
              for i in range(len(f)):
                  ifreq = int(f[i])
                  if (ifreq > 0) & (ifreq < len(sums)):
                     #if (ifreq != ifsave):
                     sums[ifreq] = sums[ifreq] + modeshape[i]
                     #ifsave = ifreq




      def update_graph(self,modes,X,Y,Z):
           """Updates the graph with new data/annotations"""
           nmodes = len(modes)
           self.canvas.ax.clear()


           sum_fmax =250
           dB_min = -30
           dB_max = 10
           sums = np.zeros(sum_fmax)

           for m in modes:
               numzeros = m.count(0)
               f0 = m[0]
               rt60 = 0.4
               deltaf = 2.2/rt60
               self.plot_mode(f0, deltaf, numzeros, sums)


           line2, = self.canvas.ax.plot(range(len(sums)), np.ma.log10(sums), 'k')

           pl = self.canvas.ax

           # Global Plot characteristics
           pl.axis([0,sum_fmax,dB_min,dB_max])
           self.canvas.ax.set_xlabel('Frequency (Hz)')
           self.canvas.ax.set_ylabel('Relative sound-pressure level (dB)')
           title = "Theoretical Steady-State Room Response"
           self.canvas.ax.set_title(title)
           pl.grid(True)

           # cheap hack to make a legend
           xs = [sum_fmax]
           ys = [dB_min]
           pA, = self.canvas.ax.plot(xs,ys,color=color_axial)
           pB, = self.canvas.ax.plot(xs,ys,color=color_tangential)
           pC, = self.canvas.ax.plot(xs,ys,color=color_oblique)
           l1 = self.canvas.ax.legend([pA,pB,pC], ['axial modes','tangential modes','oblique modes'], loc=4)
           l1.draw_frame(False)                   # no box around the legend



           """Actually draw everything"""
           self.canvas.draw()
