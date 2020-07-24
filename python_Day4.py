#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s="what we think we become;we are python programmer"
subs="we"
i=s.find(subs)
while i!=-1:
    print(i)
    i=s.find(subs,i+len(subs),len(s))




