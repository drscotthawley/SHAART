
<head>
<link rel="SHORTCUT ICON" href="shaart_logo.jpg" />
<link rel="image_src" href="http://hedges.belmont.edu/~shawley/SHAART/shaart_logo.jpg" />
<meta property="og:image" content="http://hedges.belmont.edu/~shawley/SHAART/shaart_logo.jpg" />
<meta property="og:url" content="http://hedges.belmont.edu/~shawley/SHAART" />
<meta property="og:title" content="SHAART Acoustic Tools" />

<meta keywords="">



</head>
<body>
Main web page: http://hedges.belmont.edu/~shawley/SHAART/index.html<br><br>

<p align="center">
<cente>
SHAART Acoustic Tools, v 0.6<br>
(Feb 12, 2016)<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/shaart_logo.jpg"><br>
(yes, the name is a joke)<br>
<a href="#about">About</a> &nbsp;&nbsp;
<a href="#downloads">Downloads</a> &nbsp;&nbsp;
<a href="#notes">Release Notes</a> &nbsp;&nbsp;
<a href="#license">License</a> &nbsp;&nbsp;
<a href="#screenshots">Screenshots</a> &nbsp;&nbsp;
<a href="#source">Running From Source</a> <br>
<a href="#tutorial">Tutorial(s)</a><br>
<br><br>
</p>

<a name="about"><h2>About</h2></a>
This lightweight audio analysis suite was initially written <b><i>for educational purposes only</i></b> 
over a period of 4 days.  (And then improved in bits.)<br>
It's amazing how much you can accomplish with minimal knowledge of Python programming.<br>
<br>
The name "SHAART" uses the author's initials (S.H.) in homage to the famous "SMAART" set of acoustics analysis tools.<br> 
That and "SHAART" is just hilarious to say, for other reasons. <br>
<i>(Note: "homage" = parody, derivative work = fair use = please don't sue.)</i><br>
<br>
<a name="downloads"><h2>Downloads</h2></a>
<a href="SHAART.app.tar.gz">Mac Binary Application</a> (105 MB, Yosemite - OS X 10.10);
  <a href="SHAART.tar.gz">Source code</a> (in Python); 
<a href="sample_data.wav">Sample WAV file</a><br>
(For those interested in using the source code, see the bottom of this page for further instructions.)<br>
<br>
<a name="license"><h2>License</h2></a>
This software is both "Open Source" and "Free," released under the Jesus license: "Freely you have received, freely give" 
(Matthew 10:8).
Do as you like.  Modify, redistribute, etc.  See the <a href="https://github.com/l0veweap0n/SHAART">GitHub repository</a> <br>
<br>

<a name="tutorial"><h2>Tutorial(s)</h2></a>
<ul>
  <li><a href="ir.html">Creating Impulse Responses with SHAART</a>
</ul>

<a name="notes"><h2>Release Notes/Issues</h2></a>
<ul>
 <li>v0.5:  
    <ul> <li>Got its own App icon!  
         <li>"Power": Improved power spectrum calculation and display.  
          <li>"Equation": Added equation for inverse exp. sine sweep (with "depinking").
         <li>Added IR creation tutorial (documentation)
     </ul>
 <li>Despite saying WAV file everywhere, the newest version of SHAART will read AIFF files too.  And the previous issue with 24-bit PCM WAV files has been resolved.</li>
<li> You don't need a WAV file to use the room mode calculator or the Sabine calculator.  </li>
<li> No you can't get a logarithmic frequency scale for the spectrogram.  Not yet.</li>
<li> For waterfall plots, it doesn't clear the window if you change the input data, resulting in multiple plots on the same page.  Bug or feature?</li>
</ul>

<a name="screenshots"><h2>Screenshots</h2></a>
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
invSpectro (above) created the file <a href="lena.wav">lena.wav</a>, which has a spectrogram shown below:<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/lena_spectro.jpg" width=600><br>
<br>
And interestingly, if lena.wav is encoded as an MP3, then re-read and re-written as a WAV, one can see the "lossyness" of the MP3:<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/lena_mp3_to_wav.jpg" width=600><br>
<br>
One can also apply various audio plugins to the sound and see the effect on the image, e.g. echo:<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/lena_echo.jpg" width=600><br>
Wah-wah:<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/lena_wahwah.jpg" width=600><br>
Reverb:<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/lena_reverb.jpg" width=600><br>
And here's an interesting one: a "leveler" effect turns Lena into a vampire:<br>
<img src="http://hedges.belmont.edu/~shawley/SHAART/screenshots/lena_leveler.jpg" width=600><br>
<br>
<a name="source"><h2>Running from Source</h2>
<b>Running SHAART.py from source, via Python and MacPorts:</b><br>
First, we'll assume you have already <a href="https://www.macports.org/install.php">installed MacPorts</a>. (Hint: To get the XCode Command Line Tools without creating an Apple Developer account, after you install Xcode, go into a terminal shell and run "xcode-select --install".  Voila!)<br>
Then make sure you have all the ports/packages you need:<br>
<pre>sudo port install py27-numpy py27-scipy py27-matplotlib py27-pil py27-pyqt4 py27-pyaudio py27-scikits-samplerate libsndfile; sudo easy_install-2.7 scikits.audiolab </pre>
Then don't forget to run python select:<br>
<pre>sudo port select python python27</pre>
Then you should be good to go!  Just <pre>tar xvfz SHAART.tar.gz</pre>...then <pre>cd SHAART</pre>
Finally, "./SHAART.py" should run it!
<br>
<br>
Or, for the truly ambitious:<br>
<b>Building a SHAART.app binary from source</b><br>
Make sure you can run SHAART.py as described above, before proceeding.  The build requires py2app, which used to have issues with
MacPorts, however the newer versions of MacPorts seemed to work now.  So, run <br>
<pre>sudo port install py27-py2app</pre>
<!---unless you want py2app to abort the build with the error "New Mach-O header is too large to relocate", you will need to take 
drastic measures, as follows... (The following info gleaned from <a href="http://www.danplanet.com/blog/2009/02/15/using-py2app-with-gtk/">here</a>.)<br>
<ul>
<li>
First, back up your /opt/local directory, because you're about to break <b>everything</b>:  "cd /opt; sudo cp -r local local.bak"</li>
<li>Then uninstall MacPorts (that's right): following <a href="http://guide.macports.org/chunked/installing.macports.uninstalling.html">these instructions</a>.</li>
<li>
Then do a <a href="https://www.macports.org/install.php">fresh install of MacPorts</a>. 
Before installing other ports, edit the file (as superuser) /opt/local/share/macports/Tcl/port1.0/portconfigure.tcl
so that the line "default configure.ldflags" reads:  <br>
default configure.ldflags   {"-L${prefix}/lib -Xlinker -headerpad_max_install_names"}<br>
</li>

<li>You are now free to re-install <b>every port you ever installed</b>, including the list above. </li>
-->

Then cd into the SHAART source directory and run<br>
<pre>/opt/local/bin/python setup.py py2app</pre>
and wait around while it builds.  If successfull, you will find "SHAART.app" in a new subdirectory called "dist"!
<hr>
Author: <a href="http://www.scotthawley.com">Scott Hawley</a>
</body>
</html>





More docs & info:

<pre>
================================================================================
SHAART 

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
Date:   March 24, 2013

Contact:
Improvements, bug reports, inquiries, donations, etc.: scott.hawley@(belmont)
================================================================================


Usage:
=====
Go up to the "File" tab (or press command-O) and select a WAV file to analyze.

Note: SHAART was made using Python and the SciPy package (among others).  SciPy 
can read *some* WAV files but not others.  Not sure why.  If you're having file 
input issues, including wanting to read some other format (e.g., MP3), then try
loading your file into Audacity and exporting it as a WAV.  Then read the new 
file with SHAART.

Note: You don't need a WAV file to use the room mode calculator.


Running/Building from Source:
============================
Running from source requires python packages pyqt4, scipy, numpy, matplotlib, 
...aaaand probably a host of others.  Just run ./SHAART.py.

To modify the user interface: The interface was built on QT4 using the QT 
Designer application, which reads & saves the file ui_shaart.ui:
% Designer ui_shaart.ui 
--> note: on MacPorts, Designer is no longer accessible from the command line,
rather it is an app in /Applications/MacPorts/Designer.app

This is then converted to a python script by running, e.g.,

%  pyuic4-2.7 ui_shaart.ui > ! ui_shaart.py

There is also a setup.py file provided for building a standalone application 
via py2app:

% python setup.py py2app

The final application gets placed in a new subdirectory called dist/. 
Note that even if the py2app build looks like it fails, there will usually be
a fully-functional application waiting in dist/ anyway!

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



SHAART. 
</pre>
