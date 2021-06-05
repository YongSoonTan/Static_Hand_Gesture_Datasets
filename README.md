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

    @article{tan2021convolutional,
      title={Convolutional neural network with spatial pyramid pooling for hand gesture recognition},
      author={Tan, Yong Soon and Lim, Kian Ming and Tee, Connie and Lee, Chin Poo and Low, Cheng Yaw},
      journal={Neural Computing and Applications},
      volume={33},
      number={10},
      pages={5339--5351},
      year={2021},
      publisher={Springer}
    }
    
    @article{TAN2021114797,
    title = {Hand gesture recognition via enhanced densely connected convolutional neural network},
    journal = {Expert Systems with Applications},
    volume = {175},
    pages = {114797},
    year = {2021},
    issn = {0957-4174},
    doi = {https://doi.org/10.1016/j.eswa.2021.114797},
    url = {https://www.sciencedirect.com/science/article/pii/S0957417421002384},
    author = {Yong Soon Tan and Kian Ming Lim and Chin Poo Lee},
    keywords = {Sign language recognition, Hand gesture recognition, Convolutional neural network (CNN), Enhanced densely connected convolutional neural network (EDenseNet)}
    }
    
If you use any of the datasets, please cite their papers accordingly.

For ASL dataset

    @inproceedings{pugeault2011spelling,
      title={Spelling it out: Real-time ASL fingerspelling recognition},
      author={Pugeault, Nicolas and Bowden, Richard},
      booktitle={2011 IEEE International conference on computer vision workshops (ICCV workshops)},
      pages={1114--1119},
      year={2011},
      organization={IEEE}
    }
    
For ASL with digits

    @article{barczak2011new,
      title={A new 2D static hand gesture colour image dataset for ASL gestures},
      author={Barczak, ALC and Reyes, NH and Abastillas, M and Piccio, A and Susnjak, T},
      year={2011},
      publisher={Massey University}
    }
    
For NUS hand gesture 

    @article{pisharady2013attention,
      title={Attention based detection and recognition of hand postures against complex backgrounds},
      author={Pisharady, Pramod Kumar and Vadakkepat, Prahlad and Loh, Ai Poh},
      journal={International Journal of Computer Vision},
      volume={101},
      number={3},
      pages={403--419},
      year={2013},
      publisher={Springer}
    }
