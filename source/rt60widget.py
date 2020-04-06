# Python Qt4 bindings for GUI objects
from PyQt5 import QtGui, QtWidgets

from matplotlib.backends.backend_qt4agg \
import FigureCanvasQTAgg as FigureCanvas

# Matplotlib Figure object
from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import scipy.signal as signal
import re
from os import path
import math


def my_resample(x,newnum,y):

  method = 0

  if (0==method):
     if (len(y) != len(x)):
         print("my_resample: Error: lengths of x and y are not equal!")
     # pad signal such that its length is a power of 2 = much faster
     orig_len = len(x)
     p2_len = int(math.pow(2, math.ceil(math.log(orig_len)/math.log(2))))
     x3 = np.zeros(p2_len)
     y3 = np.zeros(p2_len)
     x3[0:orig_len-1] = x[0:orig_len-1]
     y3[0:orig_len-1] = y[0:orig_len-1]
     x2, y2  = signal.resample(x3,newnum*p2_len//orig_len,y3)
     x2 = x2[0:newnum-1]
     y2 = y2[0:newnum-1]
  else:
     newnum = int(newnum)
     num = len(x)
     stride = int(num / newnum)
     x2 = np.zeros(newnum)
     y2 = np.zeros(newnum)
     i = 0
     for i2 in range(0,newnum):
         i = i2*stride
         x2[i2] = x[i]
         y2[i2] = y[i]
  return x2, y2



class Rt60Canvas(FigureCanvas):
      """Class to represent the FigureCanvas widget"""
      def __init__(self):
           # setup Matplotlib Figure and Axis
           self.fig = Figure()

           # initialization of the canvas
           FigureCanvas.__init__(self, self.fig)

           self.ax = self.fig.clear()
           self.ax = self.fig.add_subplot(111)
           self.fig.subplots_adjust(left=0.08,right=0.98,bottom=0.105, top=.92)


           # we define the widget as expandable
           FigureCanvas.setSizePolicy(self,
                                      QtWidgets.QSizePolicy.Expanding,
                                      QtWidgets.QSizePolicy.Expanding)
           # notify the system of updated policy
           FigureCanvas.updateGeometry(self)

class Rt60Widget(QtWidgets.QWidget):
      """Widget defined in Qt Designer"""
      def __init__(self, parent = None):
           # initialization of Qt MainWindow widget
           QtWidgets.QWidget.__init__(self, parent)

           # set the canvas to the Matplotlib widget
           self.canvas = Rt60Canvas()

           # create a vertical box layout
           self.vbl = QtWidgets.QVBoxLayout()

           # add rt60 widget to vertical box
           self.vbl.addWidget(self.canvas)

           # add interactive navigation
           self.navi_toolbar = NavigationToolbar(self.canvas, self)
           self.vbl.addWidget(self.navi_toolbar)

           # bind events related to drawing lines
           self.canvas.mpl_connect('button_press_event', self.on_press)
           self.canvas.mpl_connect('button_release_event', self.on_release)
           self.canvas.mpl_connect('motion_notify_event', self.on_motion)

           # set the layout to th vertical box
           self.setLayout(self.vbl)

           # no buttons pressed
           self.press = None

           # the line that users get to draw
           self.linex = [0]
           self.liney = [0]
           self.line, = self.canvas.ax.plot(self.linex, self.liney)
           self.line.set_color("red")
           self.line.set_linewidth(1.5)
           self.line.set_linestyle('-')

           # initialize annotation
           self.status_text = self.canvas.ax.text(0.45, 0.9, '', transform=self.canvas.ax.transAxes,size=14,ha='center')

      def legend_string(self,instr):
           instr = "%s" % instr           # just to make sure it's of the right 'type'
           outstr = path.basename(instr)
           match = re.match(r"(.*)\.wav",outstr)    # take out the .wav if possible
           if (match is not None):
              outstr = match.group(1)
           return outstr

      def refresh(self):  # some code taken from init
           self.canvas.ax.clear()

           # the line that users get to draw
           self.line, = self.canvas.ax.plot(self.linex, self.liney)
           self.line.set_color("red")
           self.line.set_linewidth(2.0)
           self.line.set_linestyle('-')

           ## initialize annotation
           self.status_text = self.canvas.ax.text(0.45, 0.9, '', transform=self.canvas.ax.transAxes,size=14,ha='center')


      def on_press(self, event):
           'on button press we will start drawing a line'
           #unless we're in pan or zoom interactive mode
           mode = self.canvas.ax.get_navigate_mode()
           if ((mode != 'ZOOM') & (mode != 'PAN')):
               x0, y0 = event.xdata, event.ydata
               self.press = x0, y0

      def on_motion(self, event):
           'on motion we will draw the line '
           if self.press is None: return
           x0, y0 = self.press
           x = x0, event.xdata
           y = y0, event.ydata

           self.line.set_data(x, y)   # this sets up the line to be drawn
           self.linex = x
           self.liney = y

           if (y[1] != y[0]):
               rt60 = -60.0*(x[1]-x[0])/(1.0*y[1]-y[0])
               status_template = 'RT60 = %.2f s'
               self.status_text.set_text(status_template%(rt60))
               self.line.figure.canvas.draw()   # update the canvas

      def on_release(self, event):
           '''on release we reset the press data'''
           self.press = None
           mode = self.canvas.ax.get_navigate_mode()
           # undo any zoom effects
           if ('ZOOM' == mode):
              self.navi_toolbar.zoom()
           return

      def disconnect(self):
           '''disconnect all the stored connection ids'''
           self.line.figure.canvas.mpl_disconnect(self.cidpress)
           self.line.figure.canvas.mpl_disconnect(self.cidrelease)
           self.line.figure.canvas.mpl_disconnect(self.cidmotion)

      def update_graph(self,amp,t,filenameA,ampB,tB, filenameB):
        """Updates the graph with new data/annotations"""

        epsilon = 1.0e-8     # added to avoid log(0) errors

        # Compute the quantity to be plotted
        power = (amp + epsilon) **2
        maxval = 1.0*np.max(power)
        power = power / maxval
        dB = 10*np.ma.log10(np.abs(power))   # "ma"=masked array, throws out -Inf values


        # Downsample for plotting purposes.  (otherwise the plotting takes forever)
        nsamples = len(dB)
        if (nsamples > 100000):
           plotsamples = 2048
        elif (nsamples > 50000):
           plotsamples = 2048
        else:
           plotsamples = 1024
        ds_dB, ds_t  = my_resample(dB,plotsamples,t)

        # Set up the plot
        self.refresh()
        p1, = self.canvas.ax.plot(ds_t, ds_dB,color="blue",lw=1)
        leg_fA = self.legend_string(filenameA)

        # second file
        if (filenameB is not "") and (ampB is not None) and (len(ampB) > 1):
           powerB = (ampB+epsilon)**2
           powerB = powerB / maxval   # use same max value as for file A
           dB_B = 10*np.ma.log10(np.abs(powerB))   # "ma"=masked array, throws out -Inf values
           # Downsample for plotting purposes.  (otherwise the plotting takes forever)
           nsamplesB = len(dB_B)
           if (nsamplesB > 100000):
              plotsamplesB = 4096
           elif (nsamplesB > 50000):
              plotsamplesB = 2048
           else:
              plotsamplesB = 1024
           ds_dB_B,ds_t_B  = signal.resample(dB_B,plotsamplesB,tB)
           p2, = self.canvas.ax.plot(ds_t_B, ds_dB_B,color="purple",lw=1)
           leg_fB = self.legend_string(filenameB)
           l1 = self.canvas.ax.legend([p1,p2], [leg_fA,leg_fB], loc=1)
        else:
           l1 = self.canvas.ax.legend([p1], [leg_fA], loc=1)

        l1.draw_frame(False)                   # no box around the legend
        self.canvas.ax.grid(True)

        #draw the line again, on top
        self.line, = self.canvas.ax.plot(self.linex, self.liney)
        self.line.set_data(self.linex, self.liney)
        self.line.set_color("red")
        self.line.set_linewidth(2.0)
        self.line.set_linestyle('-')
        self.line.figure.canvas.draw()

        # Annotation
        self.canvas.ax.set_xlabel('Time (s)')
        self.canvas.ax.set_ylabel('Power (dB) ')

        # Actually draw everything
        self.canvas.draw()
