
# coding: utf-8

# In[2]:


get_ipython().system('ls')


# In[3]:


import matplotlib.pyplot as plt
import numpy as np

aps_vector =np.load('aps_vector.npy')
plt.plot(aps_vector)
plt.grid()
plt.title('mAP plot')
plt.xlabel('recall')
plt.ylabel('precision')
plt.xlim([0,1])
plt.ylim([0,1])
plt.show()


# In[4]:


get_ipython().system('jupyter nbconvert --to script')

