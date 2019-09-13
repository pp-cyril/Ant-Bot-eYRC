import numpy
import cv2
import cv2.aruco as aruco
import aruco_lib
import csv
global imagename

imagename=str(input("Enter image name"))       ##takes input from the user about the name with which the image will be saved
with open('400_Task1.2.csv','a',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['Image Name','ArUco ID', '(x,y)Object-1','(x,y)Object-2']) 

object1=str(input("Enter object 1"))           ##takes input from the user about the shape of object1
color1=str(input("Enter color of object 1"))   ## takes input from the user about the color of object1
object2=str(input("Enter object 2"))           ##takes input from the user about the shape of object2
color2=str(input("Enter color of object 2"))   ##takes input from the user about the color of object2

def aruco_detect(path_to_image):
    '''
    you will need to modify the ArUco library's API using the dictionary in it to the respective
    one from the list above in the aruco_lib.py. This API's line is the only line of code you are
    allowed to modify in aruco_lib.py!!!
    '''
    img =  cv2.imread(path_to_image)    
    id_aruco_trace = 0
    det_aruco_list = {}
    
    
    det_aruco_list = aruco_lib.detect_Aruco(img)
    if (det_aruco_list):
        img3=aruco_lib.mark_Aruco(img,det_aruco_list)
        id_aruco_trace=aruco_lib.calculate_Robot_State(img3,det_aruco_list)
        print(id_aruco_trace)
        k= str(id_aruco_trace)
        i=1
        x=0
        while (k[i]!=':'):
            x=x*10 + int(k[i])
            i=i+1
        print(x)
    global csv_arucoid
    csv_arucoid= str(x)
    
     
    color_detect(img)                       #color detection and shape detection function triggered here


def color_detect(img):
    
    global flag
    global check
    flag=-1
    check=-1
    global centre1
    global centre2
    grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting image to grayscale
    ret,threshold = cv2.threshold(grayImage,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#binary and otsu thresholding is done 

    th,contours,hierarchy = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)#to find out contours 
    numContours = len(contours)#to return number of contours detected
    font = cv2.FONT_HERSHEY_SIMPLEX #setting text to a particular font


    if (numContours!=1):
        
        
        for i in range(0,numContours-1):
            
            
            cnt = contours[i]
            M = cv2.moments(cnt)
            if int(M["m00"])!=0:
                Cx = int(M["m10"]/M["m00"])                 #finds x coordinate of centroid
                Cy = int(M["m01"]/M["m00"])                 #finds y coordinate of centroid
            else:
                Cx=0
                Cy=0
            x=str(Cx)
            y=str(Cy)
            centre= '(' + x + ',' + y + ')' 
           

            px  = img[Cy,Cx] #finds out bgr value at the center of a particular contour
            epsilon = 0.01*cv2.arcLength(cnt,True) #arc length of a particular contour
            approx = cv2.approxPolyDP(cnt,epsilon,True) #returns number of vertices

####for object 1###
            if(color1.lower()=="red"):
                if((px[2]>170 and px[2]<255)and(px[1]>=0 and px[1]<27)and (px[0]>=0 and px[0]<27)): #for red color
                    if(object1.lower()=="circle"):
                        if len(approx) >= 15:  #for circle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,255,0),25) #drawing contours
                            centre1=str(centre)
                            flag=1   
                            

                    elif(object1.lower()=="square"):
                        if len(approx) == 4: #for square
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,255,0),25) #drawing contours
                            centre1=str(centre)
                            flag=1
                            
                    elif(object1.lower()=="triangle"):
                        if len(approx) == 3: #for triangle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,255,0),25) #drawing contours
                            centre1=str(centre)
                            flag=1
                            
                    elif(object1.lower()=="ellipse"):
                        if (len(approx) >=7 and len(approx) <15): 
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,255,0),25) #drawing contours
                            centre1=str(centre)
                            flag=1
                            
            elif(color1.lower()=="green"):
                if((px[2]>=0 and px[2]<84) and (px[1]>105 and  px[1]<256) and(px[0]>=0 and px[0]<84)):#for green color
                    if(object1.lower()=="circle"):
                        if len(approx) >= 15:  #for circle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(255,0,0),25) #drawing contours
                            centre1=str(centre)
                            flag=1
                            
                    elif(object1.lower()=="square"):
                        if len(approx) == 4: #for square
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(255,0,0),25) #drawing contours
                            centre1=str(centre)
                            flag=1

                    elif(object1.lower()=="triangle"):
                        if len(approx) == 3: #for triangle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(255,0,0),25) #drawing contours
                            centre1=str(centre)
                            flag=1
                            
                    elif(object1.lower()=="ellipse"):
                        if (len(approx) >=7 and len(approx) <15):
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(255,0,0),25) #drawing contours
                            centre1=str(centre)
                            flag=1
                    
            elif(color1.lower()=="blue"):
                if((px[2]>=0 and px[2]<139) and (px[1]>=0 and px[1]<139) and (px[0]>138 and px[0]<250)):#for blue color
                    if(object1.lower()=="circle"):
                        if len(approx) >= 15:  #for circle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,0,255),25) #drawing contours
                            centre1=str(centre)
                            flag=1
                                

                    elif(object1.lower()=="square"):
                        if len(approx) == 4: #for square
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,0,255),25) #drawing contours
                            centre1=str(centre)
                            flag=1
                            
                    elif(object1.lower()=="triangle"):
                        if len(approx) == 3: #for triangle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,0,255),25) #drawing contours
                            centre1=str(centre)
                            flag=1

                    elif(object1.lower()=="ellipse"):
                        if (len(approx) >=7 and len(approx) <15):
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,0,255),25) #drawing contours
                            centre1=str(centre)
                            flag=1

            
###for object 2###
            if(color2.lower()=="red"):
                if((px[2]>170 and px[2]<255)and(px[1]>=0 and px[1]<27)and (px[0]>=0 and px[0]<27)): #for red color
                    if(object2.lower()=="circle"):
                        if len(approx) >= 15:  #for circle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,255,0),25) #drawing contours
                            centre2=str(centre)
                            check=1
                            
                    elif(object2.lower()=="square"):
                        if len(approx) == 4: #for square
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,255,0),25) #drawing contours
                            centre2=str(centre)
                            check=1

                    elif(object2.lower()=="triangle"):
                        if len(approx) == 3: #for triangle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,255,0),25) #drawing contours
                            centre2=str(centre)
                            check=1

                    elif(object2.lower()=="ellipse"):
                        if (len(approx) >=7 and len(approx) <15):
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,255,0),25) #drawing contours
                            centre2=str(centre)
                            check=1
                            
            elif(color2.lower()=="green"):
                if((px[2]>=0 and px[2]<84) and (px[1]>105 and  px[1]<256) and(px[0]>=0 and px[0]<84)):#for green color
                    if(object2.lower()=="circle"):
                        if len(approx) >= 15:  #for circle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(255,0,0),25) #drawing contours
                            centre2=str(centre)
                            check=1
                            
                    elif(object2.lower()=="square"):
                        if len(approx) == 4: #for square
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(255,0,0),25) #drawing contours
                            centre2=str(centre)
                            check=1

                    elif(object2.lower()=="triangle"):
                        if len(approx) == 3: #for triangle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(255,0,0),25) #drawing contour
                            centre2=str(centre)
                            check=1
                            
                    elif(object2.lower()=="ellipse"):
                        if (len(approx) >=7 and len(approx) <15):
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(255,0,0),25) #drawing contours
                            centre2=str(centre)
                            check=1
                            
            elif(color2.lower()=="blue"):
                if((px[2]>=0 and px[2]<139) and (px[1]>=0 and px[1]<139) and (px[0]>138 and px[0]<250)):#for blue color
                    if(object2.lower()=="circle"):
                        if len(approx) >= 15:  #for circle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,0,255),25) #drawing contours
                            centre2=str(centre)
                            check=1
                            
                    elif(object2.lower()=="square"):
                        if len(approx) == 4: #for square
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,0,255),25) #drawing contours
                            centre2=str(centre)
                            check=1

                    elif(object2.lower()=="triangle"):
                        if len(approx) == 3: #for triangle
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,0,255),25) #drawing contours
                            centre2=str(centre)
                            check=1

                    elif(object2.lower()=="ellipse"):
                        if (len(approx) >=7 and len(approx) <15):
                            cv2.putText(img,centre,(Cx-10,Cy),font,0.35,(0,0,0),1)
                            cv2.drawContours(img,cnt,-1,(0,0,255),25) #drawing contours
                            centre2=str(centre)
                            check=1


    if(flag== -1):
        centre1='none'
    else:
        centre1='"'+centre1+'"'

    if(check== -1):
        centre2= 'none'
    else:
        centre2='"'+centre2+'"'

    aruconame= 'ArUco' + csv_arucoid + '.jpg'
    with open('400_Task1.2.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([aruconame,csv_arucoid,centre1,centre2])

    destination= 'C:\\400_Task1.2\\Images\\' + imagename + '.jpg'
    cv2.imwrite(destination, img)
    
    cv2.imshow("ColorImage",img)
    cv2.waitKey(0)
    cv2.DestroyAllWindows()



if __name__ == "__main__":    
    aruco_detect(path_to_image)             ###give the name of the image with the complete path
                                            ###change the dictionary bit size and combinations in aruco_lib.py in Ln32
                    
