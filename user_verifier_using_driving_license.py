# -*- coding: utf-8 -*-
"""User Verifier using Driving License.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MjOK8cJlXaKFVihbgK0GeCS3Mk8bBJNG
"""

!pip install easyocr

import matplotlib.pyplot as plt
import cv2
import easyocr
import numpy as np
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en'])

from google.colab import files
uploaded = files.upload()

Image("Test.jpeg")



output = reader.readtext('Test.jpeg')

# for vertical
import re
print(output[2][1])
# getting DOB
for name in range(len(output)):
  print(name, output[name][1])
  if len(re.findall(r"../../.*", output[name][1].lower()))==1:
    print(name, output[name][1])
    break
# getting state
for name in range(len(output)):
  if len(re.findall(r".*gia", output[name][1].lower()))==1:
    print(name, output[name][1])

output2 = reader.readtext('Test.jpeg')

# for horizontal
import re
# getting DOB
for name in range(len(output2)):
  if len(re.findall(r"../../.*", output2[name][1].lower()))==1:
    print(name, output2[name][1])
    break
# getting state
for name in range(len(output2)):
  if len(re.findall(r".*gia", output2[name][1].lower()))==1:
    print(name, output2[name][1])
# getting id number
for name in range(len(output2)):
  if len(re.findall(r".*no", output2[name][1].lower()))==1:
    print(name, output2[name][1][9:])









