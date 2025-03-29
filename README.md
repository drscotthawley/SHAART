<head>
<link rel="SHORTCUT ICON" href="shaart_logo.jpg" />
<link rel="image_src" href="http://hedges.belmont.edu/~shawley/SHAART/images/shaart_logo.jpg" />
<meta property="og:image" content="http://hedges.belmont.edu/~shawley/SHAART/images/shaart_logo.jpg" />
<meta property="og:url" content="http://hedges.belmont.edu/~shawley/SHAART" />
<meta property="og:title" content="SHAART Acoustic Tools" />
<meta property="og:image" content="http://hedges.belmont.edu/~shawley/SHAART/images/rt60.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="http://hedges.belmont.edu/~shawley/SHAART/images/rt60.png">
<meta keywords="audio acoustics analysis python education">
</head>

<body>

# SHAART Acoustic Tools


<p align="center">
SHAART Acoustic Tools, v 0.81<br>
(March 28, 2025)<br>
<img src="images/shaart_logo.jpg"><br>
(yes, the name is a joke)<br>
<a href="#about">About</a> &nbsp;&nbsp;
<a href="#features">Features</a> &nbsp;&nbsp;
<a href="#downloads">Downloads</a> &nbsp;&nbsp;
<a href="#license">License</a> &nbsp;&nbsp;
<a href="#tutorial">Tutorials</a> &nbsp;&nbsp;
<a href="#screenshots">Screenshots</a> &nbsp;&nbsp;<br>
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

The name "SHAART" uses the author's initials (S.H.) in homage to the famous "SMAART" set of acoustics analysis tools by Rational Acoustics, Inc.  ...That and "SHAART" is just hilarious to say, for other reasons.  *(Note: "homage" = parody, derivative work = fair use = please don't sue.)*



<a name="features"></a>

## Features

Most of these features are illustrated in the <a href="#screenshots">Screenshots</a> section further down this page.

* **Reverberation Time (RT60) Measurement:** The reason SHAART was written in the first place.  Load an audio file, filter in different octave bands, draw a "best fit" line on the graph by hand, read off the reverb time.  (Designed to mimic functionality of SMAART Acoustics Tools(tm).)  Can show two files ("File A" and "File B") at once.  See <a href="#tutorial">Tutorials</a> for more on this feature.
* **Waveform Display:** Linear scale only.  Displays two waveforms ("File A" and "File B") at once.
* **Power Spectrum:** Pretty standard display Doesn't do a log scale yet, though I'd like to add that.  Displays two spectra ("File A" and "File B" at once.)
* **Spectrogram:**  Shows magnitude as color, vs frequency and time. as with Power Spectrum.  Offers a few colormaps.  No log freq scale yet.  Only one file ("File A") shown.
* **Waterfall Plot:**  Alternative to Spectrogram, shows magnitude surface a function of time & frequency.   No log freq scale yet.  Only one file ("File A") shown.
* **"Inverse Spectrogram" (Image-To-Audio):**  Import an image, output audio for which the spectrogram will resemble that image.  Sounds a little "phasey," could be cleaner.  Useful for demonstrating audio effects.  See "Screenshots," below.
* **Room Mode Calculator:**  Uses the Rayleigh equation for standing waves of a 3D box, and also plots a "Fake Room Response" by assigning relative amplitudes to axial, tangential, and oblique modes.  Useful for demonstrating mode distributions for different room shapes.
* **Sabine Equation Calculator:** Assumes a box-shaped room, lets you apply absorption to different surfaces.  Based on Chapter 8 of Berg & Stork textbook, including their table for absorption coefficients.
* **Equation-to-Audio:** Specify a time-dependent function, and it'll generate audio from that. Useful for sine sweeps, e.g. for building impulse responses using Convolution (below)
* **Convolution:** Convolve File A with File B.  Useful for making impulse responses from sine sweeps, or creating convolution reverb effects, or just for screwing around (e.g., convolving Led Zeppelin's "The Ocean" with the sound of a dog bark.)
* **Play(/Record):** Very rudimentary.  Will play the audio out the speaker, with no controls.  Record doesn't work yet.

<a name="downloads"></a>

## Downloads

* [Mac Binary application](https://hedges.belmont.edu/~shawley/SHAART/SHAART.app.tar.gz) (93 MB)

*  [Windows executable](https://hedges.belmont.edu/~shawley/SHAART/SHAART.exe) (361 MB). Note that the Windows EXE takes *a while* to come up when you first run it.
* [Linux executable](https://hedges.belmont.edu/~shawley/SHAART/SHAART_Linux) (132 MB, Pop!\_OS / Ubuntu).  You can also <a href="#source">run from source</a> (below)
* [Source code (GitHub)](http://github.com/drscotthawley/SHAART) (in Python)  See <a href="#source">Running From Source</a> below for further instructions.
* [Sample WAV file](audio/sample_data.wav)



<a name="license"></a>

## License

2013 - 2015: This software is both "Open Source" and "Free," released under the Jesus license: "Freely you have received, freely give" (Matthew 10:8). Do as you like.  Modify, redistribute, etc.  

2015+: GPL 2. See [LICENSE.md](LICENSE.md) file.



<a name="tutorial"></a>

## Tutorials

* **General Instructions:**  Go up to the "File" tab and select an audio file to analyze.

  **TODO:** Add more here

* [Measuring Reverb Times with SHAART](https://github.com/drscotthawley/SHAART/blob/master/docs/rt60.md)

* [Creating Impulse Responses with SHAART](https://github.com/drscotthawley/SHAART/blob/master/docs/ir.md)



<a name="screenshots"></a>

## Screenshots

![rt60](images/rt60.png)

![power](images/power.png)



The spectrogram and waterfall plot (below) only show File A:

![spectro](images/spectro.png)

![waterfall](images/waterfall.png)



Note: The following 'Theoretical Steady-Steate Room Response' is pretty fake; it's just a bunch of superimposed parabolae, but without it this pane had a bunch of empty space:<br>
![modes](images/modes.png)



The values of absorption coefficients for the Sabine calculator come from the table in Chapter 8 of the Berg & Stork textbook:

![sabine](images/sabine.png)



The "invSpectro" feature created the file [mandrill.wav](audio/mandrill.wav) which has a spectrogram shown below:

![mandrill_spectro](images/mandrill_spectro.png)
<br>
And interestingly, if the audio is encoded as an MP3, then re-read and re-written as a WAV, one can see the "lossyness" of the MP3:<br>
![mandrill_mp3](images/mandrill_mp3_to_wav.png)
<br>
One can also apply various audio effects to the sound and see the effect on the image, e.g. echo:<br>
![echo](images/mandrill_echo.png)

Wah-wah:![wah](images/mandrill_wahwah.png)

Reverb:![reverb](images/mandrill_reverb.png)

And here's an interesting one: a "leveler" effect:<br>
![leveler](images/mandrill_leveler.png)
<br>

<a name="source"></a>

## Running from Source
<b>Running SHAART.py from source:</b><br>
Create a new Python environment and install dependencies:
```bash
pip install librosa pyqt6 pillow pyaudio numpy matplotlib
```

Then run...

```bash
cd SHAART/source
./SHAART.py
```



<a name="build"></a>

## Building an Executable

First follow the instructions above for running from source. Then we will proceed by using `pyinstaller`, that will create a new directory called `SHAART/source/dist/`, **in which a successful build will result in the presence of working binary executable.**

```bash
pip install pyinstaller
```

### Mac

In order to run from source, you'd already need to have XCode, the command-line tools, and HomeBrew installed. Then in we install `python.app` and [an older versions of a few things](https://github.com/pyinstaller/pyinstaller/issues/4067) to build the app:

```bash
pyinstaller SHAART.spec
```

...and you'll find `SHAART.app` in `source/dist/`.

### Linux (Pop!\_OS / Ubuntu)

We *could* re-use the .spec file from the Mac build, but it would give us a whole directory instead of one executable.  Instead, run this line:

```bash
pyinstaller SHAART.spec
```

...And then you can just run the `dist/SHAART` executable from the command line.   (Note: I can't seem to get it to be a "clickable icon" in Nautilus/Gnome.  Not sure how to do that.)

### Windows

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



## Changing the GUI

Run QT's `designer` or `Designer` app ([good luck finding this on your hard drive](https://stackoverflow.com/questions/37419138/is-qt-designer-bundled-with-anaconda), btw;  instead you might want to just [download QT from the main site](https://www.qt.io/)).  Open `ui_shaart.ui` as an input file.  Change the GUI as you like, save it, and then to generate the .py file, run

```bash
pyuic6 -x ui_shaart.ui -o ui_shaart.py
```



<a name="faq"></a>

## FAQ

* You do realize what the name "SHAART" sounds like...?  See "About" above.  thatsthejoke.jpg
* Can it only read WAV files?  No.  Despite saying WAV file everywhere, SHAART can read anything [librosa](https://librosa.github.io/librosa/) can read, which is...pretty much anything, e.g. WAV, AIFF, M4A,...?
* Can I get a logarithmic frequency scale for the spectrogram?  Not yet, but soon.
* For waterfall plots, it doesn't clear the window if you change the input data, resulting in multiple plots on the same page.  Bug or feature?
* Does the "Record" feature work?  Not yet. Use Audacity or....any other utility to record. ;-)
* How do I contribute to SHAART?  Submit a Pull Request!

<a name="notes"></a>

## Release Notes / Issues
* v0.8:
   * Upgrades for execution on M1 Macs: 
       * Upgraded from Qt5 to Qt6

* v0.7:

   * Updated code from Python 2.7 to Python 3.7
   * Updated GUI from Qt4 to Qt5
   * Switched executable build from py2app to PyInstaller, added capability for Windows & Linux executable builds
   * Re-ordered feature panes

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

Nomenclature:
The name is an acronym using the author's initials (S.H.), along with words
like "Acoustic," "Analysis," "Reverberation Time" or "Research Tools" -- as well
as, it is hoped, a lighthearted and not-legally-problematic play on words with
the name of the industry-standard SMAART audio analysis software made by
Rational Acoustics, Inc.  (SHAART is in no way affiliated with SMAART or
Rational Acoustics, fyi.)  ...I mean, "SHAART" is just hilarious to say.

Author: Dr. Scott H. Hawley, Associate Professor of Physics,
        Belmont University, Nashville TN USA.  
Date:   April 7, 2020 (original March 24, 2013)

Contact:  Improvements, bug reports, inquiries, donations, etc.: scott.hawley@(belmont)

<hr>
Author: <a href="http://hedges.belmont.edu/~shawley">Scott Hawley</a>
</body>
</html>

