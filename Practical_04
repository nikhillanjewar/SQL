
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm


#_Reading The Image 
srcImage = plt.imread("moonlanding.png").astype(float) 
#displaying the orignal image 
plt.figure()
plt.imshow(srcImage,plt.cm.gray) 
plt.title("Source Image")
plt.show()


fftImage = fftpack.fft2(srcImage)
plt.imshow(np.abs(fftImage),norm=LogNorm(vmin=5)) 
plt.colorbar()
plt.title("Fourier Transform Of Image")
plt.show()

#Constant for keeping the compoent frequencies 
Constant Fraction = 0.1
#Creating copy of FFT-Images 
fftImage1 = fftImage.copy()
row, column = fftImage1.shape
fftImage1[int(row*constantFraction):int(row*(1-constantFraction))] = 0
fftImage1[:, int(column*constant Fraction):int(column*(1-constantFraction))] = 0

#Plotting the figure 
plt.figure()
plt.imshow(np.abs(fftImage1),norm=LogNorm(vmin=5))
plt.colorbar()
plt.title("Filtered Spectrum")
plt.show()
newImage = fftpack.ifft2(fftImage1).real
plt.figure()
plt.imshow(newImage,plt.cm.gray)
plt.title("Denoised Image")
plt.show()
