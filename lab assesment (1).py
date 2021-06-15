#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q1
d1={1:'a',2:'b',3:'c'}
d2={4:'d',5:'e',6:'f'}
d3={7:'g',8:'h',9:'i'}

dfinal={}
dfinal.update(d1)
dfinal.update(d2)
dfinal.update(d3)
print(dfinal)


# In[ ]:


d4 = {'name':'Preeti','address':'Nalco','city':'damanjodi','state':'odisha'}
print("name : {},add : {},city : {},state : {}".format())


# In[16]:


d5 = {'Mango': 10, 'grape': 5,'apple':4,'orange':6} 
op=1
for i in d5.values():
    op=op*i
print(op)


# In[17]:


d6={}
for i in range(2):
    key=input("Key : ")
    val=int(input("Value : "))
    d6[key]=val
print(d6)
ch=input("key for checking : ")
if ch in d6:
    print(ch," : ",d6[ch])
else:
    print(ch," not present")


# In[18]:


def fun1(a,b):
    if(a==1):
        print("Coming from if ")
    elif(b==1):
        print("Coming from elif")
    else:
        print("No condition satisfied")

fun1(1,2)


# In[ ]:




