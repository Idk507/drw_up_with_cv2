#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2 as cv


# In[ ]:


canvas = np.ones([500,500,3],'uint8')*255
radius = 3
color = (0,255,0)
pressed = False
def click(event,x,y,flags,param):
    global canvas ,pressed
    if event == cv.EVENT_LBUTTONDOWN:
        pressed = True
        cv.circle(canvas,(x,y),radius,color,-1)
    elif event == cv.EVENT_MOUSEMOVE and pressed == True:
        cv.circle(canvas,(x,y),radius,-1)
        
    elif event == cv.EVENT_LBUTTONUP:
       
        pressed = False
cv.namedWindow("canvas")
cv.setMouseCallback("canvas",click)

while True:
    cv.imshow("canvas",canvas)
    ch = cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color = (255,0,0)
cv.destroyAllWindows()        


# In[ ]:


cv.destoryAllWindows()


# In[ ]:




