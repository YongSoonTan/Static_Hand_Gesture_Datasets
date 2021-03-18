# Static Hand Gesture Datasets

# ASL dataset
All the RGB images have been moved into the same folder, you can download the dataset directly from the author [here](http://empslocal.ex.ac.uk/people/staff/np331/index.php?section=FingerSpellingDataset).
All RGB images in this dataset are resized into 28x28, running Read_and_divide_data_GrayScale.m (in Matlab, alternatively you can use Octave) will convert the RGB images into grayscale, and extract the label from image's file name, and subsequently generate the dataset with 50% of the images in training set, and the remaning 50% in testing set. The dataset is randomly shuffled and saved as GesTrainSubset, GesTestSubset.m (label encoding), and GesTrainSubset1, GesTestSubset1.m (one-hot encoding).

# ASL with digits
You can download the dataset directly from the author [here](https://www.massey.ac.nz/~albarcza/gesture_dataset2012.html).
Please run Resize_Images.m (in Matlab, alternatively you can use Octave) to resize the RGB images into 28x28 resolution.
Running Read_and_divide_data_GrayScale.m (in Matlab, alternatively you can use Octave) will convert the RGB images into grayscale, and extract the label from image's file name, and subsequently generate the dataset with 60% of the images in training set, and the remaning 40% in testing set. The dataset is randomly shuffled and saved as GesTrainSubset, GesTestSubset.m (label encoding), and GesTrainSubset1, GesTestSubset1.m (one-hot encoding).

# NUS hand gesture
You can download the dataset, NUS Hand Posture Dataset II (NUS-Hand-Posture-Dataset-II/Hand Postures), directly from the author [here](https://www.ece.nus.edu.sg/stfpage/elepv/NUS-HandSet/).
Please run Resize_Images.m (in Matlab, alternatively you can use Octave) to resize the RGB images into 28x28 resolution.
Running Read_and_divide_data_GrayScale.m (in Matlab, alternatively you can use Octave) will convert the RGB images into grayscale, and extract the label from image's file name, and subsequently generate the dataset with 60% of the images in training set, and the remaning 40% in testing set. The dataset is randomly shuffled and saved as GesTrainSubset, GesTestSubset.m (label encoding), and GesTrainSubset1, GesTestSubset1.m (one-hot encoding).

# 5-fold Cross Validation
To convert any of the aforementioned datasets into 5-fold cross validation dataset used in these two papers [CNN-SPP](https://link.springer.com/article/10.1007/s00521-020-05337-0), [EDenseNet](https://doi.org/10.1016/j.eswa.2021.114797), simply use the dataset with one-hot encoding (GesTrainSubset1.m, GesTestSubset1.m), and put them into a folder named 'gesture' -> '1' for ASL dataset, -> '2' for ASL with digits, -> '3' for NUS hand gesture, and then you can open Cross_Validation.py and set the variable on line 12 accordingly, and run it to generate dataset for cross validation once at a time. Please make sure to place this file under the same directory as the folder named 'gesture', please make sure the datasets are in the correct folder as well.

if you find this code useful for your research, please consider citing (citation will be updated again later):

    @article{tan2020convolutional,
      title={Convolutional neural network with spatial pyramid pooling for hand gesture recognition},
      author={Tan, Yong Soon and Lim, Kian Ming and Tee, Connie and Lee, Chin Poo and Low, Cheng Yaw},
      journal={Neural Computing and Applications},
      pages={1--13},
      year={2020},
      publisher={Springer}
    }
    
    @article{tan2021hand,
      title={Hand Gesture Recognition via Enhanced Densely Connected Convolutional Neural Network},
      author={Tan, Yong Soon and Lim, Kian Ming and Lee, Chin Poo},
      journal={Expert Systems with Applications},
      pages={114797},
      year={2021},
      publisher={Elsevier}
    }
