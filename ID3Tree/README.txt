Author: Yingtao Zhang
VNumber: V00943483
Project name: ID3Tree
Project creation date: 2022/09/22




Introduction: 
	The ID3 algorithm is a greedy algorithm used to construct decision trees. The rate of decline of information entropy is used as the criterion for selecting test attributes, i.e., the attribute with the highest information gain that has not yet been used for classification at each node is selected as the criterion for classification, and then the process continues until the generated decision tree can perfectly classify the training samples.




Prerequisites:
	
	You should had pandas installed on you machine
	You should had numpy installed on you machine
	You should had random installed on you machine





How to run the project：
	Put election_clean.csv and ID3Tree.ipynb into the same directory, 
	open ID3Tree.ipynb and click Run All
	
	



Description of the ID3Tree architecture:

	1. This project started with importing a csv document using pandas and briefly processing the data in the dataframe as needed. For example, removing unreasonable values, selecting the attributes used to build the decision tree, and selecting the target of the decision tree.
	
	2. Recursively call the decisionTree() to achieve the construction of a decision tree. 

		2.1 In the decisionTree() method, use find_largest_IG() to find the best attribute.

			2.1.1 Use getTotalEntropy() to find the total entropy of the current dataframe。

			2.1.2 For each of the attributes in the current dataframe, use getSplitEntropy() to calculate the entropy.

			2.1.3 Subtract the entropy of each attribute separately from the total entropy, and the attribute with the largest number is the best attribute.

		2.2 Create a branch for each of the attributes in the best feature.

		2.3 By checking the value of the branch and the current depth to decide whether to stop or pass the subframe into the decisionTree() and enter recursion。

	3. Once the decision tree is built use prediciton() to make predictions and check the accuracy of the predictions.	




Extra Features:
	Gini impurity: The calculation using Gini impurity instead of entropy has also been developed, and the calculation will be faster because Gini impurity is simpler.

	



Some Important Explanations!!! :
	In the data used here, COUNTY is not a very good attribute, and his presence poses many problems, mainly because it has numerous non-repeating discrete variables that greatly interfere with the accuracy of the prediction. So please be careful to remove this column of data when testing.
	

	
	

Sources that provide help:

	1. https://www.youtube.com/watch?v=YG_nOa6-6Q8   

	2. https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python