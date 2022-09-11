import cv2
import numpy as np
import os
from gtts import gTTS
from playsound import playsound 
import inflect

# make sure to change the path to that path of your images data.

path = "E:\\firstpro.py\\images"

mylist = os.listdir(path)
print(mylist)

orb = cv2.ORB_create( nfeatures = 1000 )

# this is to create a list contains the des of all images in the directory
deslist = []
for image in mylist:
    kp , des = orb.detectAndCompute(cv2.imread(f'{path}\{image}',0) , None)
    deslist.append(des)


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# this function to return the "index" of the best match (smallest_distance) among my list in the directory

def min_distance_index(des1):
    dist_list = []
    for des in deslist:
        matches = bf.match(des,des1)
        matches = sorted(matches,key = lambda x : x.distance )
        dist_list.append(matches[0].distance)
    print(dist_list)
    return ( dist_list.index(min(dist_list)) )
    # This dictionary is to match the images to their count and audio files.

check_dict = { (0.5,'audio05.mp3')   : ("FiftyPiasters1.jpg", "FiftyPiasters2.jpg", "FiftyPiasters3.jpg", "FiftyPiasters4.jpg"),
                (1,'audio1.mp3')     : ("OnePound1.jpg", "OnePound2.jpg" , "OnePound3.jpg", "OnePound4.jpg"),
                (5,'audio5.mp3')     : ("FivePounds1.jpg", "FivePounds2.jpg","FivePounds3.jpg","FivePounds4.jpg"),
               (10,'audio10.mp3')    : ("TenPounds1.jpg", "TenPounds2.jpg", "TenPounds3.jpg", "TenPounds4.jpg", "TenPounds5.jpg","TenPounds6.jpg","TenPounds7.jpg","TenPounds8.jpg"),
               (20,'audio20.mp3')    : ("TwentyPounds1.jpg","TwentyPounds2.jpg","TwentyPounds3.jpg","TwentyPounds4.jpg"),
               (50,'audio50.mp3')    : ("FiftyPounds1.jpg", "FiftyPounds2.jpg", "FiftyPounds3.jpg", "FiftyPounds4.jpg"),
               (100,'audio100.mp3')  : ("OnehundredPounds1.jpg","OnehundredPounds2.jpg","OnehundredPounds3.jpg","OnehundredPounds4.jpg"),
               (200,'audio200.mp3')  : ("TwohundredPounds1.jpg","TwohundredPounds2.jpg","TwohundredPounds3.jpg","TwohundredPounds4.jpg"),
                }

# Activating the webcam.

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img = cv2.flip(img,1)
    cv2.imshow("my",img)
    if cv2.waitKey(1) == ord('w'):
        cv2.imwrite("mytemp.jpg",img)
        kp1 , des1 = orb.detectAndCompute(cv2.imread("mytemp.jpg",0) , None)
        check = mylist[min_distance_index(des1)]
        
        for i in check_dict:
            if check in check_dict[i]:
                count += i[0]
                playsound(i[1])
                break
        print(check)

    if cv2.waitKey(1) == ord('q'):
        print(count)
        p = inflect.engine()
        x = p.number_to_words(count)

        # playing the total money sound
         
        textT =f"You have {x} pounds total"
        g = gTTS(text=textT , lang= 'en')
        g.save('audioT.mp3')
        playsound('audioT.mp3')

        # removing unused files.

        os.remove('audioT.mp3')
        os.remove("mytemp.jpg")
        break

cap.release()
cv2.destroyAllWindows()