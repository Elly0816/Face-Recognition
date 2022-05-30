import os
from face_blur import BlurFace
import cv2
import face_recognition
from dotenv import load_dotenv

load_dotenv()

images_folder = os.getenv('IMAGES')
face_folder = os.getenv('FACE')

## TODO: Returns a list of coordinates of matches from files in the images folder
class RecognizeFace:
    """This class recognizes the faces in an image and calls the BlurFace object to blur and save the faces found in the image.
    It takes two arguments: the img parameter is the relative path to the image and the folder is the relative path to the folder
    to search for the images
    It returns nothing"""
    def __init__(self, img: str, folder: str) -> None:
        self.img  = img #Image with known face
        self.folder = folder
        self.resize = 0.25
        # self.to_encode(self.img)
        self.required_face = self.to_encode(self.img)
        self.detect_required_faces(self.required_face, folder)

    def to_encode(self, img):
        """This returns the encoding of the face to be found"""
        img = cv2.imread(img)
        img_encoding = face_recognition.face_encodings(img)[0]

        return img_encoding


    def detect_required_faces(self, img_encoded, folder):
        """This method finds similar faces and blurs the location when found"""
        for image in os.listdir(os.path.join(os.curdir, folder)):
            #Find all the faces, face locations and face encodings in the current image
            to_blur = os.path.join(os.curdir, folder, image)
            img = cv2.imread(to_blur)
            face_locations = face_recognition.face_locations(img)
            face_encodings = face_recognition.face_encodings(img, face_locations)

            for  face_encoding, face_location in zip(face_encodings,face_locations):
                # If the faces match, blur it
                if face_recognition.compare_faces([img_encoded], face_encoding)[0]:
                    BlurFace(face_location, to_blur, name=image, folder=folder)



# TODO: grab the rectangle cordinates of the image

RecognizeFace(img=f'{face_folder}/jim.jpg', folder=images_folder)

# i