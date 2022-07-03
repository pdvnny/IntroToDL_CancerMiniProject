""" ************************************************************************

    PARKER DUNN (pgdunn@bu.edu)
    
    Created on July 1st, 2022
    Assignment for COURSERA: Introduction to Deep Learning (CU Boulder)
    
    This file contains helper functions for my Week 3 mini-project
    assignment.

************************************************************************ """

from skimage import io
import glob

def read_data():
    
""" Above is supposed to be based on below

def read_data():
    
    # get image filenames
    cat_locs = glob.glob('petdataset/catsfolder/*.jpg')
    dog_locs = glob.glob('petdataset/dogsfolder/*.jpg')
    num_cats = len(cat_locs)
    num_dogs = len(dog_locs)
    
    # initialize empty arrays
    X_cats = np.zeros((num_cats,64*64))
    X_dogs = np.zeros((num_dogs,64*64))
    y_cats = np.zeros((num_cats,1))
    y_dogs = np.zeros((num_dogs,1))
              
    #Load data, reshape into a 1D vector and set labels
    
    keep_track = 0

    for i in range(num_cats):
        img = cat_locs[i]
        im = io.imread(img)
        im = im.reshape(64*64)
        X_cats[i,:] = im
        y_cats[i] = -1.0
        keep_track += 1

    for i in range(num_dogs):
        img = dog_locs[i]
        im = io.imread(img)
        im = im.reshape(64*64)
        X_dogs[i,:] = im
        y_dogs[i] = 1.0
        keep_track += 1
    
    # combine both datasets
    X = np.append(X_cats,X_dogs,0)
    y = np.append(y_cats,y_dogs)
    
    return X, y 

"""