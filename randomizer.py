from pydub import AudioSegment
from pydub.utils import make_chunks
import os, os.path
import fnmatch
import random
alph = "abcdefghijklmnopqrstuvwqyz"
"""for i in range(1,31):
    filename = "/Users/Brycemcintyre/Desktop/CS 701/SpringTerm/recordings/SWTH/SWTH" + str(i)+ ".wav"
    y, sr = lib.load(filename, sr = 44100)
    lib.output.write_wav("/Users/Brycemcintyre/Desktop/CS 701/SpringTerm/recordings/SWTH" + str(i)+".wav",y, sr)"""

for dirpath, dirs, files in os.walk('recordings'):
    for filename in fnmatch.filter(files, '*.wav'):
        x = random.randint(0,25)
        os.rename(dirpath + "/" + filename, dirpath + "/" + alph[x] + filename)
