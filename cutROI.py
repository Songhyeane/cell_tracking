import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets  import RectangleSelector
import tifffile as tiff
from PIL import Image
import pims
import os

datas_path_dir = 'C:/Users/1/Desktop/workspace/datas'
datas_list = os.listdir(datas_path_dir)
print(datas_list)

original_path = datas_path_dir+'/'+datas_list[2]
cropped_path = datas_path_dir+'/'+datas_list[0]
finished_path = datas_path_dir+'/'+datas_list[1]
result_path = datas_path_dir+'/'+datas_list[3]

print(f'original_path:{original_path} cropped_path:{cropped_path} finished_path:{finished_path} result_path:{result_path} ')

original_datas_list = os.listdir(original_path)
print(original_datas_list)

x_range = [0,0]
y_range = [0,0]

img = tiff.imread(original_path+'/'+original_datas_list[0])
img_array = np.array(img)

fig, ax = plt.subplots()
imgs = ax.imshow(img_array[:][0], cmap = 'gray')
print(img_array[:][0])


def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    print(" The button you used were: %s %s" % (eclick.button, erelease.button))

    global x_range
    global y_range

    x_range = [x1,x2]
    y_range = [y1,y2]

rs = RectangleSelector(ax, line_select_callback,
                       useblit=False, button=[1,3],
                       minspanx=5, minspany=5, spancoords='pixels',
                       interactive=True)
plt.show()

crop_img_array = img_array[:][0][int(y_range[0]):int(y_range[1]),int(x_range[0]):int(x_range[1])]

print(crop_img_array)

fig, ax = plt.subplots()
imgs = ax.imshow(crop_img_array , cmap = 'gray')

plt.show()

