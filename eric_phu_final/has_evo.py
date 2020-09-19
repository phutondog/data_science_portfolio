#!/usr/bin/env python
# coding: utf-8

# In[23]:


from bs4 import BeautifulSoup
import requests


# In[24]:


with open('evo.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# In[ ]:





# In[26]:


box = soup.find_all('td')
poke_list = []


# In[27]:


for x in range(len(box)-1):
    size = len(box)
    if '→' in str(box[x + 1].text):
        poke = str(box[x].text)
        poke_list.append(poke)
    else:
        x = False


# In[28]:


try:
    while True:
        poke_list.remove(' \xa0\n')
except ValueError:
    pass


# In[29]:





# In[30]:





# In[36]:


def combineList(l):
    y = ""
    for x in l:
        y += x
    return y


# In[37]:


final_list = []
for x in poke_list:
    change = list(x)
    change.pop(0)
    change.pop(-1)
    done = combineList(change)
    final_list.append(done)

final_list.append('Mime_Jr')
# In[38]:





# In[ ]:




