import scipy
import numpy as np
import librosa as lib
import matplotlib.pyplot as plt

#resamples files to 44100Hz for consistency
for i in range(1,31):
    filename = "/Users/Brycemcintyre/Desktop/CS 701/SpringTerm/recordings/SWTH/SWTH" + str(i)+ ".wav"
    y, sr = lib.load(filename, sr = 44100)
    lib.output.write_wav("/Users/Brycemcintyre/Desktop/CS 701/SpringTerm/recordings/SWTH" + str(i)+".wav",y, sr)
    #S = lib.feature.melspectrogram(y=y, sr=sr)
    #np.savetxt("melspecs/melspec"+str(i)".csv" , S, fmt='% f', delimiter=",")

#s = scipy.signal.wiener(S)
