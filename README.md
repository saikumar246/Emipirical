# Emipirical
An app that allows the user to enter the percentage constituents of a compound that contains carbon (C), hydrogen (H), and oxygen (O) in order to obtain
the empirical formula of the compound.For example, Aspirin contains 60.0% C, 4.48% H, and 35.5% O. The empirical formula should be found as follows:
Writing a function, named Molar (in the main code) that takes the percentage constituents of the compound (carbon, hydrogen, oxygen) and 
finds the subscripts for each element based on the following algorithm:
Start with the number of grams of each element. Assuming that the total mass is 100 grams so that
the mass of each element = the percent given.
Converting the mass of each element to moles using the molar mass from the periodic table. 
The molar mass of oxygen is 15.994 grams per mole (g/mol), molar mass of Hydrogen= 1.007 g/mol, Molar mass of C is 12.011 g/mol. 
These values should be shown as constants in your code.
In the example above, the ratio of carbon to other elements in the compound, we compute nC as:
nC = perc of carbon (g) * (1 mol of C/ molar mass of C)= 60.0g * (1 mol of C/12.011g) = 4.995 mol of C
Equally, nO = perc of oxygen(g) * (1 mol of O/molar mass of O)= 35.5g*(1 mol of O/15.994) = 2.220 mol of O
nH = perc of hydrogen (g) *(1 mol of H/ molar mass of H)= 4.48g*(1 mol of H/1.007) = 4.449
Divide each mole value by the smallest number of moles calculated. To do that, put the nC, nO, nH in a list and find the minimum value of the list.
nC/nO = 4.995/2.22 = 2.25 mol C/ 1 mol O

nH/nO = 4.449/2.22 = 2.00 mol H/ 1 mol O

Round to the nearest whole number. This is the mole ratio of the elements and is represented by subscripts in the empirical formula. 
In the example above, the compound has C:H:O in approximate ratio of 2:2:1 
(note that this is an imperfect way of arriving at the empirical formula since the fractions [~ 0.25, ~0.5, ~0.75] have been ignored).

Writing other parts of the main program to do the following:
Creating a loop (while loop) to enable the user print out the empirical formulas for three compounds. 
The user is provided with input boxes to enter percentage composition of the compound in terms of its constituent elements (carbon, hydrogen, oxygen). 
The total of all percentages must be 100%. Your code must check to ensure that the total percentage values entered is equal to 100%. Failure to do that would cost you some marks.
Call the function to compute the subscripts for carbon, hydrogen and oxygen.
Print out the formula of the compound (e.g. C2H2O).
Nott: Using the index position of the element’s subscript and concatenation for your print statement. For example, if the function receiving list is 
lst3, and lst3=[1,2,1], then your print should be: print (“C”+str(lst3[0])+….)
When the program is done, it should print: Thanks for using this app!
Sample input:
% Carbon=52.00
% Hydrogen=40.92
% Oxygen=68.54
Output:
Emp. Formula= C2H6O

