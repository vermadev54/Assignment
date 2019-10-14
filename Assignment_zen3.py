
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


import json
with open('Downloads/datafile.json', 'r') as f:
    data = json.load(f)
data = pd.DataFrame([data])


# In[4]:


data =data.to_dict('dict')
#x = data.get("/blog")
#print(data['/%22]'])
values =[]
tempvalues = list(data.values())
for i in range(len(tempvalues)):
    values.append(tempvalues[i][0])
keys = list(data.keys())
result = []
dictionary = dict(zip(keys, values))


# In[ ]:


def transitive(dictionary):
    for key, value in dictionary.items():
        print(key, value)
        tempvalue = value
        name=tempvalue
        #print (name)
        while(tempvalue):
            tempvalue = dictionary.get(tempvalue)
            print(tempvalue)
            if(tempvalue):
                name = tempvalue
        result.append(name)
           
transitive(dictionary)
resul


# In[ ]:


dictionary_out = dict(zip(keys, result))
dictionary_out

