# Sabine Equation / Room simulation tab

# Python Qt4 bindings for GUI objects
from PyQt5 import QtGui, QtWidgets

# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg \
import FigureCanvasQTAgg as FigureCanvas

# Matplotlib Figure object
from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import scipy.signal as signal


class RcGraphCanvas(FigureCanvas):
      """Class to represent the FigureCanvas widget"""
      def __init__(self):
           # setup Matplotlib Figure and Axis
           self.fig = Figure()

           # initialization of the canvas
           FigureCanvas.__init__(self, self.fig)

           self.ax = self.fig.clear()
           self.ax = self.fig.add_subplot(111)
           self.fig.subplots_adjust(left=0.1,right=0.95,bottom=0.13, top=.97)


           # we define the widget as expandable
           FigureCanvas.setSizePolicy(self,
                                      QtWidgets.QSizePolicy.Expanding,
                                      QtWidgets.QSizePolicy.Expanding)
           # notify the system of updated policy
           FigureCanvas.updateGeometry(self)

class RcGraphWidget(QtWidgets.QWidget):
      """Widget defined in Qt Designer"""
      def __init__(self, parent = None):
           # initialization of Qt MainWindow widget
           QtWidgets.QWidget.__init__(self, parent)
 
           # set the canvas to the Matplotlib widget
           self.canvas = RcGraphCanvas()

           # create a vertical box layout
           self.vbl = QtWidgets.QVBoxLayout()

          # # add rt60 widget to vertical box
           self.vbl.addWidget(self.canvas)

           # add interactive navigation
           self.navi_toolbar = NavigationToolbar(self.canvas, self)
           self.vbl.addWidget(self.navi_toolbar)

           # set the layout to th vertical box
           self.setLayout(self.vbl)


           #Absorption coefficients, in Sabines/ft^2
           self.abs_freqs   =  np.array([125.0,  500.0,  1000.0, 2000.0])  # in Hz
           abs_concrete = np.array([0.01, 0.02, 0.02, 0.02])       
           abs_glass    = np.array([0.19, 0.06, 0.04, 0.03])      
           abs_plaster  = np.array([0.20, 0.10, 0.08, 0.04])     
           abs_plywood  = np.array([0.45, 0.13, 0.11, 0.10])
           abs_carpet   = np.array([0.10, 0.30, 0.35, 0.50])
           abs_curtains = np.array([0.05, 0.25, 0.35, 0.40])
           abs_acousbrd = np.array([0.25, 0.80, 0.90, 0.90])
           self.sab_adult = np.array([3.0, 4.5, 5.0, 5.2])    # Just Sabines

           # Note this is 2d-array
           self.abs_coeffs =  np.array([ abs_concrete, abs_glass, abs_plaster, abs_plywood, \
                                         abs_carpet, abs_curtains, abs_acousbrd ] )

           self.surfacenames = ["floor", "ceiling", "fwall", "bwall", "lwall", "rwall"]
           self.areas = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

      def update(self):
           """Updates the graph with new data/annotations"""
           self.canvas.ax.clear()

           # Get information from the various inputs
           main = self.parent().parent().parent().parent().parent()   #TODO: this will break if a single thing is changed
           ss_text = str(main.sabinesslineEdit.text())
           x_text = str(main.sabinexlineEdit.text())
           y_text = str(main.sabineylineEdit.text())
           z_text = str(main.sabinezlineEdit.text())
           adults_text = str(main.adultslineEdit.text())
           floor_mi = main.floorcomboBox.currentIndex()    # mi = "material index"
           ceiling_mi = main.ceilingcomboBox.currentIndex()
           fwall_mi = main.fwallcomboBox.currentIndex()
           bwall_mi = main.bwallcomboBox.currentIndex()
           lwall_mi = main.lwallcomboBox.currentIndex()
           rwall_mi = main.rwallcomboBox.currentIndex()

           
           
           # do nothing for bad input
           if (""==ss_text) | (""==x_text) | (""==y_text) | (""==z_text) | (""==adults_text): return
 
           # Parse the text info
           vs = float(ss_text)
           x = float(x_text)
           y = float(y_text)
           z = float(z_text)
           adults = float(adults_text)
           volume = x * y * z
           self.areas = [ x*y, x*y, x*z, x*z, y*z, y*z ] 
           surf_materials = [ floor_mi, ceiling_mi, fwall_mi, bwall_mi, lwall_mi, rwall_mi] 
  
           #print "vs, x, y, z = ", vs, x, y, z
           #print "areas = ",self.areas

           freqs = self.abs_freqs
           rtimes = 0.0*freqs
           # Calculate reverb times
           for f_ind in range(len(self.abs_freqs)):
               sabines = adults*self.sab_adult[f_ind]
               for surf in range(len(self.surfacenames)):
                   #TODO: concrete only for now
                   surf_coeffs = self.abs_coeffs[surf_materials[surf]]
                   sabines = sabines + self.areas[surf]* surf_coeffs[f_ind]

               rtimes[f_ind] = 0.050 * 1140.0/vs * volume / sabines 
  
           #print "freqs = ",self.abs_freqs
           #print "rtimes = ",rtimes

           # Set up the plot
           self.canvas.ax.plot(freqs, rtimes, 'bo-')
           self.canvas.ax.grid(True)
           self.canvas.ax.axis([0.0,freqs[-1]*1.05,0.0, np.max(rtimes)*1.05 ])
#           self.canvas.ax.set_xscale("log", nonposx='clip')

           # Annotation
           self.canvas.ax.set_xlabel('Frequency (Hz)')
           self.canvas.ax.set_ylabel('Reverberation Time (s) ')

           # Actually draw everything
           self.canvas.draw()

