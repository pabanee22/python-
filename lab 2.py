#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = 27
b = 3
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# In[3]:


a=2
b=22
print("A") if a>b else print("Equals") if a==b else print("B")


# In[4]:


for num in [2, 77, 12, 42, 24, 55, 3]:
    if num%2 == 0:
        pass
    else:
        print(num)


# In[5]:


for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


# In[ ]:


list=[]
num =int(input())
for i in range(num):
    elements =input()
    list.append(elements)
print(list)    
list.sort()
print(list)
list.sort(reverse = true)
print(list)


# In[2]:


thistuple = ("mango", "banana", "grape", "melon", "orange", "apple", "mango")
print(thistuple[1]) 
print(thistuple[-4]) 
print(thistuple[3:5]) 
print(thistuple[-4:-1]) 
print(thistuple[-3:1]) 


# In[1]:


#joining of list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

#method-1
list3 = list1 + list2
print(list3)

#method-2
for x in list2:
    list1.append(x)

print(list1)


# In[ ]:





# In[ ]:





# In[ ]:




