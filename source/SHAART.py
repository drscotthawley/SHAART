#!/usr/bin/env python
# used to parse files more easily
from __future__ import with_statement
from __future__ import print_function

# Numpy module
import numpy as np

# for command-line arguments
import sys

# GUI bindings
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *

# import the MainWindow widget from the converted .ui files
from ui_shaart import Ui_TheMainWindow

import scipy.io.wavfile as wavfile
#from scikits.audiolab import Sndfile
import librosa
import scipy.signal as signal
import pylab as pl
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import re
from PIL import Image    #import Image   # cleaned this up
from scipy import zeros, ifft

import pyaudio
import time

#import cython #  not used at ALL. only in here b/c of bug with py2app packaging

#----------------- for filtering signals -----------------
# from post by Warren Weckesser, http://tinyurl.com/d4cjs7m
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    if (highcut > nyq):
       highcut = nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y
#---------------------------------------------------------

# Just for debugging:
def funcname():
    import traceback
    return traceback.extract_stack(None, 2)[0][2]


# Global variables (it's a GUI-based code, so...)
amp = [1.0]
orig_amp = amp
t= [1.0]
dB = [1.0]
sample_rate = 44100
nofile = 1
nofileB = 1
filenameA = ""
ampB = amp
orig_ampB = amp
tB = t
dB_B = dB
sample_rateB = sample_rate
filenameB = filenameA

