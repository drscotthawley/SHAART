# Python Qt4 bindings for GUI objects
from PyQt5 import QtGui, QtWidgets

# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg \
import FigureCanvasQTAgg as FigureCanvas

# Matplotlib Figure object
from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib import cm 


import numpy as np

class SpectroCanvas(FigureCanvas):
      """Class to represent the FigureCanvas widget"""
      def __init__(self):
           # setup Matplotlib Figure and Axis
           self.fig = Figure()

           # initialization of the canvas
           FigureCanvas.__init__(self, self.fig)

           self.ax = self.fig.clear()
           self.ax = self.fig.add_subplot(111)
           self.fig.subplots_adjust(left=0.12,right=0.98,bottom=0.1, top=.97)

           # we define the widget as expandable
           FigureCanvas.setSizePolicy(self,
                                      QtWidgets.QSizePolicy.Expanding,
                                      QtWidgets.QSizePolicy.Expanding)
           # notify the system of updated policy
           FigureCanvas.updateGeometry(self)

class SpectroWidget(QtWidgets.QWidget):
      """Widget defined in Qt Designer"""
      def __init__(self, parent = None):
           # initialization of Qt MainWindow widget
           QtWidgets.QWidget.__init__(self, parent)

           # set the canvas to the Matplotlib widget
           self.canvas = SpectroCanvas()

           # create a vertical box layout
           self.vbl = QtWidgets.QVBoxLayout()

           # add spectro widget to vertical box
           self.vbl.addWidget(self.canvas)

           # add interactive navigation
           self.navi_toolbar = NavigationToolbar(self.canvas, self)
           self.vbl.addWidget(self.navi_toolbar)

           # set the layout to th vertical box
           self.setLayout(self.vbl)

      def update_graph(self,amp,sample_rate,colormap_choice=0):
           """Updates the graph with new data/annotations"""

           self.canvas.ax.clear()

           nsamples = len(amp)

           NFFT = 1024       # the length of the windowing segments

           if (0 == colormap_choice):
             colormap = cm.gist_heat
           elif (1 == colormap_choice):
             colormap = cm.gist_rainbow
           elif (2 == colormap_choice):
             colormap = cm.rainbow
           elif (3 == colormap_choice):
             colormap = cm.gray
           elif (4 == colormap_choice):
             colormap = cm.Blues
           elif (5 == colormap_choice):
             colormap = cm.gist_ncar


           Pxx, freqs, bins, im = self.canvas.ax.specgram(amp, NFFT=NFFT, Fs=1.0*sample_rate, noverlap=900
               #)#  ,cmap=cm.gray) 
               # ,cmap=cm.Blues)  # color map
                ,cmap=colormap)  # color map
 
           # Annotation
           self.canvas.ax.set_xlabel('Time (s)')
           self.canvas.ax.set_ylabel('Frequency (Hz) ')
           self.canvas.ax.axis([0,bins[-1],0,freqs[-1]])

           # Actually draw everything
           self.canvas.draw()



