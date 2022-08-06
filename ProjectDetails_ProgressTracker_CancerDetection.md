# Parker Dunn
(pgdunn@bu.edu | pdunn91@gmail.com)  
Created on July 1st, 2022


__Assignment for COURSERA: Introduction to Deep Learning (via CU Boulder)__

__Assignment:__ Week 3 - CNN Cancer Detection Kaggle Mini-Project

## Progress...
[Done - 1st draft] Step 1 - Description of the data and problem  
[Done - 1st draft] Step 2 - EDA  
[Done] Step 3 - Model Achitecture

    * Discussed model design decisions
    * Designed and implemented a design testing procedure
    * Most architecture design work happened in this section
    * Varied -> layer design, CNN filter design, etc.
    * Held constant -> learning rate, momentum, etc.
    
[Almost Done] Step 4 -  Results and Analysis

	* Hyperparameter tuning
	* Trained model on all data
	* Used model to produce output
    * 

[] Step 5 -  
[ _ ] Step 6 -  



# Information about the Competition/Data
___

The Kaggle competition is called "Histopathologic Cancer Detection"  
LINK: https://www.kaggle.com/c/histopathologic-cancer-detection

### Data Description (from Kaggle)

In this dataset, you are provided with a large number of small pathology images to classify. Files are named with an image id. The train_labels.csv file provides the ground truth for the images in the train folder. You are predicting the labels for the images in the test folder. A positive label indicates that the center 32x32px region of a patch contains at least one pixel of tumor tissue. Tumor tissue in the outer region of the patch does not influence the label. This outer region is provided to enable fully-convolutional models that do not use zero-padding, to ensure consistent behavior when applied to a whole-slide image.

The original PCam dataset contains duplicate images due to its probabilistic sampling, however, the version presented on Kaggle does not contain duplicates. We have otherwise maintained the same data and splits as the PCam benchmark.
