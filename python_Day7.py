#!/usr/bin/env python
# coding: utf-8

# # make keys of given dictionary values and values key

# In[3]:


port1={21:'ftp',22:'ssh',23:'telnet',80:'http'}
port2={}
port2={v:k for k,v in port1.items()}
print(port2) 


# # Take the list of tuple and make new list contain sum of numbers in tuple

# In[4]:


list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
for each in list1:
    list2.append(each[0]+each[1])
print(list2)


# # Make elements of list in given list be elements of inner list and tuple to be element of outer list

# In[11]:


l1=[(1,2,3),[1,2],["a","hit","less"]]
l2=l1[1]+l1[2]
l3=list(l1[0])
l3.append(l2)
print(l3)


# In[ ]:




