Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> greyhounds = 500
>>> labs = 500
>>> grey_height = 28+4*np.random.randn(greyhounds)
>>> lab_height = 24+4*np.random.randn(labs)
>>> plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
([array([   0.,    0.,   11.,   39.,  100.,  125.,  137.,   59.,   23.,    6.]), array([   3.,   18.,   80.,  155.,  239.,  215.,  193.,   65.,   26.,    6.])], array([ 11.48217765,  14.32543459,  17.16869153,  20.01194848,
        22.85520542,  25.69846236,  28.5417193 ,  31.38497624,
        34.22823318,  37.07149012,  39.91474706]), <a list of 2 Lists of Patches objects>)
>>> plt.show()
