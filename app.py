import numpy as np
import scipy.signal as sgn
import matplotlib.pyplot as plt
from scipy.io import wavfile as wv

img = plt.imread('./input/tree.jpg')
arr = np.array(img)
row, cols, color = arr.shape

s = arr.ravel()
print(s)

s = s/1.0
s = s/max(abs(s))
col = len(s)

print(s)

a = [1]
b = [-1, 2]
s1 = sgn.lfilter(b, a, s)

s1 = s1-min(s1)
s1 = s1/1.1/max(abs(s1))
plt.plot(s1)
plt.show()

wv.write('./output/tone.wav', 4000, s)

s1 = s1*255
s1 = s1.astype(int)

I1 = s1.reshape(row, cols, -1)

plt.imshow(I1)
plt.show()
