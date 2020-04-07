# Creating Impulse Responses with SHAART

<a href="../index.html#downloads">Download SHAART</a>.

1. Create an exponential sine sweep of uniform amplitude.

   - You may create the sweep in SHAART by clicking on the "Equation" tab and leaving the default equation text in place and selecting "Go".  (The default is for a 10 second sweep from 20 Hz to 20000 Hz.)

     ```blah 
     0.8 * sin( 20 *2*PI*TMAX/ln(20000.0/20) * (exp(t/TMAX*ln(20000.0/20))-1) )
     ```

   - Alternatively you may generate a sweep in Audacity by selecting Generate > Chirp and then "Logarithmic". Be sure to set the starting and ending amplitudes to be the same.

2. Play the sweep from your speaker while recording the response.  (SHAART does not currently have recording functions).  Save the response to a WAV file.

3. In SHAART, choose "Equation" and this time copy & paste in the "Inverse Exponential Sine Sweep" equation text...

   ```
   exp(ln(20000.0/20)*(-t)/TMAX) * sin( 20 *2*PI*TMAX/ln(20000.0/20) * (exp((TMAX-t)/TMAX*ln(20000.0/20))-1) )
   ```

   ...and press Go.   This will go into "File A" in SHAART.

4. Load the response WAV file into "File B" in SHAART.

   A comparison of the two files now in memory will look like this:
   ![ir_sweep_and_inv](ir_sweep_and_inv_waveform.png)

5. Go to the "Convolve" tab and simply press "Go".  (No other instructions or actions are necessary.  Do not time-reverse file A).

6. File A now contains your Impulse Response!
   **TODO:** show screenshot(s) of constructed IR.



## Check: IR of a Dry Signal

If we use the 'original' (constant-amplitude, forward) sine sweep and convolve it with its 'inverse' (exponential-amplitude, backward) sweep, in theory we should get a Dirac delta function in time and a flat power spectrum.  Let's check:

1. Use the Equation feature to generate the forward sweep as File A and save it to a file: `sweep.wav`. 
2. Use the Equation feature to generate the 'Inverse filter' as File A (i.e. overwrite what's there), and keep it there.
3. Load back the original sweep file as File B.
4. Go the Convolve tab and press the big "GO!" button. 
5. Go back to the waveform display to see this 'spike': ![ir_delta](ir_delta.png)...which is not quite perfect but pretty 'impulsive'!
6. Check the power spectrum: is it flat? Press the Power tab to see this: ![ir_power](ir_power.png) ...pretty flat, eh? ;-) 

## References:

Farina: <a href="http://aurora-plugins.forumfree.it/?t=53443032">http://aurora-plugins.forumfree.it/?t=53443032</a>

Inv Exp Sweep: http://kc.koncon.nl/staff/pabon/IRM/IRMeasurementInstruction/assignment_IR_ExpSweepTheory.htm

<hr>
Author: <a href="http://hedges.belmont.edu/~shawley">Scott Hawley</a>
</body>
</html>