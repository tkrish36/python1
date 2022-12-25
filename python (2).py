#!/usr/bin/env python
# coding: utf-8

# In[5]:


subjects = ['Americans','Indians']
verbs = ['play','watch']
objects = ['baseball','cricket']


# In[13]:


for (a,b,c) in zip(subjects,verbs,objects):
    print(a,b,c)

    


# In[14]:


subjects = ['Americans','Indians']
verbs = ['play','watch']
objects = ['baseball','cricket']
combined = [(subjects,verbs,objects)]


# In[15]:


print(combined)


# In[16]:


for x in subjects:
    for z in verbs:
        for c in objects:
            print(x,z,c)


# In[ ]:




