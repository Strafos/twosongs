import wave, array
import matplotlib.pyplot as plt
import time

filename = 'Macklemore_-_Glorious_Lyrics[www.MP3Fiber.com].wav'
wf = wave.open(filename,'rb')
bpms = list(array.array('i',wf.readframes(wf.getnframes())))

n = range(0, len(bpms)/100)
plt.plot(n,bpms[:len(bpms)/100])
plt.show()
time.sleep(100)
plt.close