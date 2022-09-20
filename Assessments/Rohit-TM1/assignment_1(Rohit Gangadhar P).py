# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

# Basic Python
"""

s = "Hi there Sam!"

a=s.split()
print(a)

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

txt="The diameter of {} is {} kilometers"
print(txt.format(planet,diameter))

"""## 3. In this nest dictionary grab the word "hello"

## 1. Split this string
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

"""# Numpy"""

import numpy as np

d['k1'][3]['tricky'][3]['target'][3]

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

array=np.zeros(10)
print(array)

array=np.ones(10)
print(array)

"""## 5. Create an array of all the even integers from 20 to 35"""

array=np.arange(20,36,2)
print(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

x=np.arange(0,9).reshape(3,3)
print(x)

"""## 7. Concatenate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

from numpy.matrixlib.defmatrix import concatenate
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate((a,b),axis=0))

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

df=pd.DataFrame([['Ravi',24],['Raju',25],['Rahul',23]])
df

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

date=pd.date_range(start='01-01-2023',end='02-02-2023',freq='24H')
for i in date:
  print(i)

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

pd.DataFrame(lists)