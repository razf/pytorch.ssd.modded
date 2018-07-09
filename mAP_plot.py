
# coding: utf-8

# In[14]:



import matplotlib.pyplot as plt
import numpy as np
#from data import STANFORD_CLASSES

jump=0.001
aprox_recall_vec = np.arange(0,1+jump,jump)
aprox_prec_vec =np.load('aprox_prec_vec.npy')
f, axarr = plt.subplots(6, 1,sharex=True)

for i in range(aprox_prec_vec.shape[0]):
    print(i)
    print(aprox_recall_vec.shape)
    print(aprox_prec_vec[i,:].shape)
    axarr[i].plot(aprox_recall_vec, aprox_prec_vec[i,:])
    #axarr[i, 0].set_title('Precision vs Recall - ' STANFORD_CLASSES.keys()[i])
    plt.xlim([0,1])
    plt.ylim([0,1])
    axarr[i].grid()
    plt.xlabel('recall')
    plt.ylabel('precision')
plt.show()


# In[12]:


get_ipython().system('rm mAP_plot.py')
get_ipython().system('jupyter nbconvert --to python mAP_plot.ipynb')


# In[12]:




