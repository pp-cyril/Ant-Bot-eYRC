# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  E-Yantra Robotics Competition
*                  ================================
*  This software is intended to check version compatiability of open source software
*  Theme: ANT BOT
*  MODULE: Task1.1
*  Filename: Task1.1.py
*  Version: 1.0.0  
*  Date: October 31, 2018
*  
*  Author: e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""

"""
ArUco ID Dictionaries: 4X4 = 4-bit pixel, 4X4_50 = 50 combinations of a 4-bit pixel image
List of Dictionaries in OpenCV's ArUco library:
DICT_4X4_50	 
DICT_4X4_100	 
DICT_4X4_250	 
DICT_4X4_1000	 
DICT_5X5_50	 
DICT_5X5_100	 
DICT_5X5_250	 
DICT_5X5_1000	 
DICT_6X6_50	 
DICT_6X6_100	 
DICT_6X6_250	 
DICT_6X6_1000	 
DICT_7X7_50	 
DICT_7X7_100	 
DICT_7X7_250	 
DICT_7X7_1000	 
DICT_ARUCO_ORIGINAL

Reference: http://hackage.haskell.org/package/opencv-extra-0.2.0.1/docs/OpenCV-Extra-ArUco.html
"""

import numpy
import cv2
import cv2.aruco as aruco

def aruco_gen(id_aruco, num_pixels):            #This function expects two parameters as arguments-ID and the number of pixels in resolution. Both these inputs are whole decimal numbers.

            
    aruco_dict = aruco.Dictionary_get(aruco.DICT_nXn_C)          #Replace n with number of bits per pixels and C with the number of combinations                                                   
    img = aruco.drawMarker(aruco_dict, id_aruco, num_pixels)     #Select n and C from the list mentioned above
    img1 = cv2.copyMakeBorder(img,25,25,25,25,cv2.BORDER_CONSTANT,value=255)    #embeds a white border of 25 pixels on all sides
    image=cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)                                #RGB color conversion
    font=cv2.FONT_HERSHEY_SIMPLEX
    s1 ='ArUco ID='
    s2= str(id_aruco)
    sf= s1+s2
    cv2.putText(image,sf,(180,15),font,0.50,(0,0,255),1)                        #embeds the ID of the ArUco marker in Red Font
    des1='C:\\400_Task1.1\\Images\\ArUco'
    des2='.jpg'
    destination=des1+s2+des2
    
    cv2.imwrite(destination ,image )                                            #saves the image as ArUco<#ID>.jpg as per the respective ID 
    cv2.imshow('frame',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":    
    aruco_gen(id_aruco, num_pixels)                                              #parameters- ArUco ID and number of pixels
    
