from retinaface import RetinaFace as RT # import the retina facial recognition model
import cv2
import os
import random

path = "/Users/onyi/Desktop/vscodetest/"

output = "/Users/onyi/Desktop/Done/"

def crop_retina(data_path, output_path):
  
    for image in os.listdir(data_path):
        if image.endswith('jpeg'):
            pic = os.path.join(data_path, image)
            detector = RT.detect_faces(pic)
            
            for i, key in enumerate(detector.keys()):
                face = detector[key]
                facial = face['facial_area']
                x_min, y_min, x_max, y_max = facial
                image = cv2.imread(pic)
                cropped = image[y_min:y_max, x_min:x_max]
                rand = random.randint(100, 1000)
                cropped_path = os.path.join(output_path, f'{rand}.jpeg')
                cv2.imwrite(cropped_path, cropped)





# if __name__ == "__main__":
crop_retina(path, output)