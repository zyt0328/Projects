'''
Author: Yingtao Zhang
VNumber: V00943483
Project name: SimplexMethod solver
Project creation date: 2022/07/03
Last modification date： 2022/07/15
'''

import sys
import numpy as np

class LP:
    def __init__(self, ObjF =np.empty([0,0],dtype = float), constrains = np.empty([0,0],dtype = float), constrains_vals = np.empty([0,0],dtype = float), optimization_variables_values = np.empty([0,0],dtype = float)):
        self.ObjF = ObjF;
        self.constrains = constrains;
        self.constrains_vals = constrains_vals;
        self.optimalValue = 0.0;
        self.optimization_variables_values = optimization_variables_values;
        self.feasible = True;
        self.bounded = True;
        self.optimal = False;
    
    #Return the string representation of this LP solution
    def __str__(self):
        if self.feasible != True:
            return("infeasible")
        elif self.bounded != True:
            return("unbounded")
        else:
            return_optimization_variables_values = ""
            for i in self.optimization_variables_values:
                return_optimization_variables_values += "{string:.7g}".format(string = i)+' '
            return_optimization_variables_values = return_optimization_variables_values.rstrip()
            return("optimal\n{optimalValue:.7g}\n{optimization_variables_values}".format
                   (optimalValue = self.optimalValue,optimization_variables_values = return_optimization_variables_values))
    
    
    #Return the string representation of this LP solution               
    def __repr__(self):
        if self.feasible != True:
            return("infeasible")
        elif self.bounded != True:
            return("unbounded")
        else:
            return_optimization_variables_values = ""
            for i in self.optimization_variables_values:
                return_optimization_variables_values += "{string:.7g}".format(string = i)+' '
            return_optimization_variables_values = return_optimization_variables_values.rstrip()
            return("optimal\n{optimalValue:.7g}\n{optimization_variables_values}".format
                   (optimalValue = self.optimalValue,optimization_variables_values = return_optimization_variables_values))
        
    
    #Setters
    def setObjF(self, ObjF):
        self.ObjF = ObjF

    def setConstrains(self, constrains):
        self.constrains = constrains
    
    def set_constrains_values(self, constrains_vals):
        self.constrains_vals = constrains_vals
    
    def set_optimization_variables_values(self, optimization_variables_values):
        self.optimization_variables_values = optimization_variables_values
    
    
    
    '''
    Funtion : get_tabular_form()
    Description : Put objective funton, constrains, and constrains_values into a float[][], turn LP into tabular form.
    Calls : None
    Called by : initialize()
    Input : None
    Output : None
    Return : np.array float[][] --- LP in tabular form
    Others : Since I implement the method before the lecture, so I will continue call it tabular form instead of equational form.
    '''
    def get_tabular_form(self):
        length_n = len(self.constrains_vals)
        
        slack_variables = np.zeros(length_n, dtype = float)
        slack_table = np.identity(length_n, dtype = float)
        optimal_val = np.zeros(1, dtype = float)
        
        values = np.hstack((optimal_val, self.constrains_vals))
        values = values.reshape((len(values),1))
        
        constrains_funtion = np.hstack((self.constrains, slack_table))
        tabular = np.hstack((-self.ObjF, slack_variables))
        
        tabular = np.vstack((tabular, constrains_funtion))
        
        tabular = np.hstack((tabular, values))
        
        return tabular
    
    
    '''
    Funtion : optimize()
    Description : Solve the LP, optimaize the value of LP
    Calls : min_index()
    Called by : main()
    Input : np.array float[][] ---feasible LP in tabular form
    Output : None
    Return : None
    Others : The pivot rule is largest coeffcient rule, and Big M Method are used for find feasible region.
    '''    
    def optimize(self, tabular):
        
        # A small number used to eliminate the rounding error
        eps = 0.000000001
        
        
        #pivot step
        while(self.optimal == False):
            # Eliminate the rounding error
            for i in range(len(tabular)):
                for j in range(len(tabular[i])):
                    if tabular[i,j] > 0:
                        if tabular[i,j] < eps:
                            tabular[i,j] = 0
                    if tabular[i,j] < 0:
                        if tabular[i,j] > -eps :
                            tabular[i,j] = 0
                     
            #check if the LP optimal
            for i in tabular[0,:-1]:
                if i < 0:
                    self.optimal = False
                    break
                self.optimal = True
            if self.optimal == True:
                break
            
            
            #find the largest coefficient to be the entering variable
            #I am using the largest coefficient rule to solve LP
            minimal_val = float('inf')
            entering_index = -1
            for i in range(len(tabular[0])-1):
                if tabular[0,i] < minimal_val:
                    minimal_val = tabular[0,i]
                    entering_index = i
            
            
            #find the leaving variables, put them into a list, ready for next operation.
            leaving_list = [float('inf')]*len(tabular)
            for i in range(1,len(tabular)):
                if tabular[i,entering_index] <= 0:
                    pass
                elif tabular[i,-1] == 0:
                    leaving_list[i] = 0
                elif tabular[i,-1] < 0:
                    self.feasible = False
                    return
                else:
                    leaving_list[i] = tabular[i,-1]/tabular[i,entering_index]
            leaving_list = min_index(leaving_list)
            
            #check the unboundedness
            if leaving_list[0] == float('inf'):
                self.bounded = False
                return
            
            #Two or more chooice for leaving variable
            leaving_index = -1
            if len(leaving_list) != 1:
                #Picking leaving variable using lexicographic method
                #The leaving list above that contains the leaving variables which have the the tightest bond
                
                #In order to use lexicographic method we need to unsure that all rows that we are comparing are lexicographically positive
                #Lexicographically positive : 
                #The first element of the row has to be positive
                #In this case, the value row is the first comparison element of the row, because tabular is feasible, all rows are lexicographically positive
                
                #Whenever there are two or more possible leaving variables, select lexicographically smaller row
                #Lexicographically smaller : 
                #Rows with smaller elements appear first is lexicographically smaller
                #i.e. (1, 5, 2, 4) (1, 1, 100, 100). We pick (1, 1, 100, 100), because it is lexicographically smaller
                
                
                for coloum_index in range(len(tabular[0])-1):
                    comparing_list = []
                    for i in range(len(leaving_list)):
                        if tabular[leaving_list[i],coloum_index] != 0:
                            comparing_list.append(tabular[leaving_list[i],coloum_index]/tabular[leaving_list[i],entering_index])
                        else:
                            comparing_list.append(0)
                    min_list = min_index(comparing_list)
                    
                    if len(min_list) == 1:
                        leaving_index = leaving_list[min_list[0]]
                        break
                    else:
                        pass
                leaving_index = leaving_list[min_list[0]] 
                        
            #Exactly one choise for leaving variable
            else:
                leaving_index = leaving_list[0]
            
        
           
            #Now we have one entering variable and one leaving variable
            #Modify all rows by doing row operations.
            divider = tabular[leaving_index,entering_index]
            tabular[leaving_index] = tabular[leaving_index]/divider
            for i in range(len(tabular)):
                if i == leaving_index:
                    pass
                else:
                    if (tabular[i,entering_index] and tabular[leaving_index,entering_index]) != 0.0:
                        multiplier = tabular[i,entering_index]/tabular[leaving_index,entering_index]
                        tabular[i] = -multiplier*tabular[leaving_index]+tabular[i]
                    else:
                        pass

        
        #Get the values of the initial optimization variable values 
        optimization_variables_values = []
        for i in range(len(self.ObjF)+len(tabular)-1,len(tabular[0])-1):
            if tabular[0,i] == 0:
                count = 0
                for j in range(len(tabular)):
                    if tabular[j,i] == 1 and tabular[j,-1] != 0:
                        count += 1
                if count == 1:
                    self.feasible = False
                    return
        for i in range(len(self.ObjF)):
            if tabular[0,i] == 0:
                temp = []
                for n in range(len(tabular)):
                    if tabular[n,i] == 1:
                        temp.append(n)
                if len(temp) == 1:
                    optimization_variables_values.append(tabular[temp[0],-1])
                else:
                    optimization_variables_values.append(0.0)
            else:
                optimization_variables_values.append(0.0)
        
        self.set_optimization_variables_values(np.array(optimization_variables_values))        
        self.optimalValue = tabular[0,-1]
    
    
    
    '''
    Funtion : big_omega()
    Description : Set up artifitial variable big Omega put it into basis
    Calls : None
    Called by : initialize()
    Input : np.array float[][] --- infeasible LP in tabular form
    Output : None
    Return : np.array float[][] --- LP in tabular form with aritifitial variable big Omega in the basis
    Others : None
    '''
    def big_omega(self, tabular):
        #Set big Omega row 
        big_omega_col = np.ones(len(tabular), dtype = float)
        big_omega_col[0] = -1
        
        
        #Put big Omega row into tabular
        tabular = np.insert(tabular, -1, big_omega_col, axis=1)
        

        #Find the min value index as leaving index 
        minimal_val = float('inf')
        min_index = -1
        for i in range(1, len(tabular)):
            if minimal_val > tabular[i,-1]:
                minimal_val = tabular[i,-1]
                min_index = i
            else:
                pass
        
        
        #Pivot step put big Omega into basis
        for i in range(len(tabular)):
            divider = tabular[min_index,-2]
            tabular[min_index] = tabular[min_index]/divider
            for i in range(len(tabular)):
                if i == min_index:
                    pass
                else:
                    if (tabular[i,-2] and tabular[min_index,-2]) != 0.0:
                        multiplier = tabular[i,-2]/tabular[min_index,-2]
                        tabular[i] = -multiplier*tabular[min_index]+tabular[i]
                    else:
                        pass
        tabular[min_index] = -tabular[min_index]   
        return tabular

    
    
    '''
    Funtion : auxiliary()
    Description : Check if there is a feasible solution to the LP problem
    Calls : min_index()
    Called by : intialize()
    Input : np.array float[][] --- LP in tabular form with artifitial variable big Omega in the basis
    Output : None
    Return : np.array float[][] --- LP in tabular form ready for bring optimazation variable back
    Others : Although the big M method does not fall into a loop, adding too many big M variables will continue the pivot step almost
    infinitely, so when we encounter the problem of feasibility only, we switch to the auxiliary method to shorten the time to find a 
    feasible region by adding only one artificial variable.
    '''
    def auxiliary(self, tabular):
        
        # A small number used to eliminate the rounding error
        eps = 0.00000001
        
        
        #pivot step
        while(tabular[0,-2] != -1 or tabular[0,-1] != 0):
            # Eliminate the rounding error
            for i in range(len(tabular)):
                for j in range(len(tabular[i])):
                    if tabular[i,j] > 0:
                        if tabular[i,j] < eps:
                            tabular[i,j] = 0
                    if tabular[i,j] < 0:
                        if tabular[i,j] > -eps :
                            tabular[i,j] = 0
                     
            #check if the auxiliary problem should end
            if tabular[0,-1] > 0:
                return
            
            #check if the Auxiliary dictionary optimal
            for i in tabular[0,:-1]:
                if i < 0:
                    self.optimal = False
                    break
                self.optimal = True
            if self.optimal == True:
                break
            
            
            #find the largest coefficient to be the entering variable
            #I am using the largest coefficient rule to solve LP
            minimal_val = float('inf')
            entering_index = -1
            for i in range(len(tabular[0])-1):
                if tabular[0,i] < minimal_val:
                    minimal_val = tabular[0,i]
                    entering_index = i
            
            
            #find the leaving variables, put them into a list, ready for next operation.
            leaving_list = [float('inf')]*len(tabular)
            for i in range(1,len(tabular)):
                if tabular[i,entering_index] <= 0:
                    pass
                elif tabular[i,-1] == 0:
                    leaving_list[i] = 0
                elif tabular[i,-1] < 0:
                    self.feasible = False
                    return
                else:
                    leaving_list[i] = tabular[i,-1]/tabular[i,entering_index]
            leaving_list = min_index(leaving_list)
            
            
            #check the unboundedness
            if leaving_list[0] == float('inf'):
                self.feasible = False
                self.bounded = False
                return
            
            #Two or more chooice for leaving variable
            leaving_index = -1
            if len(leaving_list) != 1:
                #picking leaving variable using lexicographic method
                for coloum_index in range(len(tabular[0])-1):
                    comparing_list = []
                    for i in range(len(leaving_list)):
                        if tabular[leaving_list[i],coloum_index] != 0:
                            comparing_list.append(tabular[leaving_list[i],coloum_index]/tabular[leaving_list[i],entering_index])
                        else:
                            comparing_list.append(0)
                    min_list = min_index(comparing_list)
                    if len(min_list) == 1:
                        leaving_index = leaving_list[min_list[0]]
                        break
                    else:
                        pass
                leaving_index = leaving_list[min_list[0]]
            #Exactly one choise for leaving variable
            else:
                leaving_index = leaving_list[0]

            
            #Now we have one entering variable and one leaving variable
            #Modify all rows by doing row operations.
            divider = tabular[leaving_index,entering_index]
            tabular[leaving_index] = tabular[leaving_index]/divider
            for i in range(len(tabular)):
                if i == leaving_index:
                    pass
                else:
                    if (tabular[i,entering_index] and tabular[leaving_index,entering_index]) != 0.0:
                        multiplier = tabular[i,entering_index]/tabular[leaving_index,entering_index]
                        tabular[i] = -multiplier*tabular[leaving_index]+tabular[i]
                    else:
                        pass
        
        if tabular[0,-2] == -1 and tabular[0,-1] == 0:
            return tabular
        else:
            self.feasible = False
            return
    
    '''
    Funtion : initialize()
    Description : Use Big M method find a feasible region for LP
    Calls : get_tabualr_form()
    Called by : main()
    Input :  None
    Output : None
    Return : np.array float[][] ---contains feasible LP in tabular form
    Others : Return the tabular if it is origionally feasible. Otherwise reconstruct the tabular, return the new tabular which 
    contain Big Ms.
    '''
    def initialize(self):
        #Set print format only for debug
        np.set_printoptions(formatter = {'float':'{:.3f}'.format})
        #Auxiliary approch only for feasibility only problem
        if (self.ObjF == 0).all() and (self.constrains_vals < 0).any():
            tabular = self.get_tabular_form()
            tabular = self.big_omega(tabular)
            tabular = self.auxiliary(tabular)
            
            if self.feasible == False:
                return
            
        
        #Get the tabular form
        tabular = self.get_tabular_form()
        

        
        #check initial tabular feasible or unfeasible
        for i in range(1,len(tabular)):
            if tabular[i,-1] < 0:
                self.feasible = False
            else:
                pass
        
        
        #Initial tabular feasible, go optimize!
        if self.feasible == True:
            return tabular
        
        
        #Slice the tabular into parts, ready for reconstruct
        list1 = []
        for i in range(1, len(tabular)):
            if tabular[i,-1] < 0:
                list1.append(i)
                tabular[i] = -tabular[i]
   
        left = tabular[0:len(tabular), 0:len(tabular[0])-1]
        right = tabular[0:len(tabular), -1]
        right = right.reshape(-1,1)
        
        
        #Construct big Ms coloum by coloum, then put them into tabular one by one
        for i in list1:
            z = np.zeros((len(tabular),1), dtype = float)
            z[0,0] = 1000000
            z[i,0] = 1
            left = np.hstack((left,z))
            
        tabular = np.hstack((left,right))
        
        #Initialize the tabular by puting M into basis
        for i in range(len(self.ObjF)+len(tabular)-1,len(tabular[0])):
            for j in range(len(tabular)):
                if tabular[j,i] == 1:
                    tabular[0] = -1000000*tabular[j]+tabular[0]
                
        self.feasible = True
        return tabular
                
    
    
        
def main():
   
    #Initialize the list for Objective funtion, Constrains and constrains value
    ObjF = []
    constrains = []
    constrains_vals = []
    
    
    #Read lines from standard input
    lines = []
    for line in sys.stdin:
        sp = line.split()
        temp = []
        for i in sp:
            temp.append(float(i))
        lines.append(temp)
    
    #Put values into list
    ObjF = lines[0]
    lines = lines[1:len(lines)]
    for i in range(len(lines)):
        constrains_vals.append(lines[i][-1])
        temp = []
        for j in range(len(lines[i])-1):
            temp.append(float(lines[i][j]))
        constrains.append(temp)

    
    lp = creat_LP(ObjF, constrains, constrains_vals)
    tabular = lp.initialize()
    if lp.feasible != False:
        lp.optimize(tabular)
    print(lp)

'''
Funtion :  creat_LP()
Description : Used to create a new LP object
Calls : LP.setObjF() LP.setConstrains() LP.set_constrains_values()
Called by :  main()
Input :  parameter1: float[]   parameter2: float[][]   parameter3: float[] 
Output : None
Return : LP object 
Others : None
'''
def creat_LP(ObjF, constrains, constrains_vals):
    new_lp = LP()
    new_lp.setObjF(np.array(ObjF))
    new_lp.setConstrains(np.array(constrains))
    new_lp.set_constrains_values(np.array(constrains_vals))
    return new_lp



'''
Funtion : min_index()
Description : Find index of the smallest number/numbers.
Calls : None
Called by : optimize()
Input : float[] ---list of float numbers
Output : None
Return : int[] ---list that contain the index of smallest number/numbers inthe input list 
Others : Return float[float('inf')] if all the number in the input list are infinity.
'''    
def min_index(leaving_list):
    index = []
    min_n = min(leaving_list)
    if min_n == float('inf'):
        return [float('inf')]
    for i in range(len(leaving_list)):
        if leaving_list[i] == min_n:
            index.append(i)
    return index


if __name__ == "__main__":
    main()