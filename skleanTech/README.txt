Author: Yingtao Zhang
VNumber: V00943483
Project name: ID3Tree
Project creation date: 2022/09/25




Introduction: 
	Sklearn is a machine learning tool based on the Python language. It is intended to be used in conjunction with NumPy, SciPy, Pandas and Matplotlib. It has six main task modules: classification, regression, clustering, dimensionality reduction, model selection and preprocessing, respectively.	



Prerequisites:
	
	You should had pandas installed on you machine
	You should had numpy installed on you machine
	You should had random installed on you machine
	You should had matplotlib installed on you machine




How to run the project：
	Put election_clean.csv, fandango_score_comparison.csv and .ipynb files into the same directory, 
	open .ipynb files and click Run All
	



Objectives of the project：
	Exercise the skills of using the six modules of sklearn.




Description of files contents:
	ID3Tree_Sklearn: contains a tree classifier that trains and predicts the target values from the decision tree created by Sklearn.
	RandomForest_Sklearn: contains a RandomForestClassifier that trains and predicts the target values through a random forest created by Sklearn. And the number of trees in the forest is modified to find the best prediction.
	treeRegression_Sklearn: contains a decision treee regressor that trains and predicts the target values from the decision tree created by Sklearn. And K-Fold allows the evaluation results to be as close as possible to the performance of the model on the test set.
	LinearRegression_Sklearn： contains information on how to use sklearn's linear regressor to predict the target trend and to plot the trend as a line, curve, and plane via plt

	
	
Sources that provide help:

	1. https://towardsdatascience.com/normal-equation-in-python-the-closed-form-solution-for-linear-regression-13df33f9ad71
	2. https://pythonnumericalmethods.berkeley.edu/notebooks/chapter12.01-2D-Plotting.html    
	3. https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html