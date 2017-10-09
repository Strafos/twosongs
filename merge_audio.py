import wave, array
import matplotlib.pyplot as plt
import time
import numpy
import scipy.io.wavfile

filename1 = 'Linkin Park - In Pieces [Lyrics on screen] HD-gVx_Qw1BrkQ.wav'
# BPM 160
first_beat1 = 676528
wf1 = wave.open(filename1,'rb')
# params = wf1.getparams()
bpms1 = (array.array('i',wf1.readframes(wf1.getnframes())))

filename2 = 'Ratatat - Gettysburg-PH_a2OcCmnI.wav'
wf2 = wave.open(filename2, 'rb')
params = wf2.getparams()
# BPM = 160
first_beat2 = 644880
bpms2 = (array.array('i',wf2.readframes(wf2.getnframes())))

diff = abs(first_beat1 - first_beat2)

# new_song = bpms2[:diff]
new_song = []
for (a,b) in zip(bpms1, bpms2):
    if abs(a+b) < 2**30-1:
        new_song.append(a+b)
    else:
        new_song.append(a)
# print(sum(bpms1)/float(len(bpms1)))

# new_song = [ for (a,b) in zip(bpms1, bpms2)]
# bpms2 = bpms2[diff:]
# mix = array.array([s1 + s2 for (s1, s2) in zip(bpms1, bpms2)])
# new_song += mix

out = numpy.asarray(new_song)
output = wave.open('combined.wav', 'wb')
print params
params = (params[0],params[1], params[2]*2, params[3], params[4], params[5])
output.setparams(params)
output.writeframes(out.tostring())
output.close()