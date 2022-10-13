Author: Yingtao Zhang
VNumber: V00943483
Project name: Logistic regression
Project creation date: 2022/09/28




Introduction: 
	Logistic regression is one of the most common modelling approaches in the field of machine learning. Logistic regression is very similar to linear regression, except that linear regression is often used to predict a trend, such as what the temperature will be tomorrow. Whereas logistic regression tends to return a yes or no answer, for example, whether it will rain tomorrow. So in essence logistic regression is a classification method.





Prerequisites:
	
	You should had pandas installed on you machine
	You should had numpy installed on you machine
	You should had random installed on you machine
	You should had sklearn installed on you machine





How to run the project：
	Put fandango_score_comparison and logistic_regression.ipynb into the same directory, 
	open logistic_regression.ipynb and click Run All.
	
	



Objectives of the project：
	Use Fandango_Ratingvalue and Fandango_Difference to predict whether the movie will get 3 or more Fandango stars.




Description of the logistic_regression architecture:
	We know that the linear regression method is used to analyze the linear relationship between the independent and dependent variables, which can be expressed in the following form.
	$$ Y = W^{\top} \cdot X + B $$

	1. Use gradient_descent() to find the most suitable W and B.
	
		1.1 Initialize all the values of W and B to 0. The length of W will be the length of X (ensuring that W and X have the same dimension)

		1.2 For each iteration, calculate the values of W and B that make the cost function smaller.

	2. After obtaining the optimal W and B we calculate the target value。
		
		2.1 By using sigmoid function we obtain a discrete set of numbers between 0 and 1.

		2.2 For this set of data greater than 0.5 we predicted it to be 1 and the rest to be 0.

	3. Our accuracy is obtained by comparing the answers with the test data。




	

Sources that provide help:

	1. https://www.youtube.com/watch?v=sDv4f4s2SB8  
	2. https://www.youtube.com/watch?v=U1omz0B9FTw&list=PLuhqtP7jdD8Chy7QIo5U0zzKP8-emLdny&index=1   
	3. https://www.youtube.com/watch?v=ar8mUO3d05w&list=PLuhqtP7jdD8Chy7QIo5U0zzKP8-emLdny&index=2
	4. https://www.youtube.com/watch?v=0VMK18nphpg&list=PLuhqtP7jdD8Chy7QIo5U0zzKP8-emLdny&index=3   
	5. https://www.youtube.com/watch?v=t6MVuMavbBY&list=PLuhqtP7jdD8Chy7QIo5U0zzKP8-emLdny&index=4 
	6. https://www.youtube.com/watch?v=nzNp05AyBM8&list=PLuhqtP7jdD8Chy7QIo5U0zzKP8-emLdny&index=6   
	7. https://github.com/Jaimin09/Coding-Lane-Assets/tree/main/Logistic%20Regression%20in%20Python%20from%20Scratch   
	8. https://zhuanlan.zhihu.com/p/28408516   