# Python Qt5 bindings for GUI objects
from PyQt6 import QtGui, QtWidgets

# import the Qt5Agg FigureCanvas object, that binds Figure to
# Qt5Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt5agg \
import FigureCanvasQTAgg as FigureCanvas

# Matplotlib Figure object
from matplotlib.figure import Figure


import numpy as np
from mpl_toolkits.mplot3d import axes3d

#from scipy.misc import imresize
from scipy import ndimage


class WaterCanvas(FigureCanvas):
      """Class to represent the FigureCanvas widget"""
      def __init__(self):
           # setup Matplotlib Figure and Axis
           self.fig = Figure()

           # initialization of the canvas
           FigureCanvas.__init__(self, self.fig)

           self.ax = self.fig.add_subplot(111, projection='3d')
           self.fig.subplots_adjust(left=0,right=1.0,bottom=0, top=1.0)

           # we define the widget as expandable
           FigureCanvas.setSizePolicy(self,
                                      QtWidgets.QSizePolicy.Policy.Expanding,
                                      QtWidgets.QSizePolicy.Policy.Expanding)
           # notify the system of updated policy
           FigureCanvas.updateGeometry(self)

class WaterWidget(QtWidgets.QWidget):
      """Widget defined in Qt Designer"""
      def __init__(self, parent = None):
           # initialization of Qt MainWindow widget
           QtWidgets.QWidget.__init__(self, parent)

           # set the canvas to the Matplotlib widget
           self.canvas = WaterCanvas()

           # create a vertical box layout
           self.vbl = QtWidgets.QVBoxLayout()

           # add water widget to vertical box
           self.vbl.addWidget(self.canvas)

           # set the layout to th vertical box
           self.setLayout(self.vbl)


      def update_graph(self,amp,sample_rate):
           """Updates the graph with new data/annotations"""

           from matplotlib import cm # lazy loading
           import matplotlib.mlab as mlab 

           nsamples = len(amp)
           NFFT = 1024       # the length of the windowing segments
           """ The next line creates a spectrogram but doesn't draw it."""
           Pxx, f, t = mlab.specgram(amp,NFFT=NFFT, Fs=1.0*sample_rate, noverlap=900)
           #Pxx, f, t = mlab.specgram(amp, Fs=1.0*sample_rate)
           image = np.row_stack(Pxx)
           image = ndimage.gaussian_filter(image, 3)

           """convert the spectrogram into the type of 2D-array(s) that can be plotted"""
           dt = t[1]-t[0]
           df = f[1]-f[0]
           x = [ a*dt for a in range(image.shape[1])]     # times
           y = [ a*df for a in range(image.shape[0])]     # frequencies
           X,Y = np.meshgrid(x,y)
           Z = 10.0*np.log10(image)                       # log scale for intensity
           maxval = np.max(Z)
           Z = np.array([ x - maxval for x in Z])                   # normalize to zero dB
           #print "X.shape = ", X.shape, ", Y.shape = ", Y.shape #, ", Z.shape = ", Z.shape

           """A form of downsampling: set the 'stride' when plotting, for cris-crossy lines"""
           cstride = 10            # stride in time indices
           rstride = X.shape[0]    # stride in frequency indices
           maxn = 1000  # say we can reasonably handle a maxn values, beyond that, we reduce
           if X.shape[1] > maxn:  cstride = 10* X.shape[1] // maxn
          # self.canvas.ax.plot_surface(X,Y,Z,rstride=rstride, cstride=cstride, alpha=1.0, cmap=cm.Blues)
           self.canvas.ax.plot_surface(X,Y,Z,rstride=rstride, cstride=cstride, cmap=cm.Blues)

           self.canvas.ax.set_xlabel('Time (s)')
           self.canvas.ax.set_ylabel('Freq (Hz)')
           self.canvas.ax.set_zlabel('Power (dB)')

           """Actually draw everything"""
           self.canvas.draw()