class DesignerMainWindow(QMainWindow, Ui_TheMainWindow):
    """Customization for Qt Designer created window"""
    def __init__(self, parent = None):
        # initialization of the superclass
        super(DesignerMainWindow, self).__init__(parent)
        # setup the GUI --> function generated by pyuic4
        self.setupUi(self)
        # connect the signals with the slots
        #QtCore.QObject.connect(self.actionChangeFeedbackController, QtCore.SIGNAL("triggered()"), self.changeFeedbackController)
        #self.actionChangeFeedbackController.triggered.connect(self.changeFeedbackController)
        self.theactionOpen.triggered.connect(self.menuselect_read_fileA)
        self.theactionOpenB.triggered.connect(self.menuselect_read_fileB)
        #self.theactionQuit.triggered.connect(QtGui.qApp, QtCore.SLOT("quit()"))
        self.theactionQuit.triggered.connect(QMainWindow.close)

        self.theactionAbout.triggered.connect(self.about_message )
        self.theactionSave.triggered.connect(self.write_wav_file)

        #QtCore.QObject.connect(self.waveform_abs_checkBox, QtCore.SIGNAL('stateChanged(int)'), self.update_tab)
        self.waveform_abs_checkBox.stateChanged.connect(self.update_tab)
        self.waveform_env_checkBox.stateChanged.connect(self.update_tab)

        self.inwavfileselectButton.clicked.connect(self.menuselect_read_fileA )
 #       QtCore.QObject.connect(self.rt60lineEdit, QtCore.SIGNAL('editingFinished()'),   self.changedtext_read_fileA )
        self.inwavfileBselectButton.clicked.connect(self.menuselect_read_fileB )
 #       QtCore.QObject.connect(self.fileBlineEdit, QtCore.SIGNAL('editingFinished()'),  self.changedtext_read_fileB )

        self.spectrocmcomboBox.currentIndexChanged.connect(self.update_tab)


        self.rt60comboBox.currentIndexChanged.connect(self.filter_signal)
        self.tabWidget.currentChanged.connect(self.update_tab )
        self.speedlineEdit.editingFinished.connect(self.calc_modes )
        self.lengthlineEdit.editingFinished.connect(self.calc_modes )
        self.widthlineEdit.editingFinished.connect(self.calc_modes )
        self.heightlineEdit.editingFinished.connect(self.calc_modes )
        self.maxmodelineEdit.editingFinished.connect(self.calc_modes )

        self.is_img_pushButton.clicked.connect(self.select_read_img_file)
        self.is_wav_pushButton.clicked.connect(self.select_write_wav_file)
        self.is_go_pushButton.clicked.connect(self.img_to_wav)

        self.eq_go_pushButton.clicked.connect(self.equation_go)
        self.convolve_go_pushButton.clicked.connect(self.convo_go)

        self.pushButton_playrec_go.clicked.connect(self.playrec_go)


    # writes a PCM 16 bit WAV file
    def write_wav_file(self):
        global sample_rate, orig_amp
        filename = QtWidgets.QFileDialog.getSaveFileName(self,"Filename to Save to","",'WAV File Name (*.wav)')
        if filename != "":
            filename = filename[0]  # Qt5 dialog returns a tuple
            # write to file
            #--------------
            wavfile.write(filename, sample_rate, amp)
        return

    # generic reader routine for audio files.
    def read_audio_file(self, file_name):
        if file_name=='': return

        y, samplerate = librosa.load(file_name, sr=None, dtype=np.float32)
        nsamples = len(y)
        if (len(y.shape) > 1):    # take left channel of stereo track
            y = y[:,0]

        x = np.arange(nsamples)*1.0/samplerate   # time values
        return y, x, samplerate

    def changedtext_read_fileA(self):
        global amp, filenameA, t, sample_rate, orig_amp
        filenameA = self.rt60lineEdit.text()
        if filenameA=='': return
        amp, t, sample_rate = self.read_audio_file(filenameA)
        orig_amp = amp
        global nofile
        nofile = 0
        self.update_tab()

    def menuselect_read_fileA(self):
        """opens a file select dialog"""
        # open the dialog and get the selected file
        file = QtWidgets.QFileDialog.getOpenFileName()
        # if a file is selected
        if file:
            file = file[0]   # newer qt5 also returns list of file types, which we don't want
            # update the lineEdit text with the selected filename
            self.rt60lineEdit.setText(file)
            self.changedtext_read_fileA()
            filenameA = "%s" % file

    def changedtext_read_fileB(self):
        global ampB, filenameB, tB, sample_rateB, orig_ampB
        filenameB = self.fileBlineEdit.text()
        ampB, tB, sample_rateB = self.read_audio_file(filenameB)
        orig_ampB = ampB
        global nofileB
        nofileB = 0
        self.update_tab()

    def menuselect_read_fileB(self):
        """opens a file select dialog"""
        # open the dialog and get the selected file
        fileB = QtWidgets.QFileDialog.getOpenFileName()
        # if a file is selected
        if fileB:
            fileB = fileB[0]   # newer qt5 also returns list of file types, which we don't want
            # update the lineEdit text with the selected filename
            self.fileBlineEdit.setText(fileB)
            self.changedtext_read_fileB()
            filenameB = "%s" % fileB


    def select_read_img_file(self):
        # open the dialog and get the selected file
        file = QtWidgets.QFileDialog.getOpenFileName()
        if file:
            # update the lineEdit text with the selected filename
            self.is_imname_lineEdit.setText(file)

    def select_write_wav_file(self):
        # open the dialog and get the selected file
        file = QtWidgets.QFileDialog.getSaveFileName()
        if file:
            # update the lineEdit text with the selected filename
            self.is_wavname_lineEdit.setText(file)

    #-----------------------------------------------------
    # In response to "Octave" comboBox trigger
    # Filters signal for use with rt60 measurements
    #-----------------------------------------------------
    def filter_signal(self):
        global amp, orig_amp, filenameA
        global ampB, orig_ampB, filenameB
        octave_text = str(self.rt60comboBox.currentText())
        if (octave_text != 'All'):
           octave_center_freq = (float)(re.sub(r' Hz','',octave_text))
           lowcut  = 1.0*(int)(0.71 * octave_center_freq)
           highcut = 1.0*(int)(1.42 * octave_center_freq)
           amp = butter_bandpass_filter(orig_amp, lowcut, highcut, 1.0*sample_rate, order=3)
           if (len(orig_ampB) > 1):
              ampB = butter_bandpass_filter(orig_ampB, lowcut, highcut, 1.0*sample_rate, order=3)
        else:
           amp = orig_amp
           if (len(orig_ampB) > 1):
              ampB = orig_ampB
        self.rt60.linex = [0]   # erase the old line
        self.rt60.liney = [0]   # erase the old line
        self.rt60.update_graph(amp,t,filenameA,ampB,tB,filenameB)
        return



    def calc_modes(self):
        vs_text = str(self.speedlineEdit.text())
        x_text = str(self.lengthlineEdit.text())
        y_text = str(self.widthlineEdit.text())
        z_text = str(self.heightlineEdit.text())
        mm_text = str(self.maxmodelineEdit.text())
        if (vs_text=="") | (x_text=="") | (y_text=="") or (z_text==""): return
        vs = float(vs_text)
        x = float(x_text)
        y = float(y_text)
        z = float(z_text)
        maxmodenum = int(mm_text)
        modes = []
        #maxmodenum = 15
        outstring = "Freq (Hz)  Nx Ny Nz\n---------  -- -- -- \n"
        # The following convoluted loops & if statement are simply to enforce a
        # particular ordering I am fond of for displaying mode numbers
        for modesum in np.arange(1,maxmodenum+1):
           for mm in np.arange(1,modesum+1):
              for i in np.arange(mm,-1,-1):
                 for j in np.arange(mm,-1,-1):
                    for k in np.arange(0,mm+1):
                       if (i+j+k == modesum) & (i<= mm) & (j<=mm) & (k<=mm) & \
                               ((i==mm)| (j==mm) | (k==mm)):
                          f = vs/2.0*np.sqrt( (1.0*i/x)**2 + (1.0*j/y)**2 + (1.0*k/z)**2)
                          mode = [f, i, j, k]
                          modes.append(mode)
        # or we can destroy that ordering by sorting by frequency
        modes.sort()
        for m in modes:
            thisline = '%9.1f  %2d %2d %2d\n' %  (m[0], m[1], m[2], m[3])
            outstring = outstring + thisline
        self.modesTextEdit.setPlainText(outstring)
        self.modegraph.update_graph(modes,x,y,z)

    def tojas_isft(self, X, fs, T, hop):
       x = scipy.zeros(T*fs)
       framesamp = X.shape[1]
       hopsamp = int(hop*fs)
       for n,i in enumerate(range(0, len(x)-framesamp, hopsamp)):
           x[i:i+framesamp] += scipy.real(scipy.ifft(X[n]))
       return x


    def my_istft(self, X, fs, T):
        # Inverse Short-Time Fourier Transform, i.e. "Inverse Spectrogram"
        # Props to Steve Tjoa, cf.  http://stackoverflow.com/questions/2459295/stft-and-istft-in-python
        # Added the overlapping frames / buffers to improve image quality - Scott Hawley
        # inputs:
        #   X = image/ stft
        #   fs = sample rate, in samples/sec
        #   T = duration, in secs
        #
        #  Output array will have this structure:
        #                                 pixel                                      pixel
        #  ||----------|--------------------o------------------|-----------------------o-----------------|-----etc
        #               <------------------hop----------------><----------------------hop---------------->
        #                                    <--------------------hop------------------>
        #    <---buf--->                                        <---buf--->
        #    <---------------------------- frame-------------------------->
        #                                             <--buf--->                                          <--buf--->
        #                                             <---------------------------- frame-------------------------->
        #...and then the starting and ending buffers will be removed

        nhops = X.shape[1]              # each pixel is a "hop"
        hop_duration = T / nhops        # in secs
        samples_per_hop = int(hop_duration * fs)

        ibuf = 128 * fs / 44100     # buffer size,  calibrated for 44.1 kHz
        tbuf = 1.0 * ibuf / fs      # may seem redundant, but readable
        x = zeros((T+2*tbuf)*fs)

        # around each hop, we put a frame, centered on the hop, but wider by buf on each side
        samples_per_frame = samples_per_hop + 2*ibuf
        n = samples_per_frame

        for ihop in range(nhops):
            b = np.array(ifft(X[ihop], n = n))    # b is a 'vertical' set of pixels
            framedata = np.imag(b)     # I actually find that imag() gives better image results than real()
            ibgn = ibuf +  samples_per_hop/2 +  ihop*samples_per_hop - samples_per_frame/2
            iend = ibgn + n-1
            x[ibgn:iend] += framedata[0:n-1]

        y = x[ibuf:-ibuf]  # chop off the buffers
        return y

    def ekman_istft(self, X, fs, T, minfreq, maxfreq):
        # This is based on Coagula by Rasmus Ekman: https://www.abc.se/~re/Coagula/Coagula.html
        # In this method, we don't actually take an inverse STFT.
        # Ekman: "How: Coagula uses one sinewave (beep) per image line, one short blip per point (pixel) on the line. "
        #   X is the image, i.e. the STFT of the time series data to be produced (called 'x', below)
        #   fs = sample rate, in samples/sec
        #   T = duration, in secs
        #   minfreq, maxfreq = min & max frequency (in Hz) in which to map image ("vertically")

        nhops = X.shape[0]              # each pixel is a "hop"
        hop_duration = T / nhops        # in secs
        samples_per_hop = int(hop_duration * fs)
        nfreq = X.shape[1]
        dfreq = (maxfreq - minfreq) / nfreq

        print('ekman: nhops, nfreq, dfreq = ',nhops, nfreq, dfreq)

        ibuf = 0  # no buffer
        tbuf = 1.0 * ibuf / fs      # may seem redundant, but readable
        x = zeros((T+2*tbuf)*fs)    # x is the time series data
        for ihop in range(nhops):
            for ifreq in range(nfreq):   #scan vertically upwards
                freq = minfreq + ifreq * dfreq
                intensity = X[ihop,ifreq]
                phase = 0.0
                framedata = intensity * np.sin( 2*3.14159*freq * np.arange(0,hop_duration,hop_duration/samples_per_hop) + phase )

                ibgn = ibuf +  ihop*samples_per_hop
                iend = ibgn + samples_per_hop
                x[ibgn:iend] += framedata[0:iend-ibgn]


        y = x
        return y


    def img_to_wav(self):
        im_filename  = str( self.is_imname_lineEdit.text() )
        wav_filename = str( self.is_wavname_lineEdit.text() )
        dur_str = str( self.is_duration_lineEdit.text() )
        rate_str = str( self.is_rate_lineEdit.text() )
        minf_str = str( self.is_minf_lineEdit.text() )
        maxf_str = str( self.is_maxf_lineEdit.text() )

        if (im_filename=="") | (wav_filename=="") | (dur_str=="") | (rate_str=="") |(minf_str=="") | (maxf_str=="") : return

        rate = int( rate_str )
        image_duration = float( dur_str )
        minfreq = float(minf_str)
        maxfreq = float(maxf_str)

        pic = Image.open(im_filename).convert("LA")
       # pic = pic.resize((512, 512), Image.ANTIALIAS)  # my_istft works 'best' with 512x512...
        image = np.array(pic.getdata())
        image = np.array(image[:,0]).reshape(pic.size[1], pic.size[0])


        # Construct the signal. Put the image into X, transpose & flip, take its inverse stft
        #---------------------
        X = 1.0*np.array(image)       # floating point values
        contrast_power = 1.5          # higher = more contrast, but also introduces more distortion
        X = (X)**contrast_power
        X = X.T  # transpose
        X = np.fliplr(X) # flip

        mysignal = self.ekman_istft(X, rate, image_duration,minfreq,maxfreq)    # conversion routine


        # normalize &  convert the signal to int
        #-------------------------------------------
        maxval = np.max(mysignal)
        mysignal = np.array([1.0*x / maxval for x in mysignal])

        iscale = 32767           # This sets the overall volume, 32727 = full scale

        # In the following line, the dtype='i2' selects 16-bit; without it you get 64 bits & no audio
        data = np.array([int(iscale * x) for x in mysignal], dtype='i2')

        # write to file
        #--------------
        wavfile.write(wav_filename, rate, data)

        self.is_status_label.setText("Finished!  Try opening the WAV file in the Spectrogram!")

        return



    #---------------------------------------------------
    # Code for generating sound based on equation
    #---------------------------------------------------
    def equation_go(self):
        global amp, orig_amp, nofile, filenameA, t, sample_rate
        dur_str = str( self.eqnduration_lineEdit.text() )
        rate_str = str( self.eqnsr_lineEdit.text() )
        eq_str = str( self.equation_lineEdit.text() )

        # basic definitions
        TMAX = float( dur_str )
        SR = int( rate_str )
        SRm1 = 1.0/SR
        sample_rate = SR
        NS = int( TMAX * sample_rate )
        print('TMAX, SR, NS, SRm1 = ',TMAX, SR, NS, SRm1)

        #allocate storage
        amp = np.zeros(NS,dtype=np.float64)

        #'parse' the equation string
        eq_str = re.sub('sin','np.sin',eq_str)
        eq_str = re.sub('cos','np.cos',eq_str)
        eq_str = re.sub('tan','np.tan',eq_str)
        eq_str = re.sub('arcnp.','np.arc',eq_str)
        eq_str = re.sub('sqrt','np.sqrt',eq_str)
        eq_str = re.sub('ln','np.log',eq_str)
        eq_str = re.sub('log10','np.log10',eq_str)
        eq_str = re.sub('abs','np.abs',eq_str)
        eq_str = re.sub('exp','np.exp',eq_str)
        eq_str = re.sub('PI','3.14159265358979323846',eq_str)
        eq_str = re.sub('np.np.','np.',eq_str)

        # now create the sounds
        t = np.arange(0,TMAX, SRm1)
        newstr = "amp[0:t.shape[0]] = " + eq_str
        print('Executing newstr = [', newstr, ']')
        exec(newstr)

        print('Finished loop')

        # Global settings for commucating with the rest of the program
        orig_amp = amp
        t = np.arange(0.0,TMAX,SRm1)
        nofile = 0
        filenameA = eq_str
        return

    # My own little autocorrelation routine
    def my_autocorr(self,x):
        meanx = np.mean(x)
        x -= meanx
        result = np.correlate(x, x, mode='full')
        maxval = np.max(result);
        result = result / maxval;
        return result

    #---------------------------------------------------
    #  Convolution
    #---------------------------------------------------
    def convo_go(self):
        global orig_amp, sample_rate, amp, t, filenameA
        global orig_ampB, sample_rateB, ampB, tB, filenameB
        global nofile, nofileB

        if ((1==nofileB) and (False == self.checkBox_autocorr.checkState())):
           print("convo_go: Unable to perform convolution")
           return

        if self.checkBox_timerev.checkState():
           amp3 = amp[::-1]
           amp = amp3

        if self.checkBox_autocorr.checkState(): # autocorrelation
            print("Debug: autocorrelation is checked")
            amp3 = self.my_autocorr(amp)
        elif (0 == nofileB):   # normal convolution

           amp3 = signal.fftconvolve( amp, ampB, mode="same")

           maxval_3 = np.max(amp3)
           amp3 *= 0.9999999 / maxval_3

        if self.checkBox_removefirsthalf.checkState():
           amp = amp3[amp3.size/2:]    # cut off first half of array
        else:
           amp = amp3

        orig_amp = amp
        t = np.arange(0.0,amp.size,1.0)/sample_rate;
        amp3 = 0

        nofileB = 1     # wipe out fileB
        ampB = [1.0]
        tB = [1.0]
        filenameB = ""
        return


    #---------------------------------------------------------------------
    # Tab for playing & recording audio
    #---------------------------------------------------------------------
    def playrec_go(self):
        global amp, sample_rate
        global current_index, maxi
        current_index = 0
        maxi = len(amp)-1


        # pull a frame_count samples from array "amp"
        def get_chunk(frame_count):
           global current_index

           if ( current_index < maxi):
               iend = np.min(  [current_index + frame_count-1, maxi ])
               chunk = amp[current_index: maxi]
               out_data = chunk.astype(np.float32).tostring()
               current_index += frame_count
           else:
               out_data = []
           return out_data


        # define callback
        def callback(in_data, frame_count, time_info, status):
           out_data = get_chunk(frame_count)
           return ( out_data , pyaudio.paContinue)



        if nofile: return

        # instantiate PyAudio
        p = pyaudio.PyAudio()

        # open stream using callback
        stream = p.open(
                   format=pyaudio.paFloat32,
                   channels=1,
                   rate=sample_rate,
                   output=True,
                   stream_callback=callback)

        #start the stream
        stream.start_stream()

        # wait for the stream to finish
        while stream.is_active() and (current_index < len(amp)-1) :
           time.sleep(0.1)

        #stop stream
        stream.stop_stream()
        stream.close()

        #close PyAudio
        p.terminate()

        return



    #----------------------------------------------------------------
    # Generic routine for updating whichever tab is currently showing
    #----------------------------------------------------------------
    def update_tab(self):
        global orig_amp, sample_rate, amp, t, filenameA
        global orig_ampB, sample_rateB, ampB, tB, filenameB
        tabnum = self.tabWidget.currentIndex()
        if (0 == tabnum):   # rt60
            if nofile: return
            self.rt60.update_graph(amp,t,filenameA,ampB,tB,filenameB)
        elif (1 == tabnum):   # waveform
            self.waveform.update_graph(amp,t,filenameA,ampB,tB,filenameB,
                   self.waveform_abs_checkBox.checkState(),self.waveform_env_checkBox.checkState())
            if nofile: return
        elif (2 == tabnum):   # power spectrum
            if nofile: return
            self.pwrspec.update_graph(amp,sample_rate,filenameA,ampB,sample_rateB,filenameB)
        elif (3 == tabnum):  # spectrogram
            if nofile: return
            self.spectro.update_graph(amp,sample_rate,self.spectrocmcomboBox.currentIndex())
        elif (4 == tabnum):   # wateverfall
            if nofile: return
            self.water.update_graph(amp,sample_rate)
        elif (5 == tabnum):  # invSpectro
            self.img_to_wav()
            return
        elif (6 == tabnum):  # Room Modes
            self.calc_modes()
        elif (7 == tabnum):  # Sabine Eq
            return
        elif (8 == tabnum):   #equation
            #  self.equation_go()  only run equation_go when the go button is pushed
            return
        elif (9 == tabnum):   # convolve
            if nofile: return
            # self.convo_make(); only run convo_go when the go button is pushed
        elif (10 == tabnum):  # play/rec
            if nofile: return
        else:
            print("ERROR: tabnum =",tabnum,"is unsupported.")


    def about_message(self):
        msg = """
SHAART v.0.7
http://hedges.belmont.edu/~shawley/SHAART

A simple audio analysis suite intended for
educational purposes, student projects, etc.

Scott H. Hawley, Ph.D.
Belmont University
scott.hawley@belmont.edu
        """
        QtWidgets.QMessageBox.about(self, "About SHAART", msg.strip())

        return

# create the GUI application
app = QtWidgets.QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
