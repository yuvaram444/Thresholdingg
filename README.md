# THRESHOLDING
## Aim
To segment the image using global thresholding, adaptive thresholding and Otsu's thresholding using python and OpenCV.

## Software Required
1. Anaconda - Python 3.7
2. OpenCV

## Algorithm

### Step1:
Load the necessary packages.

### Step2:
Read the Image and convert to grayscale.<br>

### Step3:
Use Global thresholding to segment the image.<br>

### Step4:
Use Adaptive thresholding to segment the image.<br>

### Step5:
Use Otsu's method to segment the image and display the results.<br>

## Program

```
# Load the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import cv2
```
# Read the Image and convert to grayscale
```
image = cv2.imread("C:/Users/admin/OneDrive/Pictures/Screenshots/Screenshot 2025-04-24 173304.png",1)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image_gray = cv2.imread("C:/Users/admin/OneDrive/Pictures/Screenshots/Screenshot 2025-04-24 173304.png",0)
```
# Use Global thresholding to segment the image
```
ret,thresh_img1=cv2.threshold(image_gray,86,255,cv2.THRESH_BINARY)
ret,thresh_img2=cv2.threshold(image_gray,86,255,cv2.THRESH_BINARY_INV)
ret,thresh_img3=cv2.threshold(image_gray,86,255,cv2.THRESH_TOZERO)
ret,thresh_img4=cv2.threshold(image_gray,86,255,cv2.THRESH_TOZERO_INV)
ret,thresh_img5=cv2.threshold(image_gray,100,255,cv2.THRESH_TRUNC)
```
# Use Adaptive thresholding to segment the image
```
thresh_img7=cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thresh_img8=cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
```
# Use Otsu's method to segment the image 
```
ret,thresh_img6=cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
```
# Display the results
# ORIGIONAL IMAGE
```
plt.axis("off")
plt.title("Original Image")
plt.imshow(image)
```
![image](https://github.com/user-attachments/assets/05ed1faf-1302-401e-91ac-8304b3d1df62)
# GREY IMAGE
```
plt.axis("off")
plt.title("Gray Image")
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/283b419c-b9dc-4bbf-ad1b-4e455b349876)

# Threshold Image (Binary)
```
plt.axis("off")
plt.title("Threshold Image (Binary)")
plt.imshow(cv2.cvtColor(thresh_img1, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/278344ab-f64a-496a-a725-7ff14c04f393)

# Threshold Image (Binary Inverse)
```
plt.axis("off")
plt.title("Threshold Image (Binary Inverse)")
plt.imshow(cv2.cvtColor(thresh_img2, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/e88f8a5f-adc8-4383-85f4-5cdecfb8008a)

# Threshold Image (To Zero)
```
plt.axis("off")
plt.title("Threshold Image (To Zero)")
plt.imshow(cv2.cvtColor(thresh_img3, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/68750825-2f24-4b19-a688-f2c16f67d099)

# Threshold Image (To Zero-Inverse)
```
plt.axis("off")
plt.title("Threshold Image (To Zero-Inverse)")
plt.imshow(cv2.cvtColor(thresh_img4, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/e10858fb-52ae-408a-8883-16b3c256d106)

# Threshold Image (Truncate)
```
plt.axis("off")
plt.title("Threshold Image (Truncate)")
plt.imshow(cv2.cvtColor(thresh_img5, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/af1f1e66-3a13-447a-a442-aabfb254130e)

# Otsu
```
plt.axis("off")
plt.title("Otsu")
plt.imshow(cv2.cvtColor(thresh_img6, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/1fed3379-63b5-44ee-8a87-24887bab9268)

# Adaptive Threshold (Mean)
```
plt.axis("off")
plt.title("Adaptive Threshold (Mean)")
plt.imshow(cv2.cvtColor(thresh_img7, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/60adcb81-22c8-4a27-80df-4a84e5d36df9)

# Adaptive Threshold (Gaussian)
```
plt.axis("off")
plt.title("Adaptive Threshold (Gaussian)")
plt.imshow(cv2.cvtColor(thresh_img8, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```
![image](https://github.com/user-attachments/assets/1e9a9da1-38b2-47f7-b0bb-b761883c9a50)

## Result
Thus the images are segmented using global thresholding, adaptive thresholding and optimum global thresholding using python and OpenCV.
