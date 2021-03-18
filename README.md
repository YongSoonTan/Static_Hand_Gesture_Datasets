# Static Hand Gesture Datasets

# ASL dataset
All the RGB images are moved into the same folder, you can download the dataset directly from the author [here](http://empslocal.ex.ac.uk/people/staff/np331/index.php?section=FingerSpellingDataset).
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
To convert any of the aforementioned datasets into 5-fold cross validation dataset used in these two papers [CNN-SPP](https://link.springer.com/article/10.1007/s00521-020-05337-0), [EDenseNet](https://doi.org/10.1016/j.eswa.2021.114797), simply use the dataset with one-hot encoding (GesTrainSubset1.m, GesTestSubset1.m), and put them into a folder named 'gesture' -> '1' for ASL dataset, -> '2' for ASL with digits, -> '3' for NUS hand gesture, and then you can open Cross_Validation.py and set the variable on line 12 accordingly, and run it to generate dataset for cross validation once at a time.
