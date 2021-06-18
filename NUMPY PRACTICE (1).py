#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Write a NumPy program to get the numpy version and show numpy build configuration.

import numpy as np
print (np.__version__)
print (np.show_config())


# In[9]:


#Write a NumPy program to test whether none of the elements of a given array is zero.

import numpy as np
arr_1 = [4, 2, 1, 8, 0]
arr_2 = [7, 5, 9, 3]
print ("First array:", arr_1)
print ("The array contains 0 as its element:", np.all(arr_1))
print ("Second array:", arr_2)
print ("The array contains 0 as its element:", np.all(arr_2))


# In[10]:


# Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
import numpy as np
arr = [1, 2, np.nan, np.inf, 0]
print ("Given array:", arr)
print ("Finiteness of the array:", np.isfinite(arr))


# In[12]:


#  Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.

import numpy as np
arr_1 = np.array ([1, 2, 3, 4, 0, 100])
arr_2 = np.array ([7, 6, 0, 5, 9, 00.0000001])
print ("Array 1:", arr_1)
print ("Array 2:", arr_2)
print ("Comparison - equal:", np.equal(arr_1, arr_2))
print ("Comparison on the basis of tolerance - equal:", np.allclose(arr_1, arr_2))


# In[13]:


# Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.

import numpy as np
arr_1 = np.zeros(10)
print ("Array of 10 zeros:", arr_1)
arr_2 = np.ones(10)
print ("Array of 10 ones:", arr_2)
arr_3 = np.ones(10) * 5
print ("Array of 10 fives:", arr_3)


# In[15]:


# Write a NumPy program to create a 3x3 identity matrix.
import numpy as np
arr = np.identity(3)
print ("3x3 indentity matrix:")
print (arr)


# In[16]:


# Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

import numpy as np
vector = np.arange(15, 56)
print ("Array in range 15 to 55:")
print (vector)
print ("Array excluding 15 and 55:")
print (vector[1:-1])


# In[17]:


# Write a NumPy program to create an array of the integers from 30 to70. 

import numpy as np
arr = np.arange(30, 71)
print ("Array of integers from 30 to 70:")
print (arr)


# In[ ]:




