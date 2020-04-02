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
<a href="#downloads">Downloads</a> &nbsp;&nbsp;
<a href="#license">License</a> &nbsp;&nbsp;
<a href="#screenshots">Screenshots</a> &nbsp;&nbsp;
<a href="#source">Running From Source</a> <br>
<a href="#tutorial">Tutorial(s)</a> &nbsp;&nbsp;
<a href="#faq">FAQ</a> &nbsp;&nbsp;
<a href="#notes">Release Notes</a> &nbsp;&nbsp;
<br><br>
</p>

<a name="about"></a>

## About

This lightweight audio analysis suite was initially written <b><i>for educational purposes only</i></b>
over a period of 4 days.  (And then improved in bits.)<br>
It's amazing how much you can accomplish with minimal knowledge of Python programming.<br>
<br>
The name "SHAART" uses the author's initials (S.H.) in homage to the famous "SMAART" set of acoustics analysis tools.<br>
That and "SHAART" is just hilarious to say, for other reasons. <br>
<i>(Note: "homage" = parody, derivative work = fair use = please don't sue.)</i><br>

<a name="downloads"></a>

## Downloads

* [Mac Binary Application](https://hedges.belmont.edu/~shawley/SHAART/SHAART.app.tar.gz) (105 MB)

*  [Windows Executable](https://drive.google.com/file/d/1F2ljmx9K1xb1S2RXX4YLEqViVLCqWzV2/view?usp=sharing) (380 MB)
* [Source code](https://hedges.belmont.edu/~shawley/SHAART/SHAART.tar.gz) (in Python)  See "Running from Source" below for further instructions.
* [Sample WAV file](https://hedges.belmont.edu/~shawley/SHAART/sample_data.wav)



<a name="license"></a>

## License

2013 - 2019: This software is both "Open Source" and "Free," released under the Jesus license: "Freely you have received, freely give" (Matthew 10:8). Do as you like.  Modify, redistribute, etc.  

2020+: Consider this a Creative Commons License.



<a name="tutorial"></a>

## Tutorial(s)

* **How to use the App:**  Go up to the "File" tab and select a WAV file to analyze.

  Note: You don't need a WAV file to use the room mode calculator.  

* [Creating Impulse Responses with SHAART](ir.html)

* ...TODO: add more later, e.g. measuring reverb times.



<a name="screenshots"></a>

## Screenshots

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
Create a new [Anaconda] Python environment and install dependencies...

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
Each of these methods will create a new directory called `SHAART/source/dist/`, in which a successful build will result in the presence of working binary executable.

A few notes on PyInstaller:

   1. The `conda` version of `pyinstaller` is old (v3.5); to get the new one (v3.6) we need to use `pip` instead: `$ pip install pyinstaller`
      2. It produces a seemingly huge (380 MB) executable, whereas py2app is more compact.
      3. The pyinstaller-generated executable takes a long time to load up when you try to run it.

### Linux (Ubuntu / Pop!\_OS)
```bash
pyinstaller -w --onefile --hidden-import="librosa" SHAART.py
```

### Windows (10)
Install the Windows SDK, and also install `pywin32` and `pypiwin32`, and we need to list a bunch of other stuff when we run pyinstaller:

**TODO:** add more Windows instructions.

### Mac
You need to have XCode and the command-line tools installed, and HomeBrew as well.

```bash
python setup.py py2app
```

<hr>
Author: <a href="http://www.scotthawley.com">Scott Hawley</a>
</body>
</html>


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
