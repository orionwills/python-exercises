#!/usr/bin/env python
# coding: utf-8

# In[240]:
# 4.7 numpy_exercises


# get_ipython().run_line_magic('matplotlib', 'notebook')
import numpy as np
import math
from functools import reduce
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')


# In[95]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# ### How many negative numbers are there?

# In[14]:


a[a < 0].shape[0]


# ### How many positive numbers are there?

# In[15]:


a[a > 0].shape[0]


# ### How many even positive numbers are there?

# In[99]:


a[(a > 0) & (a % 2 == 0)].shape[0]


# ### If you were to add 3 to each data point, how many positive numbers would there be?

# In[33]:


# a[(a + 3) & (a > 0)]
b = a + 3
b[b > 0].shape[0]


# ### If you squared each number, what would the new mean and standard deviation be?

# In[71]:


b = (a ** 2).mean()
print(b)
c = (a ** 2).std()
print(c)


# ### A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

# In[66]:


b = a - a.mean()
b


# Calculate the z-score for each data point. Recall that the z-score is given by:
# z = x - mean / std

# In[67]:


b = (a - a.mean()) / a.std()
b


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
#
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
#
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
#
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
#
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
#
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
#
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
#
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# In[227]:


aa = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
aaa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[236]:


sum_of_aa = aa.sum()
print(f'numpy sum = {sum_of_aa}')

sum_of_aaa = sum(aaa)
print(f'python list comp sum = {sum_of_aaa}')


# In[147]:


min_of_aa = aa.min()
print(f'numpy min = {min_of_aa}')

min_of_aaa = min(aaa)
print(f'python min = {min_of_aaa}')


# In[146]:


max_of_aa = aa.max()
print(f'numpy max = {max_of_aa}')

max_of_aaa = max(aaa)
print(f'python max = {max_of_aaa}')


# In[144]:


mean_of_aa = aa.mean()
print(f'numpy mean = {aa.mean()}')

mean_of_aaa = sum(aaa) / len(aaa)
print(f'python mean = {mean_of_aaa}')


# In[142]:


product_of_aa = aa.prod()
print(f'numpy product = {product_of_aa}')

product_of_aaa = reduce((lambda x, y: x * y), aaa)
print(f'python reduce product = {reduce((lambda x, y: x * y), aaa)}')


# In[158]:


squares_of_aa = np.square(aa)
print(f'numpy squares = {squares_of_aa}')

squares_of_aaa = [i ** 2 for i in aaa]
print(f'python list comp squares = {[i ** 2 for i in aaa]}')


# In[164]:


odds_in_aa = aa[aa % 2 == 1]
print(f'numpy odds = {odds_in_aa}')

odds_in_aaa = [i for i in aaa if i % 2 == 1]
print(f'python list comp odds = {[i for i in aaa if i % 2 == 1]}')


# In[166]:


evens_in_aa = aa[aa % 2 == 0]
print(f'numpy evens = {evens_in_aa}')

evens_in_aaa = [i for i in aaa if i % 2 == 0]
print(f'python list comp evens {[i for i in aaa if i % 2 == 0]}')


# What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
#
# Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
#
# b = [
#
#     [3, 4, 5],
#     [6, 7, 8]
#
# ]
#

# In[205]:


bb = np.array([[3, 4, 5], [6, 7, 8]])


# In[173]:


bb_sum = bb.sum()
bb_min = bb.min()
bb_max = bb.max()
bb_mean = bb.mean()
bb_prod = bb.prod()
bb_square = np.square(bb)
print(f'sum = {bb_sum}')
print(f'min = {bb_min}')
print(f'max = {bb_max}')
print(f'mean = {bb_mean}')
print(f'prod = {bb_prod}')
print(f'square = {bb_square}')


# Exercise 9 - print out the shape of the array b.
#
# Exercise 10 - transpose the array b.
#
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
#
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# In[237]:


bb.shape[0]


# In[181]:


np.transpose(bb)


# In[208]:


# np.concatenate(bb)
bb = bb.flatten()


# In[192]:


np.asarray(bb)


# In[213]:


bb = np.reshape(bb, (6, 1))


# In[214]:


bb


# In[253]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# Exercise 1 - Find the min, max, sum, and product of c.
#
# Exercise 2 - Determine the standard deviation of c.
#
# Exercise 3 - Determine the variance of c.
#
# Exercise 4 - Print out the shape of the array c
#
# Exercise 5 - Transpose c and print out transposed result.
#
# Exercise 6 - Multiply c by the c-Transposed and print the result.
#
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
#
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

# In[243]:


print(f'numpy min = {c.min()}')
print(f'numpy max = {c.max()}')
print(f'numpy sum = {c.sum()}')
print(f'numpy prod = {c.prod()}')


# In[226]:


print(f'numpy std = {c.std()}')
print(f'numpy variance = {c.var()}')
print(f'numpy shape = {c.shape}')
print(f'numpy transpose = {c.transpose()}')
print(f'numpy c * c.transpose = {c * c.transpose()}')
print(f'numpy sum of c*c.trans = {(c * c.transpose()).sum()}')
print(f'numpy prod of c*c.trans = {(c.prod() * c.transpose())}')


# In[256]:


dd = np.array(
    [[90, 30, 45, 0, 120, 180],
     [45, -90, -30, 270, 90, 0],
     [60, 45, -45, 90, -45, 180]]
)


# In[264]:


sine_dd = np.sin(dd)
print(f'sin(dd) = \n{sine_dd}')


# In[265]:


cos_dd = np.cos(dd)
print(f'cos(dd) = \n{cos_dd}')


# In[266]:


tan_dd = np.tan(dd)
print(f'cos(dd) = \n{tan_dd}')


# In[280]:


neg_dd = dd[dd < 0]
print(f'negative(dd) = \n{neg_dd}')


# In[281]:


pos_dd = dd[dd > 0]
print(f'positive(dd) = \n{pos_dd}')


# In[282]:


unique_array_dd = np.unique(dd)
print(f'unique array(dd) =\n{unique_array_dd}')


# In[284]:


unique_count = len(np.unique(dd))
print(f'unique count(dd) = {unique_count}')


# In[296]:


print(f'dd.shape = {dd.shape}')


# In[300]:


trans_dd = dd.transpose()
print(f'trans shape(dd) = \n{trans_dd}')


# In[303]:


reshape9x2 = np.reshape(dd, (9, 2))
print(f'reshaped 9x2 = \n{reshape9x2}')


# In[ ]:
