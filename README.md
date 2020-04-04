<head>
<link rel="SHORTCUT ICON" href="shaart_logo.jpg" />
<link rel="image_src" href="http://hedges.belmont.edu/~shawley/SHAART/shaart_logo.jpg" />
<meta property="og:image" content="http://hedges.belmont.edu/~shawley/SHAART/shaart_logo.jpg" />
<meta property="og:url" content="http://hedges.belmont.edu/~shawley/SHAART" />
<meta property="og:title" content="SHAART Acoustic Tools" />
<meta property="og:image" content="http://hedges.belmont.edu/~shawley/SHAART/screenshots/rt60.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="http://hedges.belmont.edu/~shawley/SHAART/screenshots/rt60.jpg">
<meta keywords="audio acoustics analysis python education">
</head>
<body>

# SHAART Acoustic Tools

Main web page: http://hedges.belmont.edu/~shawley/SHAART/index.html

<p align="center">
SHAART Acoustic Tools, v 0.7<br>
(April 5, 2020)<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/shaart_logo.jpg"><br>
(yes, the name is a joke)<br>
<a href="#about">About</a> &nbsp;&nbsp;
<a href="#features">Features</a> &nbsp;&nbsp;
<a href="#downloads">Downloads</a> &nbsp;&nbsp;
<a href="#license">License</a> &nbsp;&nbsp;
<a href="#tutorial">Tutorial(s)</a> &nbsp;&nbsp;
<a href="#screenshots">Screenshots</a> &nbsp;&nbsp;
<a href="#source">Running From Source</a>  &nbsp;&nbsp;
<a href="#build">Building an Executable</a>  &nbsp;&nbsp;
<a href="#faq">FAQ</a> &nbsp;&nbsp;
<a href="#notes">Release Notes</a> &nbsp;&nbsp;
<br><br>
</p>


<a name="about"></a>

## About

This lightweight audio analysis suite was initially written <b><i>for educational purposes only</i></b>
over a period of 4 days.  (And then improved in bits.)  It's amazing how much you can accomplish with minimal knowledge of Python programming!

The name "SHAART" uses the author's initials (S.H.) in homage to the famous "SMAART" set of acoustics analysis tools.  That and "SHAART" is just hilarious to say, for other reasons.  *(Note: "homage" = parody, derivative work = fair use = please don't sue.)*



<a name="features"></a>

## Features

Most of these features are illustrated in the <a href="#screenshots">Screenshots</a> section further down this page.

* **RT60 Measurement:** The reason SHAART was written in the first place.  Load an audio file, filter in different octave bands, draw a "best fit" line on the graph by hand, read off the reverb time.  (Designed to mimic functionality of SMAART Acoustics Tools(tm).)  Can show two files ("File A" and "File B") at once.  See "Tutorial(s)" below for a demo.
* **Waveform Display:** Linear scale only.  Displays two waveforms ("File A" and "File B") at once.
* **Power Spectrum:** Pretty standard display Doesn't do a log scale yet, though I'd like to add that.  Displays two spectra ("File A" and "File B" at once.)
* **Spectrogram:**  Shows magnitude as color, vs frequency and time. as with Power Spectrum.  Offers a few colormaps.  No log freq scale yet.  Only one file ("File A") shown.
* **Waterfall Plot:**  Alternative to Spectrogram, shows magnitude surface a function of time & frequency.   No log freq scale yet.  Only one file ("File A") shown.
* **"Inverse Spectrogram" (Image-To-Audio):**  Import an image, output audio for which the spectrogram will resemble that image.  Sounds a little "phasey," could be cleaner.  Useful for demonstrating audio effects.  See "Screenshots," below.
* **Room Mode Calculator:**  Uses the Rayleigh equation for standing waves of a 3D box, and also plots a "Fake Room Response" by assigning relative amplitudes to axial, tangential, and oblique modes.  Useful for demonstrating mode distributions for different room shapes.
* **Sabine Equation Calculator:** Assumes a box-shaped room, lets you apply absorption to different surfaces.  Based on Chapter 8 of Berg & Stork textbook, including their table for absorption coefficients.
* **Equation-to-Audio:** Specify a time-dependent function, and it'll generate audio from that. Useful for sine sweeps, e.g. for building impulse responses using Convolution (below)
* **Convolution:** Convolve File A with File B.  Useful for making impulse responses from sine sweeps, or just for screwing around (e.g. convolving Led Zeppelin's "The Ocean" with the sound of a dog bark.)
* **Play(/Record):** Very rudimentary.  Will play the audio out the speaker, with no controls.  Record doesn't work yet.


<a name="downloads"></a>

## Downloads

* [Mac Binary application](https://hedges.belmont.edu/~shawley/SHAART/SHAART.app.tar.gz) (105 MB)

*  [Windows executable](https://drive.google.com/file/d/1F2ljmx9K1xb1S2RXX4YLEqViVLCqWzV2/view?usp=sharing) (380 MB). Note that the Windows EXE takes *a while* to come up when you first run it.
* [Linux executable](https://drive.google.com/file/d/1uE_1x8ZCXI1bpQY5EamCEqUT2PUCLzYg/view?usp=sharing) (132 MB, Pop!\_OS / Ubuntu).  You can also <a href="#source">run from source</a> (below)
* [Source code](https://hedges.belmont.edu/~shawley/SHAART/SHAART.tar.gz) (in Python)  See <a href="#source">Running From Source</a> below for further instructions.
* [Sample WAV file](https://hedges.belmont.edu/~shawley/SHAART/sample_data.wav)



<a name="license"></a>

## License

2013 - 2019: This software is both "Open Source" and "Free," released under the Jesus license: "Freely you have received, freely give" (Matthew 10:8). Do as you like.  Modify, redistribute, etc.  

2020+: Consider this a Creative Commons License.



<a name="tutorial"></a>

## Tutorial(s)

* **How to use the App:**  Go up to the "File" tab and select a WAV file to analyze.

  Note: You don't need a WAV file to use the room mode calculator.

*  **TODO:** Measuring Reverb times with SHAART

* [Creating Impulse Responses with SHAART](ir.html)



<a name="screenshots"></a>

## Screenshots

**TODO:** update screenshots with new QT5 version & show all tabs

<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/rt60.jpg" width=600><br>
<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/power.jpg" width=600><br>
<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/spectro.jpg" width=600><br>
<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/waterfall.jpg" width=600><br>
<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/modes.jpg" width=600><br>
<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/sabine.jpg" width=600><br>
<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/invspectro.jpg" width=600><br>
<br>
invSpectro (above) created the file [mandrill.wav](https://hedges.belmont.edu/~shawley/SHAART/mandrill.wav) which has a spectrogram shown below:

<img src="https://hedges.belmont.edu/~shawley/SHAART/screenshots/mandrill_spectro.png" width=600><br>
<br>
And interestingly, if the audio is encoded as an MP3, then re-read and re-written as a WAV, one can see the "lossyness" of the MP3:<br>
<img src="https://hedges.belmont.edu/~shawley/SHAART/screenshots/mandrill_mp3_to_wav.png" width=600><br>
<br>
One can also apply various audio plugins to the sound and see the effect on the image, e.g. echo:<br>
<img src="https://hedges.belmont.edu/~shawley/SHAART/screenshots/mandrill_echo.png" width=600><br>
Wah-wah:<br>
<img src="https://hedges.belmont.edu/~shawley/SHAART/screenshots/mandrill_wahwah.png" width=600><br>
Reverb:<br>
<img src="https://hedges.belmont.edu/~shawley/SHAART/screenshots/mandrill_reverb.png" width=600><br>
And here's an interesting one: a "leveler" effect:<br>
<img src="https://hedges.belmont.edu/~shawley/SHAART/screenshots/mandrill_leveler.png" width=600><br>
<br>

<a name="source"></a>

## Running from Source
<b>Running SHAART.py from source:</b><br>
Create a new [Anaconda](https://www.anaconda.com/) Python environment and install dependencies...

```bash
cd SHAART/source
conda create --name shaart python=3.7
conda activate shaart
conda install -c numba numba      # numba is optional, actually
conda install -c conda-forge librosa
conda install pyqt pillow pyaudio
python SHAART.py
```



## Building an Executable

First follow the instructions above for running from source.  Then install an app-building app.  
For Mac, we use `py2app`, whereas for Linux and Windows we'll use `pyinstaller`.  
Each of these methods will create a new directory called `SHAART/source/dist/`, **in which a successful build will result in the presence of working binary executable.**


### Mac
In order to run from source, you'd already need to have XCode, the command-line tools, and HomeBrew installed. Then in we add py2app

```bash
conda install py2app
python setup.py py2app
```

### Windows & Linux

Install PyInstaller:

```bash
conda install -c conda-forge pyinstaller
```

One note on PyInstaller: The pyinstaller-generated executable takes a long time to load up when you try to run it.

#### Windows (10)
Here are the steps taken to build the Window EXE:

1. Download & Install Windows SDK: https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/

2. Download & Install Anaconda (64 bit):  https://www.anaconda.com/

3. Run Anaconda Powershell prompt and install requirements:

   ```bash
   conda install -c conda-forge ffmpeg
   conda install -c anaconda pyqt pywin32 pypiwin32
   conda install pyaudio librosa pywintypes
   ```

5. Downgrade `setuptools` to avoid conflicts `pyinstaller` as per https://github.com/pypa/setuptools/issues/1963:
   `pip install --upgrade 'setuptools<45.0.0'`

6. Run `pyinstaller` with these arguments:

   ```bash
   pyinstaller -w --icon=shaart_logo_icon.ico  --hidden-import="pypiwin32" --hidden-import="pywintypes" --hidden-import="sklearn.utils._cython_blas" --hidden-import="sklearn.neighbors._typedefs" --hidden-import="sklearn.neighbors.quad_tree" --hidden-import="sklearn.tree._utils" --onefile SHAART.py
   ```

#### Linux (Ubuntu / Pop!\_OS)

For Linux, all dependencies are the in "spec" file, so after installing `pyinstaller`, you can just run...

```bash
pyinstaller SHAART.spec --specpath=test
```
...builds it.  And then you can just run the `dist/SHAART` executable from the command line.   Note: I can't seem to get it to be a "clickable icon" in Nautilus/Gnome.  Not sure how to do that.

<hr>
Author: <a href="http://www.scotthawley.co



m">Scott Hawley</a>
</body>
</html>



## Changing the GUI

Run QT5's `designer` (or `Designer`) app using `ui_shaart.ui` as an input.  Change the GUI as you like, save it, and then to generate the .py file, run

```bash
pyuic5 -x ui_shaart.ui -o ui_shaart.py
```



<a name="faq"></a>

## FAQ

* Can it only read WAV files?  No.  Despite saying WAV file everywhere, the newest version of SHAART will read AIFF files too.  And the previous issues with 24-bit PCM WAV files has been resolved.
* Do I always need an audio file?  No. You don't need a WAV file to use the room mode calculator or the Sabine calculator.
* Can I get a logarithmic frequency scale for the spectrogram?  Not yet.
* For waterfall plots, it doesn't clear the window if you change the input data, resulting in multiple plots on the same page.  Bug or feature?
* Does the "Record" feature work?  Not yet.
* How do I contribute to SHAART?  Submit a Pull Request!

<a name="notes"></a>

## Release Notes / Issues
* v0.7:

   * Updated code from Python 2.7 to Python 3.7
   * Updated GUI from Qt4 to Qt5
   * Added capability for Windows & Linux executable builds

* v0.6: Minor improvements to speed and reliability

* v0.5:  

   * Got its own App icon!

   * "Power": Improved power spectrum calculation and display.
   * "Equation": Added equation for inverse exp. sine sweep (with "depinking").
   * Added IR creation tutorial (documentation)



## More docs & info

Purpose:
SHAART is intended as an in-house solution for teaching PHY2010 ("Physics for
Audio Engineering Technology") at Belmont University.  Perhaps others will find
it useful as well.  ...That and the PHY4410 ("Survey of Advanced Physics")
students and I have been learing Python this semester to implement our
simulations and analysis, so writing this also serves as an instructive
exercise in Python programming.

License:
The source code any binaries are free.  Free as in beer, and free as in "do
whatever you want with them."  SHAART was made using code provided by others for
free.   "Freely you have received, freely give."

Nomenclature:
The name is an acronym using the author's initials (S.H.), along with words
like "Acoustic," "Analysis," "Reverberation Time" or "Research Tools" -- as well
as, it is hoped, a lighthearted and not-legally-problematic play on words with
the name of the industry-standard SMAART audio analysis software made by
Rational Acoustics,Inc.  (SHAART is in no way affiliated with SMAART or
Rational Acoustics, fyi.)  I mean, "SHAART" is just hilarious to say.

Author: Dr. Scott H. Hawley, Associate Professor of Physics,
        Belmont University, Nashville TN USA.  
Date:   April 2, 2020 (original March 24, 2013)

Contact:  Improvements, bug reports, inquiries, donations, etc.: scott.hawley@(belmont)



List of files:
    SHAART.py         - the main control window, and most of the mode calc's
    rt60widget.py     - most of the rt60 tab functionality
    pwrspecwidget.py  - power spectrum
    spectrowidget.py  - spectrogram
    rcgraphwidget.py  - reverb characteristic graph for the Sabine calc
    waterwidget.py    - waterfall plot
    ui_shaart.ui      - QT Designer file for the user interface
    ui_shaart.py      - auto-generated by pyuic
    setup.py          - used for py2app.  See above.
    shaart_logo.png   - one of the most horrifying graphic designs ever
