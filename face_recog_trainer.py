import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
path = 'dataset'
strvar = 'dataset\\'


def getimgid():
    global path
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath)
        imageNp = np.array(pilImage, 'uint8')
        id = int(imagePath.strip(strvar).strip('.jpg').split('.')[0])
        faceSamples.append(imageNp)
        ids.append(id)
        cv2.imshow('training', imageNp)
        cv2.waitKey(10)
    return np.array(ids), faceSamples

ids, faces = getimgid()
recognizer.train(faces, ids)
recognizer.save('trainingDataset.yml')
cv2.destroyAllWindows()
