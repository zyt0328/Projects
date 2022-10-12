

Author: Yingtao Zhang
VNumber: V00943483
Project name: SimplexMethod solver
Project creation date: 2022/07/03



Prerequisites:
	
	You should had Python3 installed on you machine
	You should had numpy installed on you machine




Running the tests:
	
	The project taking file input via standard input
	i.e.  
	$ python3 SimplexMethod.py < FileName.txt




Description of the solver architecture:

	1. This project starts by reading the data from the standard input line by line in the main()	.
	
	2. Create a new LP object from the read data with create_LP(). 

	3. Create a tabular form for the LP object using get_tabular_form()

	4. If the tabular is initially feasible, put the tabular into optimize() for calculation. 
	   Otherwise, use the big M method to initialize the tabular and put it into optimize() for computation.
		4.1 The big M Method guarantees that any LP can be optimize(), 
		    but LP is feasible only if the optimal solution exists and big Ms does not appear in the tabular's basis.

	5. The Simplex Method pivots are performed in optimize(), and the largest coefficient rule is used.




Extra Features:

	1. Alternate Cycling Avoidance Implemented: lexicographic method is used in the selection of leaving variables. 4 cycling case input has provided in the folder. (cycling1.txt cycling2.txt cycling3.txt cycling4.txt)
	
	Use following command to run the test cases:
	$ python3 Simplexmethod.py < cycling1.txt
	



Some Important Explanations!!! :
	
	For some very large data, this SimplexMethod solver may take more time to perform calculations, so please be patient!
	
	Results of remote testing at linux.csc.uvic.ca：
		netlib_share1b.txt took 100 sec
		netlib_klein2.txt took 90 sec
		netlib_scagr7.txt took 30 sec
		netlib_stocfor1.txt took 15 sec
			
		other test file normally finished in 5 sec!

	
	

Sources that provide help:

	1. Tabular form/equation form
		https://www.youtube.com/watch?v=FY97HLnstVw
	2. Numpy 
		https://www.youtube.com/watch?v=XnDuD_By0hA&list=PLV5qT67glKSHqns6dZwm79pxIzpdYR9K0&index=5
	3. Lexicographic method
		https://www.youtube.com/watch?v=aqBHq2X_Iao
	4. Big M Method
		https://www.youtube.com/watch?v=aM4zlwr12S8
	
