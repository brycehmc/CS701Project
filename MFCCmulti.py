from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy as np
import os, os.path
import fnmatch

training_data = []
testing_data = []
labels = []
testing_labels = []


num_files = 0
for dirpath, dirs, files in os.walk('recordings'):
   count_to_five = 0
   for filename in fnmatch.filter(files, '*.wav'):
      num_files += 1
      audiopath = dirpath+"/"+filename
      (rate, sig) = wav.read(audiopath, (count_to_five%5)==0)

      # computes the log of the Mel feature banks of the signal
      fbank_feat = logfbank(sig, rate)

      final_values = np.reshape(fbank_feat[1:52, :], -1)
      if count_to_five == 0:
         testing_data.append(final_values)
         if("tuti" in audiopath):
            testing_labels.append([0])
         elif("swth" in audiopath):
            testing_labels.append([1])
         elif("blgu" in audiopath):
   			testing_labels.append([2])
         elif("blja" in audiopath):
   			testing_labels.append([3])
         elif("grow" in audiopath):
   			testing_labels.append([4])
         elif("moch" in audiopath):
   			testing_labels.append([5])
         elif("modo" in audiopath):
   			testing_labels.append([6])
         elif("amcr" in audiopath):
   			testing_labels.append([7])
         elif("hosp" in audiopath):
            testing_labels.append([8])
         elif("coqu" in audiopath):
            testing_labels.append([9])
         #else:
         #   testing_labels.append([0])
      else:
         training_data.append(final_values)
         if("tuti" in audiopath):
            labels.append([0])
         elif("swth" in audiopath):
            labels.append([1])
         elif("blgu" in audiopath):
            labels.append([2])
         elif("blja" in audiopath):
   			labels.append([3])
         elif("grow" in audiopath):
   			labels.append([4])
         elif("moch" in audiopath):
   			labels.append([5])
         elif("modo" in audiopath):
   			labels.append([6])
         elif("amcr" in audiopath):
   			labels.append([7])
         elif("hosp" in audiopath):
            labels.append([8])
         elif("coqu" in audiopath):
            labels.append([9])

         #else:
         #   labels.append([0])

      count_to_five = (1+count_to_five)%5
print "The Number of Files is: "+ str(num_files)

np.savetxt("sound_attributes_mfccShort.csv", np.asarray(training_data), fmt='%f', delimiter=",")
np.savetxt("testing_attributes_mfccShort.csv", np.asarray(testing_data), fmt='%f', delimiter=",")
np.savetxt("sound_labels_mfccShort.csv", np.asarray(labels), fmt='%f', delimiter=",")
np.savetxt("testing_labels_mfccShort.csv", np.asarray(testing_labels), fmt='%f', delimiter=",")
