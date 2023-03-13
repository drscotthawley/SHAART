# Python Qt bindings for GUI objects
from PyQt6 import QtGui, QtWidgets

# import the Qt5Agg FigureCanvas object, that binds Figure to
# Qt5Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt5agg \
import FigureCanvasQTAgg as FigureCanvas

# Matplotlib Figure object
from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import scipy.signal as signal
from os import path
import re
import scipy.signal.signaltools as sigtool



def my_resample(x,y,newnum):
  num = len(x)
  stride = int(num / newnum)
  x2 = np.zeros(newnum)
  y2 = np.zeros(newnum)
  i = 0
  for i2 in range(0,newnum):
      x2[i2] = x[i]
      y2[i2] = y[i]
      i = i+stride
  return x2, y2




class WaveformCanvas(FigureCanvas):
      """Class to represent the FigureCanvas widget"""
      def __init__(self):
           # setup Matplotlib Figure and Axis
           self.fig = Figure()

           # initialization of the canvas
           FigureCanvas.__init__(self, self.fig)

           self.ax = self.fig.clear()
           self.ax = self.fig.add_subplot(111)
           self.fig.subplots_adjust(left=0.09,right=0.98,bottom=0.13, top=.97)


           # we define the widget as expandable
           FigureCanvas.setSizePolicy(self,
                                      QtWidgets.QSizePolicy.Policy.Expanding,
                                      QtWidgets.QSizePolicy.Policy.Expanding)
           # notify the system of updated policy
           FigureCanvas.updateGeometry(self)

class WaveformWidget(QtWidgets.QWidget):
      """Widget defined in Qt Designer"""
      def __init__(self, parent = None):
           # initialization of Qt MainWindow widget
           QtWidgets.QWidget.__init__(self, parent)

           # set the canvas to the Matplotlib widget
           self.canvas = WaveformCanvas()

           # create a vertical box layout
           self.vbl = QtWidgets.QVBoxLayout()

           # add waveform widget to vertical box
           self.vbl.addWidget(self.canvas)

           # add interactive navigation
           self.navi_toolbar = NavigationToolbar(self.canvas, self)
           self.vbl.addWidget(self.navi_toolbar)

           # set the layout to th vertical box
           self.setLayout(self.vbl)

      def legend_string(self,instr):
           instr = "%s" % instr           # just to make sure it's of the right 'type'
           outstr = path.basename(instr)
           match = re.match(r"(.*)\.wav",outstr)    # take out the .wav if possible
           if (match is not None):
              outstr = match.group(1)
           return outstr

      def draw_graph(self,amp,t,color="red",abs_checked=0, env_checked=0):
           """Updates the graph with new data/annotations"""

           nsamples = len(amp)
           if (nsamples > 100000):
              plotsamples = 4096
           elif (nsamples > 50000):
              plotsamples = 2048
           else:
              plotsamples = 1024

           ds_t,ds_amp  = my_resample(t,amp,plotsamples)

           maxval = np.max(ds_amp)
           minval = np.min(ds_amp)

           if abs_checked:
                ds_amp = np.abs(ds_amp)

           if env_checked:
                env = np.abs(sigtool.hilbert(ds_amp))
                ds_amp = env
                #ds_t = np.arange(0,len(env),t[1])


           # Set up the plot
           p = self.canvas.ax.plot(ds_t, ds_amp,color=color,lw=1)

           self.canvas.ax.grid(True)


           # Annotation
           self.canvas.ax.set_xlabel('Time (s)')
           self.canvas.ax.set_ylabel('Displacement')

           return p


      def update_graph(self,amp,t,filenameA,ampB,tB,filenameB,abs_checked=0, env_checked=0):
           self.canvas.ax.clear()
           p1, = self.draw_graph(amp,t,"blue",abs_checked,env_checked)
           leg_fA = self.legend_string(filenameA)

           if (ampB is not None) & (len(ampB) > 1):
              p2, = self.draw_graph(ampB,tB,"purple",abs_checked,env_checked)
              leg_fB = self.legend_string(filenameB)
              l1 = self.canvas.ax.legend([p1,p2], [leg_fA,leg_fB], loc=3)
           else:
              l1 = self.canvas.ax.legend([p1], [leg_fA], loc=3)

           l1.draw_frame(False)                   # no box around the legend

           # Actually draw everything
           self.canvas.draw()
