from pydub import AudioSegment
from pydub.utils import make_chunks
import os, os.path
import fnmatch
"""for i in range(1,31):
    filename = "/Users/Brycemcintyre/Desktop/CS 701/SpringTerm/recordings/SWTH/SWTH" + str(i)+ ".wav"
    y, sr = lib.load(filename, sr = 44100)
    lib.output.write_wav("/Users/Brycemcintyre/Desktop/CS 701/SpringTerm/recordings/SWTH" + str(i)+".wav",y, sr)"""

for dirpath, dirs, files in os.walk('recordings'):
    for filename in fnmatch.filter(files, '*.wav'):
        audiopath = dirpath+"/"+filename
        myaudio = AudioSegment.from_file(audiopath , "wav")
        chunk_length_ms = 10000 # pydub calculates in millisec
        chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
        #Export all of the individual chunks as wav files
        for i, chunk in enumerate(chunks):
            chunk_name = filename + "chunk{0}.wav".format(i)
            print "exporting", chunk_name
            chunk.export("chunks/" + chunk_name, format="wav")
