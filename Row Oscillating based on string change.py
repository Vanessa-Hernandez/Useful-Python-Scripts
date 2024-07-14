#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.dates as dates
import time
import numpy as np
from matplotlib.colors import LightSource
import scipy.interpolate

get_ipython().run_line_magic('matplotlib', 'notebook')
#calling the location of where the original excel sheet is at.
direct = "C:/Users/vhernan7/Downloads/"

#++++++***************** REMEMBER TO INPUT A CSV +++++++++++++++++++++++++**********

df = pd.read_csv(direct+"Book39.csv", encoding='latin-1') 
#create a new column where you put the first 5 strings in the seedling number.
df['new_col'] = df['Seedling'].astype(str).str[:5]

#create a new column and call it Number and put them in numerical order.

df['Number'] = df.new_col.astype('category').cat.codes.add(1)

#create a new column called New_Number.
i = df.new_col
df['New_Number'] = i.ne(i.shift()).cumsum()

#Make Var3 in order.
df[["New_Number"]] = df[["New_Number"]].apply(pd.to_numeric)



#is_odd = (df['Var3'] & 1) == 1
df['is_odd'] = (df['New_Number'] & 1) == 1


#Make the pink tags by calling the odd numbers.Put in the downloads
dfPink = df[df['is_odd'] == True]
print (dfPink)
dfPink.to_excel(r'/Users/vhernan7/Downloads/Block7_West_color2.xlsx')


#Make the blue tags by calling the even numbers.Put in the downloads
dfBlue = df[df['is_odd'] == False]
print (dfBlue)
dfBlue.to_excel(r'/Users/vhernan7/Downloads/Block7_West_color1.xlsx')


#df.to_string(max_rows=float('inf'), max_cols=float('inf')))
print (df)


# In[ ]:





# In[ ]:




