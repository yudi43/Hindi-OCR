import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image

rcParams['figure.figsize'] = 8, 16
reader = easyocr.Reader(['en', 'hi'])

file_name = "Image.png"

Image(file_name)

#output is a list of tuples, the first one is the co-ordinate of the text and the second is the predicted hindi text.
#and the third item in the tuple is the prediction accuracy.
output =  reader.readtext(file_name)

for i in output:
    print("this is where it starts")
    print(i)
