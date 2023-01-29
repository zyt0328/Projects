

Author: Yingtao Zhang
Project name: Feline Canine Convolutional Extractor
Project creation date: 2023/01/25


This project is a group project and one of our aims is to train a good CNN model for cat and dog 
recognition to help people identify 🐱 and 🐶 pictures faster and more efficiently. You are welcome 
to use our trained model to do some interesting things. We have demonstrated in our experiments 
that the refined data can be very effective in improving the accuracy of other basic models. Please
read our reprot for more details.


Prerequisites:

    Using Anoconda and Visual Studio Code is highly recommended 
	
	You should had Python3 installed on you machine
	
    Use the following line command to configure the required basic environment:
        
        conda create --name myenv

        conda activate myenv
        
        conda install numpy
        conda install pandas
        conda install matplotlib
        conda install scikit-learn
        conda install tensorflow
        conda install keras
        conda install -c conda-forge xgboost
        conda install -c conda-forge adaboost
        conda install -c anaconda itertools


    Please note that when you run the file you must be in the environment "myenv" that you created.
    Use the following code to activate the environment you have just created：

        conda activate myenv



Dataset :
    We used the cat and dog recognition dataset on Kaggle to train our model.
    Below are links to the two datasets we used:
    https://www.kaggle.com/datasets/karakaggle/kaggle-cat-vs-dog-dataset
    https://www.kaggle.com/datasets/tongpython/cat-and-dog

    Store the images in the dataset in the folder in the following format:
    |Best_CNN_Model.ipynb
    |Train|Cat|pictures...
          |Dog|pictures...
    |Test |Cat|pictures...
          |Dog|pictures...
    
    



Description of each document in the project:

	Best_CNN_Model:This file shows how we trained our CNN dog and cat recognition model. We used close
    to 25,000 images of dogs and cats to train the model, and the training time was close to 90 minutes, 
    and the prediction accuracy was stable at about 91%. The accuracycan be further improved by increasing 
    the number of images in the training set and increasing the number of training rounds.


    DogVsCat: This folder holds our trained model and its parameters in Best_CNN_Model.
    Using the load_model function in Keras to use our model directly:
        myModel = tf.keras.models.load_model('DogVsCat')

    
    all_model:This file shows the improvement of each classification model from the refined data extracted 
    using our trained CNN model as a feature extractor.The training results of the common model are not 
    included in this paper, and all common models are given almost 50% accuracy. You can add your own code 
    to test the common model.        !!!For detailed information, please check our report.!!!



How to use our Model:
    