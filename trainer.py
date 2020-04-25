import os
from tkinter import *
import cv2
import numpy as np 
from tkinter import messagebox
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'
if not os.path.exists('./trainer'):
    os.makedirs('./trainer')
def getImagesWithID(path):
  imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
  faces = []
  IDs = []
  for imagePath in imagePaths:
    faceImg = Image.open(imagePath).convert('L')
    faceNp = np.array(faceImg,'uint8')
    ID = int(os.path.split(imagePath)[-1].split('.')[1])
    faces.append(faceNp)
    IDs.append(ID)
    cv2.imshow("training",faceNp)
    cv2.waitKey(10)
  return np.array(IDs), faces
Ids, faces = getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.write('trainer/trainer.yml')
cv2.destroyAllWindows()
messagebox.showinfo("Success", "Trained Successfully")
