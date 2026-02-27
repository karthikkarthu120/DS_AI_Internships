#pandas series
import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Series 1:", s1)
print("Series 2:", s2)
    
#indexing and selection in series
marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])
print(marks['Math'])
print(marks[['Math', 'Chemistry']])

#operations on series
scores = pd.Series([45, 67, 89, 34, 90])
passed = scores[scores > 60]
print(passed)

#handling missing values
data = pd.Series([10, None, 30, None])
print(data.isnull())
print(data.fillna(15))

#string operations on series 
names = pd.Series(['Alice', 'bob', 'CHARLIE'])
res = names.str.upper()
print(res)
print(res.str.contains('A'))





















