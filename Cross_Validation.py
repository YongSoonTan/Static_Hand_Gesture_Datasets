# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:41:58 2019

@author: Soon_
"""

import scipy.io as sio
import os
import numpy as np

dataset = '1'
path = os.path.join('gesture', dataset)
Train =sio.loadmat(os.path.join(path, 'GesTrainSubset1.mat'))
Test = sio.loadmat(os.path.join(path, 'GesTestSubset1.mat'))
#Test = sio.loadmat(os.path.join(path, 'D1_1st_fold_test.mat'))
Train_Images = Train['trainImages']
Train_Labels = Train['trainLabels2']
total_trainImages = len(Train_Images[0,2])
Test_Images = Test['testImages']
Test_Labels = Test['testLabels2']
total_testImages = len(Test_Images[0,2])

All_Images = np.concatenate((Train_Images,Test_Images), axis=2)
All_Labels = np.concatenate((Train_Labels, Test_Labels), axis=1)

if path == 'gesture\\1':
    f1_images = All_Images[:,:,:13155]
    s2_images = All_Images[:,:,13155:26310] 
    t3_images = All_Images[:,:,26310:39465]
    f4_images = All_Images[:,:,39465:52620]
    f5_images = All_Images[:,:,52620:]
    
    f1_labels = All_Labels[:,:13155]
    s2_labels = All_Labels[:,13155:26310]
    t3_labels = All_Labels[:,26310:39465]
    f4_labels = All_Labels[:,39465:52620]
    f5_labels = All_Labels[:,52620:]
    
    #1st fold
    Train_Images = np.concatenate((s2_images,t3_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((s2_labels,t3_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = f1_images
    Test_Labels = f1_labels
    sio.savemat('D1_1st_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D1_1st_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #2nd fold
    Train_Images = np.concatenate((f1_images,t3_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,t3_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = s2_images
    Test_Labels = s2_labels
    sio.savemat('D1_2nd_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D1_2nd_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #3rd fold
    Train_Images = np.concatenate((f1_images,s2_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = t3_images
    Test_Labels = t3_labels
    sio.savemat('D1_3rd_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D1_3rd_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #4th fold
    Train_Images = np.concatenate((f1_images,s2_images,t3_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,t3_labels,f5_labels), axis=1) 
    Test_Images = f4_images
    Test_Labels = f4_labels
    sio.savemat('D1_4th_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D1_4th_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #5th fold
    Train_Images = np.concatenate((f1_images,s2_images,t3_images,f4_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,t3_labels,f4_labels), axis=1) 
    Test_Images = f5_images
    Test_Labels = f5_labels
    sio.savemat('D1_5th_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D1_5th_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
if path == 'gesture\\2':
    f1_images = All_Images[:,:,:503]
    s2_images = All_Images[:,:,503:1006]
    t3_images = All_Images[:,:,1006:1509]
    f4_images = All_Images[:,:,1509:2012]
    f5_images = All_Images[:,:,2012:]
    
    f1_labels = All_Labels[:,:503]
    s2_labels = All_Labels[:,503:1006]
    t3_labels = All_Labels[:,1006:1509]
    f4_labels = All_Labels[:,1509:2012]
    f5_labels = All_Labels[:,2012:]
    
    #1st fold
    Train_Images = np.concatenate((s2_images,t3_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((s2_labels,t3_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = f1_images
    Test_Labels = f1_labels
    sio.savemat('D2_1st_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D2_1st_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #2nd fold
    Train_Images = np.concatenate((f1_images,t3_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,t3_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = s2_images
    Test_Labels = s2_labels
    sio.savemat('D2_2nd_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D2_2nd_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #3rd fold
    Train_Images = np.concatenate((f1_images,s2_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = t3_images
    Test_Labels = t3_labels
    sio.savemat('D2_3rd_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D2_3rd_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #4th fold
    Train_Images = np.concatenate((f1_images,s2_images,t3_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,t3_labels,f5_labels), axis=1) 
    Test_Images = f4_images
    Test_Labels = f4_labels
    sio.savemat('D2_4th_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D2_4th_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #5th fold
    Train_Images = np.concatenate((f1_images,s2_images,t3_images,f4_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,t3_labels,f4_labels), axis=1) 
    Test_Images = f5_images
    Test_Labels = f5_labels
    sio.savemat('D2_5th_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D2_5th_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
if path == 'gesture\\3':
    f1_images = All_Images[:,:,:400]
    s2_images = All_Images[:,:,400:800]
    t3_images = All_Images[:,:,800:1200]
    f4_images = All_Images[:,:,1200:1600]
    f5_images = All_Images[:,:,1600:]
    
    f1_labels = All_Labels[:,:400]
    s2_labels = All_Labels[:,400:800]
    t3_labels = All_Labels[:,800:1200]
    f4_labels = All_Labels[:,1200:1600]
    f5_labels = All_Labels[:,1600:]
    
    #1st fold
    Train_Images = np.concatenate((s2_images,t3_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((s2_labels,t3_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = f1_images
    Test_Labels = f1_labels
    sio.savemat('D3_1st_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D3_1st_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #2nd fold
    Train_Images = np.concatenate((f1_images,t3_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,t3_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = s2_images
    Test_Labels = s2_labels
    sio.savemat('D3_2nd_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D3_2nd_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #3rd fold
    Train_Images = np.concatenate((f1_images,s2_images,f4_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,f4_labels,f5_labels), axis=1) 
    Test_Images = t3_images
    Test_Labels = t3_labels
    sio.savemat('D3_3rd_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D3_3rd_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #4th fold
    Train_Images = np.concatenate((f1_images,s2_images,t3_images,f5_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,t3_labels,f5_labels), axis=1) 
    Test_Images = f4_images
    Test_Labels = f4_labels
    sio.savemat('D3_4th_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D3_4th_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	
    
    #5th fold
    Train_Images = np.concatenate((f1_images,s2_images,t3_images,f4_images), axis=2)
    Train_Labels = np.concatenate((f1_labels,s2_labels,t3_labels,f4_labels), axis=1) 
    Test_Images = f5_images
    Test_Labels = f5_labels
    sio.savemat('D3_5th_fold_train.mat', {'trainImages':Train_Images, 'trainLabels2': Train_Labels},do_compression=True)		
    sio.savemat('D3_5th_fold_test.mat', {'testImages':Test_Images, 'testLabels2': Test_Labels},do_compression=True)	