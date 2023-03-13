# Python Qt5 bindings for GUI objects
from PyQt6 import QtGui, QtWidgets

# import the Qt5Agg FigureCanvas object, that binds Figure to
# Qt5Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt5agg \
import FigureCanvasQTAgg as FigureCanvas

# Matplotlib Figure object
from matplotlib.figure import Figure

#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import scipy.signal as signal
import scipy
from os import path
import re


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




class PwrSpecCanvas(FigureCanvas):
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

class PwrSpecWidget(QtWidgets.QWidget):
      """Widget defined in Qt Designer"""
      def __init__(self, parent = None):
           # initialization of Qt MainWindow widget
           QtWidgets.QWidget.__init__(self, parent)

           # set the canvas to the Matplotlib widget
           self.canvas = PwrSpecCanvas()

           # create a vertical box layout
           self.vbl = QtWidgets.QVBoxLayout()

           # add pwrspec widget to vertical box
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

      def draw_graph(self,amp,samplerate,color="red"):
           """Updates the graph with new data/annotations"""

           print("pwrspec: Computing dB, amplength = ",len(amp))
           #fftlength = 16384
           #dB = 20.0*np.log10(np.abs(np.fft.rfft(amp,n=fftlength)))
#           dB = 20 * scipy.log10(scipy.absolute(scipy.fft(amp)))
           dB = 20.0*np.log10(np.abs(np.fft.rfft(amp)))   # this works the best
           print("pwrspec: finished Computing dB")
           graphsamples = len(dB)
           print("pwrspec computing f, graphsamples = ",graphsamples)
           f = np.linspace(0, samplerate/2.0, graphsamples)
           print("pwrspec finished computing f")

           if (graphsamples > 100000):
                graphsamples = 4096
           elif (graphsamples > 50000):
                graphsamples = 2048
           else:
                graphsamples = 1024
           graphsamples = len(dB)   #todo remove this
#           ds_dB,ds_f  = signal.resample(dB,graphsamples,f)
           ds_f,ds_dB  = my_resample(f,dB,graphsamples)

           maxval = np.max(ds_dB)
           ds_dB = [ x - maxval for x in ds_dB]
           minval = np.min(ds_dB)

           # Set up the plot
           p = self.canvas.ax.plot(ds_f, ds_dB,color=color,lw=1)

           self.canvas.ax.grid(True)
           self.canvas.ax.axis([10,ds_f[-1],minval,0])
           self.canvas.ax.set_xscale("log", nonpositive='clip')


           # Annotation
           self.canvas.ax.set_xlabel('Frequency (Hz)')
           self.canvas.ax.set_ylabel('Power (dB) ')

           print("leaving draw_graph")

           return p


      def update_graph(self,amp,samplerate,filenameA,ampB,samplerateB,filenameB):
           print("starting update_graph")
           self.canvas.ax.clear()
           p1, = self.draw_graph(amp,samplerate,"blue")
           leg_fA = self.legend_string(filenameA)

           if (ampB is not None) & (len(ampB) > 1):
              p2, = self.draw_graph(ampB,samplerateB,"purple")
              leg_fB = self.legend_string(filenameB)
              l1 = self.canvas.ax.legend([p1,p2], [leg_fA,leg_fB], loc=3)
           else:
              l1 = self.canvas.ax.legend([p1], [leg_fA], loc=3)

           l1.draw_frame(False)                   # no box around the legend

           # Actually draw everything
           self.canvas.draw()
           print("leaving update_graph")
