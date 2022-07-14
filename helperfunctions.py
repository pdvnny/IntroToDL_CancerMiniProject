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
import matplotlib.pyplot as plt
# import seaborn as sns

# This is the right idea now ... but I cannot load the entire dataset on my device. 
# There is too much data!!

def read_data():
    # get image filenames
    
    train_locs = glob.glob("train/*.tif")
    test_locs = glob.glob("test/*.tif")
    
    #train_locs = glob.glob("data/train/*.tif")
    #test_locs = glob.glob("data/test/*.tif")
    
    num_train = len(train_locs)
    num_test = len(test_locs)
    
    # initialize empty arrays for training and test data
    x_train = np.zeros((num_train, 96, 96, 3))
    x_train_IDs = []
    x_test = np.zeros((num_test, 96, 96, 3))
    x_test_IDs = []
    # y_train = I should be able to read in the csv directly actually....
    
    # get true labels for training data
    y_train_df = pd.read_csv("train_labels.csv", header=0)
    
    # Load data, reshape into a 1D vector and save a list of the file IDs
    for i, img_file in enumerate(train_locs):
        img = io.imread(img_file)        # NOTE: io.imread() reads images in as numpy.ndarray
        #img = img.reshape(1,96*96,3)
        x_train[i,:,:,:] = img
        x_train_IDs.append(img_file[6:-4])
    
    for i, img_file in enumerate(test_locs):
        img = io.imread(img_file)        # NOTE: io.imread() reads images in as numpy.ndarray
        #img = img.reshape(1,96*96,3)
        x_test[i,:,:,:] = img
        x_test_IDs.append(img_file[5:-4])
    
    return x_train, x_train_IDs, x_test, x_test_IDs, y_train_df


def load_image_info():
    # get image filenames
    
    # train_locs = glob.glob("train/*.tif")
    # test_locs = glob.glob("test/*.tif")
    
    train_locs = glob.glob("data/train/*.tif")
    test_locs = glob.glob("data/train/*.tif")
    
    num_train = len(train_locs)
    num_test = len(test_locs)
    
    y_train = pd.read_csv("train_labels.csv", header=0)
    
    return train_locs, test_locs, y_train

def show_training_image(img_info):
    # displaying the image
    file = "train/" + img_info.loc["id"] + ".tif"
    image = io.imread(file)
    plt.imshow(image)
    plt.title("{}\n Class: {}".format(img_info.loc["id"], img_info.loc["label"]))
    
    # Drawing the center 32x32 region on the picture
    rectangle = plt.Rectangle((32,32), 32, 32, ec="red", linewidth=1.5, fill=False)
    plt.gca().add_patch(rectangle)
    plt.legend(["Classification Region"])
    
def show_training_images(img_info, dim):
    fig, axes = plt.subplots(nrows=dim[0], ncols=dim[1], figsize=(10,8))
    
    ax = axes.flatten()
    plt.subplots_adjust(hspace=0.4)
    
    for i in range(len(img_info.index)):
        file = "train/" + img_info.loc[i,"id"] + ".tif"
        image = io.imread(file)
        ax[i].imshow(image)
        ax[i].set_title("{}\n Class: {}".format(img_info.loc[i,"id"], img_info.loc[i,"label"]))
        rectangle = plt.Rectangle((32,32), 32, 32, ec="red", linewidth=1.5, fill=False)
        ax[i].add_patch(rectangle)
        ax[i].legend(["Classification Region"])
        
def load_image_data(img):
    #file = "train/"+img+".tif"
    file = "data/train/"+img+".tif"
    image = io.imread(file)
    return image

""" From work on another projeect basically ... I used modified version above

def show_image(X, i):
    # select image
    image = X[i,:]
    # reshape into original image structure (32 x 32)
    image = image.reshape((32,32))
    # display the image
    plt.imshow(image)
    
def show_images(X, dim, lst):
    fig, axes = plt.subplots(nrows=dim[0], ncols=dim[1], figsize=(10, 8))
    
    images = []
    for img in lst:
        image = X[img, :]
        image.reshape((32,32))
        images.append(image) # assumes each image is a row in X
    
    for ax, image in zip(axes.flatten(), images):
        ax.imshow(image)   # I think this is all that is needed to produce the image
                            # additional arguments allow me to modify the images though
        ax.set_xticks(list(range(0,32,1)))
        ax.set_yticks(list(range(0,32,1)))
        
"""