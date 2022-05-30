**FACE RECOGNITION**

This recognizes predefined faces in a picture and applies a pixelated blur to it.

**PACKAGES**

opencv: pip install opencv-python

numpy

face-recognition: pip install face-recognition

**Environment Variables**

IMAGES = name of folder in current directory containing images to match against

FACE = name of folder containing face to find

**FOLDERS**

/face: holds the image file of the face to look for. 

/images: Holds the image files to be compared against

**MODULES**

**face_blur**: BlurFace(coordinates=(bottom, right, top, left),
image=relative_path_to_image,
folder=relative_path_of_folder_containing_images_to_search_against,
name=name_of_image)

**recognize_face**:RecognizeFace(img=relative_path_to_image,
folder=relative_path_of_folder_containing_images_to_search_against,
)

