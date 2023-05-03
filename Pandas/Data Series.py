#============================================================================================
>>Formate:
1.Question
2.Input
3.Output
4.Hints
5.Solution
#============================================================================================

#------------------------------------------------------------#
Question-1:
Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

input:
[10,20,30,40,50,60,70,80,90,100]

output:
0     10
1     20
2     30
3     40
4     50
5     60
6     70
7     80
8     90
9    100
dtype: int64

Solution:
import pandas as pd

data_sets=[10,20,30,40,50,60,70,80,90,100]
ds = pd.Series(data_sets)
print(ds)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-2:
Write a Pandas program to convert a Panda module Series to Python list and it's type.

input:
[5,10,15,20,25,30]

output:
0     5
1    10
2    15
3    20
4    25
5    30
dtype: int64

Solution:
import pandas as pd

ds = pd.Series([5,10,15,20,25,30])
print(ds)
print(type(ds))

print("Convert pandas Series to python list: ")
lst=ds.tolist()
print(lst)
print(type(lst))

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

input:
data_set1=[1,2,3,4,5]
data_set2=[6,7,8,9,10]

output:
Add two data sereis:
 0     7
1     9
2    11
3    13
4    15
dtype: int64

Subtraction two DS:
0   -5
1   -5
2   -5
3   -5
4   -5
dtype: int64

Multiplication of DS;
0     6
1    14
2    24
3    36
4    50
dtype: int64

Division of two data series:
 0    6
1    3
2    2
3    2
4    2
dtype: int64

Solution:
import pandas as pd 

data_set1=[1,2,3,4,5]
data_set2=[6,7,8,9,10]

ds1=pd.Series(data_set1)
ds2=pd.Series(data_set2)
print("Add two data sereis:\n",ds1+ds2)
print("Subtraction two DS:\n",ds1-ds2)
print("Multiplication of DS;\n",ds1*ds2)
print("Division of two data series:\n",ds2//ds1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Write a Pandas program to compare the elements of the two Pandas Series.

input:
data1=[1,2,3,4,5]
data2=[1,2,3,6,9]


output:
compaire Two data series:


Equal data:
0     True
1     True
2     True
3    False
4    False
dtype: bool

DS1 Greater than DS2
0    False
1    False
2    False
3    False
4    False
dtype: bool

DS2 is greate then DS2
0    False
1    False
2    False
3     True
4     True
dtype: bool

Solution:
import pandas as pd 

data1=[1,2,3,4,5]
data2=[1,2,3,6,9]

ds1=pd.Series(data1)
ds2=pd.Series(data2)
print("compaire Two data series:\n")

print("\nEqual data:")
print(ds1==ds2)

print("\nDS1 Greater than DS2")
print(ds1>ds2)

print("\nDS2 is greate then DS2")
print(ds1<ds2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Write a Pandas program to convert a dictionary to a Pandas series

input:
dict_data={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

output:
a    100
b    200
c    300
d    400
e    800
dtype: int64


Solution:
import pandas as pd

dict_data={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
pds = pd.Series(dict_data)
print(pds)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Write a Pandas program to convert a NumPy array to a Pandas series.

input:
[10,20,30,40,50,60,70,80,90]

output:
[10 20 30 40 50 60 70 80 90]
<class 'numpy.ndarray'>

Convert numpy array to pandas data series:
0    10
1    20
2    30
3    40
4    50
5    60
6    70
7    80
8    90
dtype: int32
<class 'pandas.core.series.Series'>


Solution:
import pandas as pd
import numpy as ny

ny_arry=ny.array([10,20,30,40,50,60,70,80,90])
print(ny_arry)
print(type(ny_arry))

print("Convert numpy array to pandas data series:")
ds  = pd.Series(ny_arry)
print(ds)
print(type(ds))


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Write a Pandas program to convert a given Series to an array.

input:
[100,200,'Python',300.12,400]

output:
0       100
1       200
2    Python
3    300.12
4       400
dtype: object
<class 'pandas.core.series.Series'>

[100 200 'Python' 300.12 400]
<class 'numpy.ndarray'>


Solution:
import pandas as pd
import numpy as ny

ds = pd.Series([100,200,'Python',300.12,400])
print(ds)
print(type(ds))

arr = ny.array(ds)
print(arr)
print(type(arr))

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-11:
Write a Pandas program to sort a given Series.

input:
data=['100', '200', 'python', '300.12', '400']

output:
Orignal values: 
0       100
1       200
2    python
3    300.12
4       400
dtype: object

After shorting data: 
0       100
1       200
3    300.12
4       400
2    python
dtype: object


Solution:
import pandas as pd

data=['100', '200', 'python', '300.12', '400']
ds = pd.Series(data)
print("Orignal values: ")
print(ds)

print("After shorting data: ")
ds1=pd.Series(data).sort_values()
print(ds1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-12:
Write a Pandas program to add some data to an existing Series.

input:
[1,2,3,4,5]

output:
0    1
1    2
2    3
3    4
4    5
dtype: int64
0     1
1     2
2     3
3     4
4     5
5    10
6    20
dtype: int64

Solution:
import pandas as pd

ds = pd.Series([1,2,3,4,5])
print(ds)

ds1 = pd.concat([ds,pd.Series([10,20])],ignore_index=True)
print(ds1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-13:
Write a Pandas program to create a subset of a given series based on value and condition.

input:
[1,2,3,4,5,6,7,8,9,10]

output:
Original data: 
0     1
1     2
2     3
3     4
4     5
5     6
6     7
7     8
8     9
9    10
dtype: int64
subset data: 
5     6
6     7
7     8
8     9
9    10
dtype: int64

Solution:
import pandas as pd 

ds = pd.Series([1,2,3,4,5,6,7,8,9,10])
print("Original data: ")
print(ds)

print("subset data: ")
res=ds[ds>5]
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-14:
Write a Pandas program to change the order of index of a given series.

input:
[10,0,30,40,50]

output:
A    10
B     0
C    30
D    40
E    50
dtype: int64

Change index position: 
B     0
A    10
C    30
D    40
E    50
dtype: int64

Solution:
import pandas as pd

ds = pd.Series([10,0,30,40,50],index=['A','B','C','D','E'])
print(ds)

print("Change index position: ")
ds1 = ds.reindex(index=['B','A','C','D','E'])
print(ds1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-15:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-16:
Write a Pandas program to get the items of a given series not present in another given series.

input:
[1,2,3,4,5,6]
[4,5,6,7,8,9]

output:
Original data: 
0    1
1    2
2    3
3    4
4    5
5    6
dtype: int64
0    4
1    5
2    6
3    7
4    8
5    9
dtype: int64
data series1 val not present in data series2:
0    1
1    2
2    3
dtype: int64

Solution:
import pandas as pd 
dsr1=pd.Series([1,2,3,4,5,6])
dsr2=pd.Series([4,5,6,7,8,9])
print("Original data: ")
print(dsr1)
print(dsr2)

print("data series1 val not present in data series2:")
res=dsr1[~dsr1.isin(dsr2)]
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-17:
Write a Pandas program to get the items which are not common of two given series.

input:
[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
output:
oringal data sets
0    1
1    2
2    3
3    4
4    5
dtype: int64
0     2
1     4
2     6
3     8
4    10
dtype: int64
Not common Series in both: 
0     1
2     3
4     5
2     6
3     8
4    10
dtype: int64

Solution:
import pandas as pd

dsr1 = pd.Series([1, 2, 3, 4, 5])
dsr2 = pd.Series([2, 4, 6, 8, 10])

print("oringal data sets")
print(dsr1)
print(dsr2)

print("Not common Series in both: ")
dsr11=dsr1[~dsr1.isin(dsr2)]
dsr12=dsr2[~dsr2.isin(dsr1)]

res=pd.concat([dsr11,dsr12])
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-18:


input:


output:


Solution:

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-19:
Write a Pandas program to calculate the frequency counts of each unique value of a given series.

input:
[1,2,5,2,1,2,3,6,3,2,1,4,5,6,3,2,1,4,5,2,1,3,6,5,4]

output:
Original data:
0     1
1     2
2     5
3     2
4     1
5     2
6     3
7     6
8     3
9     2
10    1
11    4
12    5
13    6
14    3
15    2
16    1
17    4
18    5
19    2
20    1
21    3
22    6
23    5
24    4

dtype: int64
2    6
1    5
5    4
3    4
6    3
4    3
Name: count, dtype: int64


Solution:
import pandas as pd
import numpy as ny

ds = pd.Series([1,2,5,2,1,2,3,6,3,2,1,4,5,6,3,2,1,4,5,2,1,3,6,5,4])
print("Orinal data:")
print(ds)

res=ds.value_counts()
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-20:


input:


output:

Solution:



#------------------------------------------------------------#


#------------------------------------------------------------#
Question-21:
Write a Pandas program to find the positions of numbers that are multiples of 5 of agiven series. 

input:
[1,2,3,4,5,6,7,8,9,10]

output:
Data Series: 
0     1
1     2
2     3
3     4
4     5
5     6
6     7
7     8
8     9
9    10
dtype: int64
Numbers that are multipley of 5

(array([4, 9], dtype=int64),)

Solution:
import pandas as pd 
import numpy as ny

ds1=pd.Series([1,2,3,4,5,6,7,8,9,10])
print("Data Series: ")
print(ds1)

print("Numbers that are multipley of 5")
res=ny.where(ds1%5==0)
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-22:
Write a Pandas program to extract items at given positions of a given series.

input:
list="1234567899874563211258963258741258896"

output:
Original data sete: 
0     1
1     2
2     3
3     4
4     5
5     6
6     7
7     8
8     9
9     9
10    8
11    7
12    4
13    5
14    6
15    3
16    2
17    1
18    1
19    2
20    5
21    8
22    9
23    6
24    3
25    2
26    5
27    8
28    7
29    4
30    1
31    2
32    5
33    8
34    8
35    9
36    6
dtype: object
Extract items at given position: 
0     1
2     3
6     7
11    7
21    8
dtype: object

Solution:
import pandas as pd


ds = pd.Series(list("1234567899874563211258963258741258896"))
print("Original data sete: ")
print(ds)

print("Extract items at given position: ")
ele_poss=[0,2,6,11,21]
res=ds.take(ele_poss)
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-23:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-24:
Write a Pandas program convert the first and last character of each word to upper case in each word of a given series.

input:
["php","Python",'java','django','pandas','numpy']

output:
Oringal data sets: 
0       php
1    Python
2      java
3    django
4    pandas
5     numpy
dtype: object

After changing data:
0       PhP
1    PythoN
2      JavA
3    DjangO
4    PandaS
5     NumpY
dtype: object

Solution:
import pandas as pd

ds1=pd.Series(["php","Python",'java','django','pandas','numpy'])
print("Oringal data sets: ")
print(ds1)

res=ds1.map(lambda x:x[0].upper()+x[1:-1]+x[-1].upper())
print("After changing data:")
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-25:
Write a Pandas program to calculate the number of characters in each word in a givenseries.

input:
['python','java','django','php']

output:
0    python
1      java
2    django
3       php
dtype: object
0    6
1    4
2    6
3    3
dtype: int64

Solution:
import pandas as pd

ds1=pd.Series(['python','java','django','php'])
print(ds1)

res=ds1.map(lambda x: len(x))
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-26:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-27:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-28:


input:


output:


Solution:


#------------------------------------------------------------#



#------------------------------------------------------------#
Question-29:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-30:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-31:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-32:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-33:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-34:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-35:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-36:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-37:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-38:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-39:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-40:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-41:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-42:


input:


output:


Solution:


#------------------------------------------------------------#
