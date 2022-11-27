#!/usr/bin/env python
# coding: utf-8

# In[3]:


year = 2014 
if year % 4 == 0:
    print('Leap Year')
else:
    print('Not leap year')


# In[4]:


x = 40.7
y = 100
z = 20.4

max(x,y,z)


# In[9]:


my_list = ['Hello World']
test_list = []
if len(my_list) > 0:
    print (True)
else:
    print(False)
    
if len(test_list) < 0:
    print(True)
else:
    print(False)


# In[11]:


List_1=[1,2,3]
List_2=['Banana', 'Apple' , 'Orange']
list_3  = List_1 + List_2
print(list_3)


# In[12]:


Mul_list=['Apple']
mul_list2 = Mul_list * 5
print(mul_list2)


# In[21]:


Str_x = 'Emma is a good painter. Emma is also a good Teacher'
print(Str_x.count('Emma'))


# In[23]:


D1 = {'first_name' : 'Jim', 'age' : 23, 'height' : 6.0 , 'job' : 'developer', 'company': 'XYZ'}
D1['age']


# In[26]:


list_x=['Python','Java','GO','Dot Net','Python','GO']
lst1 = set(list_x)
print(list(lst1))


# In[27]:


lst2 = [1, 'a', 2 , 'b', 3 , 'c']
D2 = dict(lst2)
print(D2)


# In[31]:


str3 = 'Umbrella'
if 'e' in str3:
    print ('Contains e')
else:
    print('does not contain e')


# In[41]:


My_list= 'Python is a fun Programming Language'
lst4 = My_list.split(',')
print(lst4)


# In[40]:


My_tuple= ('my','phone','number','is','123')
str4 = '#'.join(My_tuple)
print(str4)


# In[45]:


Foot_ball_teams= ['Qatar', 'Brazil' , 'Argentina' , 'France' , 'Belgium']
for i in Foot_ball_teams:
    print(i)


# In[44]:


for i in Foot_ball_teams:
    print('World Cup 2022' + ' ' + i)


# In[58]:


for i in Foot_ball_teams:
    i.upper()
print(i)


# In[70]:


fifa_list = []
g = [i.upper() for i in Foot_ball_teams]
fifa_list.append(g)
print(fifa_list)


# In[80]:


lenght_fifa = []

for i in Foot_ball_teams:
    index = Foot_ball_teams.index(i)
    print('index of', i , 'is', index)
    print('lenght of', i, 'is', len(i))


# In[85]:


list_1=[109,44,-33,567,753,-100,-33,-89,798,90,-70]
new_list = []
for i in list_1:
    if i >= 0:
        new_list.append(i)
print(new_list)


# In[ ]:




