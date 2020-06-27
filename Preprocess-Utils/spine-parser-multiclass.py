import os
import shutil
import sys

DATASET_DIR = 'C:/Users/iFai1/Desktop/Cornell/MRCNN_Iteration/RCNN_data_clean/spine/'

image_dir = os.path.join(DATASET_DIR, 'Image/')
gt_dir = os.path.join(DATASET_DIR, 'mask/')

c1 = os.path.join(DATASET_DIR, 'mask/', 'Class1/')
c2 = os.path.join(DATASET_DIR, 'mask/', 'Class2/')
c3 = os.path.join(DATASET_DIR, 'mask/', 'Class3/')
c4 = os.path.join(DATASET_DIR, 'mask/', 'Class4/')

labels = [f for f in os.listdir(gt_dir)]

# walk through image dir
for entry in os.scandir(image_dir):
    
    # take image, find all corresponding labels to it
    if (entry.path.endswith(".tif") and entry.is_file()):
        
        # Get list of all relevant labels
        classes = [x for x in labels if entry.name[:-4] in x]
        
        # Put them into the corresponding folders, and rename them
        for f in classes:
            if "_1" in f:
                print('_1 found')
                os.rename(os.path.join(gt_dir, f), os.path.join(c1, f[:-6]+'.tif'))
            if "_2" in f:
                print('_2 found')
                os.rename(os.path.join(gt_dir, f), os.path.join(c2, f[:-6]+'.tif'))
            if "_3" in f:
                print('_3 found')
                os.rename(os.path.join(gt_dir, f), os.path.join(c3, f[:-6]+'.tif'))
            if "_4" in f:
                print('_4 found')
                os.rename(os.path.join(gt_dir, f), os.path.join(c4, f[:-6]+'.tif'))                