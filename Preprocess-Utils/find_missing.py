import os
import shutil
import sys

DATASET_DIR = 'C:/Users/iFai1/Documents/GitHub/Coregistration-Detection/Detection/Mask-RCNN/datasets/spine_segmented/'

image_dir = os.path.join(DATASET_DIR, 'data', 'train', 'img')
gt_dir = os.path.join(DATASET_DIR, 'data', 'train', 'gt')

c1 = os.path.join(gt_dir, 'Class1/')
c2 = os.path.join(gt_dir, 'Class2/')
c3 = os.path.join(gt_dir, 'Class3/')
c4 = os.path.join(gt_dir, 'Class4/')


# Get collection of all unique images from our masks/classes
c1_labels = [f for f in os.listdir(c1)]
c2_labels = [f for f in os.listdir(c2)]
c3_labels = [f for f in os.listdir(c3)]
c4_labels = [f for f in os.listdir(c4)]

# walk through image dir
for entry in os.scandir(image_dir):
    
    # take image, find all corresponding labels to it
    if (entry.path.endswith(".tif") and entry.is_file()):
        
        # Check to see if a mask exists for this image
        if entry.name in c1_labels:
            continue
        if entry.name in c2_labels:
            continue
        if entry.name in c3_labels:
            continue
        if entry.name in c4_labels:
            continue
        
        # Move the image to a not_found folder
        else:
            if not os.path.exists( os.path.join(image_dir, 'not_found') ):
                os.makedirs( os.path.join(image_dir, 'not_found') )
            os.rename( os.path.join(image_dir, entry.name), os.path.join(image_dir, 'not_found', entry.name) )

# Sanity Check, remember total images should be +1 more because of the not_found folder
all_labels = c1_labels + c2_labels + c3_labels + c4_labels
all_labels = list(dict.fromkeys(all_labels))
print('Total matching masks: ', len(all_labels))
print('Total Images: ', len([f for f in os.listdir(image_dir)]))