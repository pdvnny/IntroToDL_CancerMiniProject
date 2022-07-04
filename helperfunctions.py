""" ************************************************************************

    PARKER DUNN (pgdunn@bu.edu)
    
    Created on July 1st, 2022
    Assignment for COURSERA: Introduction to Deep Learning (CU Boulder)
    
    This file contains helper functions for my Week 3 mini-project
    assignment.

************************************************************************ """

from skimage import io
import pandas as pd
import numpy as np
import glob

def read_data():
    # get image filenames
    train_locs = glob.glob("train/*.tif")
    test_locs = glob.glob("test/*.tif")
    num_train = len(train_locs)
    num_test = len(test_locs)
    
    # initialize empty arrays for training and test data
    x_train = np.zeros((num_train, 96*96))
    x_train_IDs = []
    x_test = np.zeros((num_test, 96*96))
    x_test_IDs = []
    # y_train = I should be able to read in the csv directly actually....
    
    # get true labels for training data
    y_train_df = pd.read_csv("train_labels.csv", header=0)
    
    # Load data, reshape into a 1D vector and save a list of the file IDs
    for i, img_file in enumerate(train_locs):
        img = io.imread(img_file)        # NOTE: io.imread() reads images in as numpy.ndarray
        img = img.reshape(1,96*96,3)
        x_train[i,:] = img
        x_train_IDs.append(img_file[6:-4])
    
    for i, img_file in enumerate(test_locs):
        img = io.imread(img_file)        # NOTE: io.imread() reads images in as numpy.ndarray
        img = img.reshape(1,96*96,3)
        x_test[i,:] = img
        x_test_IDs.append(img_file[5:-4])
    
    return x_train, x_train_IDs, x_test, x_test_IDs, y_train_df