**Face Blur: React / Flask Application**

[Live Site](https://faceblur01.herokuapp.com/)

The client contains a react frontend that posts to two routes on the flask server.


The routes are /save and /find

**/save**

This route saves the image to a folder as one of the images to find a face in and blur


**/find**

This route sends a face to the server to find and blur if it exists in the saved images.


**Clone the repo with**: git clone https://github.com/Elly0816/Face-Recognition.git


**Server**

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
