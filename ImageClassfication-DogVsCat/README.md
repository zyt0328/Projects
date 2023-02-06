
Project name: Feline & Canine Convolutional Extractor

Project creation date: 2023/01/25




"Welcome to the Feline & Canine Convolutional Extractor project! This project aims to train a high-performing CNN model for cat and dog recognition to help people identify pictures of cats and dogs more efficiently. The trained model can be used for various interesting applications and we have demonstrated in our experiments that the refined data can be very effective in improving the accuracy of other general classification models. In this README file, you will find information on how to set up the required environment, access the datasets used, and run the code to train and use the model. We hope you find this project useful and we look forward to seeing how you use it!"


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

	Best_CNN_Model:
	This file shows how we trained our CNN dog and cat recognition model. We used close
    to 25,000 images of dogs and cats to train the model, and the training time was close to 90 minutes, 
    and the prediction accuracy was stable at about 91%. The accuracycan be further improved by increasing 
    the number of images in the training set and increasing the number of training rounds.


    DogVsCat:
	This folder holds our trained model and its parameters in Best_CNN_Model.
    Using the load_model function in Keras to use our model directly:
        myModel = tf.keras.models.load_model('DogVsCat')

    
    all_model:
	This file shows the improvement of each classification model from the refined data extracted 
    using our trained CNN model as a feature extractor.The training results of the common model are not 
    included in this paper, and all common models are given almost 50% accuracy. You can add your own code 
    to test the common model.        !!!For detailed information, please check our report.!!!



How to use our Model:

    Loading Model:
        model1 = tf.keras.models.load_model('DogVsCat')
    
    Continue training the model:
        model1.fit(Train_data, validation_data= Test_data ,epochs= 1, verbose= 1)
        

    Using our model as feature extractors:
        model2= Model(inputs=model1.input, outputs=myModel.layers[-6].output)
        new_train = model2.predict(Train_data)
        new_test = model2.predict(Test_data)

        fit the new train and test data into other General classification model.



Sources that have helped me:

    https://www.kaggle.com/code/ivanechen/deeplearning-cnn-dog-vs-cat-acc-93
    https://www.kaggle.com/code/vanausloos/solution-dogs-vs-cats-svm-model-model-2
    https://towardsdatascience.com/svm-support-vector-machine-for-classification-710a009f6873
    https://blog.csdn.net/my_name_is_learn/article/details/109536273
    https://www.bilibili.com/video/BV1rK4y147qn/?spm_id_from=333.788.recommend_more_video.-1&vd_source=1f2ec6ceeac061ecf5a257ffe5ce1896
    https://www.kaggle.com/datasets/trishalsingh/dogs-vs-cats
    https://zhuanlan.zhihu.com/p/41423739
    https://zhuanlan.zhihu.com/p/37777074
    https://stackoverflow.com/questions/48018457/removing-layers-from-a-pretrained-keras-model-gives-the-same-output-as-original
    https://www.mathworks.com/help/deeplearning/ug/preprocess-images-for-deep-learning.html

    
    
