#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')
bank_df = pd.read_csv("data_banknote_authentication.txt", names= ["variance", "skewness", "kurtosis", "Entropy", "class"])


# In[2]:


bank_df.head()


# In[3]:


bank_df.shape


# In[4]:


bank_df.describe()


# In[5]:


import seaborn as sns
sns.pairplot(bank_df, hue='class' , diag_kind= 'kde')


# In[6]:


from scipy.stats import zscore

bank_df_attr = bank_df.loc[:, 'variance':'Entropy']  
bank_df_attr_z = bank_df_attr.apply(zscore)

# A simple function that takes as input a column, find's its median, identifies outliers, replaces outliers with median     
def replace(x):
    median, std = x.median(), x.std()  #Get the median and the standard deviation of every column
    outliers = (x - median).abs() > 2*std # Subtract median from every member of each column. Take absolute values > 2std
    x[outliers] = x.median()       
    return x

bank_df_corrected = bank_df_attr_z.apply(lambda x:x.transform(replace)) # transforming raw data using replace function
bank_df_treated = bank_df_corrected.join(pd.DataFrame(bank_df['class']))  # joining back the numeric and non-numeric columns


# In[7]:


import seaborn as sns
sns.pairplot(bank_df_treated, hue = 'class', diag_kind = 'kde')


# In[8]:


X = bank_df.drop('class', axis=1)  
y = bank_df['class'] 


# In[9]:


from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)  


# In[10]:


from sklearn.svm import SVC  
svclassifier = SVC(kernel='linear')  
svclassifier.fit(X_train, y_train)  


# In[11]:


y_pred = svclassifier.predict(X_test)  


# In[12]:


from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  


# In[13]:


svclassifier = SVC(kernel='sigmoid')  
svclassifier.fit(X_train, y_train)  


# In[14]:


y_pred = svclassifier.predict(X_test)  


# In[15]:


print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  


# In[16]:


svclassifier = SVC(kernel='poly', degree=15) 
svclassifier.fit(X_train, y_train)  


# In[17]:


y_pred = svclassifier.predict(X_test)  


# In[18]:


print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  


# In[19]:


svclassifier = SVC(kernel='rbf')  
svclassifier.fit(X_train, y_train)  


# In[20]:


y_pred = svclassifier.predict(X_test)  


# In[21]:


print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  


# In[ ]:




