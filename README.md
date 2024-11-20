
# Image cropping using Retina Face 

This project utilizes the RetinaFace machine learning model to crop faces from an image dataset, preparing the data for facial recognition model training.
![Face Cropping Demo](IMG_0631.gif "Face Cropping in Action")


## Appendix

This script detects and crops faces from images using the RetinaFace model and save the cropped images to a specified folder.
### imports
- RetinaFace: Detects faces in images.
- cv2: Reads and writes images.
- os: Handles file and directory operations.
- random: Generates random numbers for unique filenames.

### variables
- path: Directory containing input images. Replace "INPUT YOUR PICTURES PATH" with the folder path.
- output: Directory to save cropped images. Replace "INPUT OUTPUT PATH" with the desired output folder path.



## Dependencies
pip install retina face opencv-python
