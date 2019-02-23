
import pickle
import os
import shutil
import array
import glob
from os import listdir, getcwd
from os.path import join
from PIL import Image, ImageFilter, ImageColor,ImageEnhance,ImageCms,ImageChops,ImageOps,ImageTransform

import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
import multiprocessing as mp
from mpl_toolkits.mplot3d import Axes3D

# add new line

x=np.linspace(-3,3,50)

y1=2*x+1
y2=x**2
plt.figure()
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.plot(x,y2)

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('i am x')
plt.ylabel('i am y')
                
new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
           ['$really\ bad$','$bad$','$normal$','$cood$','$really\ cood$'])
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))

plt.show()
