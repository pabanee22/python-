#!/usr/bin/env python
# coding: utf-8

# In[1]:


#python program to find if given co-ordinates are inside circle
def isInside(circle_x, circle_y, rad, x, y):
    if ((x - circle_x) * (x - circle_x) +
        (y - circle_y) * (y - circle_y) <= rad * rad):
        return True;
    else:
        return False;

x = 1;
y = 1;
circle_x = 0;
circle_y = 1;
rad = 2;
if(isInside(circle_x, circle_y, rad, x, y)):
    print("Inside");
else:
    print("Outside");


# In[2]:


#Python Program to Map two lists into a Dictionary
keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is:")
print(d)


# In[3]:


#python program for the sum of first n numbn=int(input("Enter a number: "))
sum1 = 0
n=int(input())
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)


# In[ ]:




