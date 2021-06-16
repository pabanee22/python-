#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input("Enter a number: "))  
sum = 0  
temp = n 
  
while temp > 0:  
    Number = temp % 10  
    sum += Number ** 3  
    temp //= 10  
print(sum)


# In[6]:


n=int(input("Enter a no:- "))
sum=0
for i in range(0,n+1):
    sum=sum+i
print(sum)


# In[7]:


n=int(input("Enter The no of terms:-  "))
result = list(map(lambda x: 2 ** x, range(n)))

print("The total terms are:",n)
for i in range(n):
    print("{}".format(result[i]))


# In[9]:


decimal = int(input("Enter a decimal number \n"))
binary = 0
ctr = 0
temp = decimal 

#calculating binary
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1
       
print("Binary of {} is: {}".format(decimal,binary))


# In[ ]:


print("Enter the values of the list:-1 ")
x=[]
for i in range(0,6):
    b=int(input(""))
    x.append(b)
y=int(input("Enter 2nd no:- "))
for i in range(0,4):
    if(x[i]%y==0):
         print("Numbers Divisible by another number are:- {}".format(x[i]))
else:
    print("Numbers are not divisible by another No's")
    break


# In[ ]:


x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))
if x > y:
    smaller = y
else:
    smaller = x
for i in range (1,smaller+1):
    if((x % i == 0) and (y % i == 0)):
        gcd = i
print("The GCD of {} and {} is:- {} ".format(x,y,gcd))


# In[ ]:




