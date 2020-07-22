#!/usr/bin/env python
# coding: utf-8

# # black slash,triple quotes,string inside quotes,escape sequence of string,formatted output


print("Hello       LetsUpgrade")

print(""" Hello everyone""")
print("""💘""")
"""💘"""

print('python\'s program')

print("python \t program")
print("python \n program")

name="xyz"
mark="90.8"
age="20"
print("name of person",name,"marks",mark,"age",age)
print(f"name of person is{name},marks{mark},age{age}")


# # variables and assignments

# In[26]:
x=y=10
print(x)
print(y)
id(y)
id(x)
del x
del y


# # Arithmatic operator

# In[32]:
a=5**5
print(a)
b=67/2
print(b)
c=10%2
print(c)
e=67//2
print(e)


# # comparison operator

# In[34]:
a=10
b=20
a == b
# In[35]:
c=10
a==c
# In[37]:
a>=b
# In[38]:
a!=b


# # Assignment operator

# In[40]:
a=10
a*40


# # bitwise operator

# In[49]:
a=240
bin(a)
# In[50]:
b=1
bin(b)
# In[51]:
a|b
# In[52]:
a&b
# In[53]:
a<<b
# In[54]:
a>>b
# In[55]:
a^b
# In[56]:
~a


# # Logical operators

# In[57]:
a=1
b=20
a>b


# In[58]:
a>b or 10>9
# In[59]:
a>b and 10>9


# In[63]:
a>b and 10>m
# In[64]:
not 10<9


# # Membership operators

# In[66]:


str="python programming"
"a" in str
# In[67]:
"a" not in str
# In[68]:
"x" not in str


# # Identity operator

# In[69]:
a=10
b=10
a == b
# In[70]:
a is b

# In[73]:
a=257
b=257
a==b
# In[74]:
a is b
# In[75]:
a is not b


# # Operator precedence

# In[76]:


10+10/29*4
# In[77]:
2**-1
# In[78]:
2**2


# In[ ]:




