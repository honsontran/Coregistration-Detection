import os
import shutil
import sys

DATASET_DIR = 'C:/Users/iFai1/Downloads/data-20200620T223847Z-003/'

image_dir = os.path.join(DATASET_DIR, 'data', 'train', 'img')
gt_dir = os.path.join(DATASET_DIR, 'data', 'train', 'gt')

masks = os.path.join(gt_dir, 'Class1/')

# Get collection of all unique images from our masks/classes
masks_labels = [f for f in os.listdir(masks)]

# walk through image dir
for entry in os.scandir(image_dir):
    
    # take image, find all corresponding labels to it
    if (entry.path.endswith(".tif") and entry.is_file()):
        
        # Check to see if a mask exists for this image
        if entry.name in masks_labels:
            continue        
        # Move the image to a not_found folder
        else:
            if not os.path.exists( os.path.join(image_dir, 'not_found') ):
                os.makedirs( os.path.join(image_dir, 'not_found') )
            os.rename( os.path.join(image_dir, entry.name), os.path.join(image_dir, 'not_found', entry.name) )

# Sanity Check, remember total images should be +1 more because of the not_found folder
all_labels = masks_labels
print('Total matching masks: ', len(all_labels))
print('Total Images: ', len([f for f in os.listdir(image_dir)]))