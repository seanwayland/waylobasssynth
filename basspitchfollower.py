

from pyo import *

# Creates and boots the server.
# The user should send the "start" command from the GUI.
s = Server(sr=96000, buffersize=1000 ).boot()
s.start()
a = Input(chnl=0)

# Drops the gain by
s.amp = 0.5
# envelope pollower
fol2= Follower2(a, risetime=0.001, falltime=.01)
# pitch detection
pit = Yin(a, tolerance=0.2,minfreq=10, maxfreq=1000, cutoff = 1000, winsize=3000)

# Creates a sine wave player.
# The out() method starts the processing
# and sends the signal to the output.
b = Sine(freq=pit, mul=fol2).out(0)
c = Sine(freq=pit, mul=fol2).out(1)
# octave lower
d = Sine(freq=pit/2, mul=fol2).out(0)
e = Sine(freq=pit/2, mul=fol2).out(1)

# Opens the server graphical interface.
s.gui(locals())
