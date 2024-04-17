#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NAME : 
#REF NO : 


# In[3]:


# Load the necessary packages

# Read the Image and convert to grayscale
image=cv2.imread(".jpg")
image1=cv2.cvtColor(image,cv2.)


# In[4]:


# Use Global thresholding to segment the image
cv2.threshold(image, threshold_value, max_val, thresholding_technique)


# In[5]:


# Use Adaptive thresholding to segment the image

cv2.adaptiveThreshold(source, max_val, adaptive_method, threshold_type, blocksize, constant)


# In[6]:


# Use Otsu's method to segment the image 
cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# In[7]:



# Display the results
titles=["Gray Image","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC"
       ,"THRESH_TOZERO","THRESH_TOZERO_INV","ADAPTIVE_THRESH_MEAN_C","ADAPTIVE_THRESH_GAUSSIAN_C","OTSU"]
images=[image1,]
for i in range(0,):
    plt.figure(figsize=(10,))
    plt.subplot(1,2,1)
    plt.title("Original Image")
    plt.imshow(image)
    plt.axis("off")
    plt.subplot(1,)



# In[ ]:




