import numpy as np
import cv2

class BlurFace:
    """This blurs certain coordinates from an image.
    It takes 2 parameters upon instantiation: coordinates and the name of the image file.
    Coordinates should be sent as a list containing the bottom, right, top and left corners of the detected face respectively.
    The module writes the blurred images back to the path f"{os.curdir}/{folder}/blur_{image}
    with the string 'blur_' prepended. The name of the image should be passed in """
    def __init__(self, coordinates: list[int], image: str, folder: str, name: str) -> None:
        self.coordinates = coordinates
        self.image = image
        self.folder = folder
        self.name = name
        self.pixelate_face()



    def pixelate_face(self, blocks=5):
        # find the coordinates sent on the image
        img = cv2.imread(self.image)

        #Coordinates should be sent as [bottom, right, top, left]
        bottom = self.coordinates[0]
        top = self.coordinates[2]
        left = self.coordinates[3]
        right = self.coordinates[1]
        if left >= right or bottom >= top:
            print(f"Invalid coordinates: {[left, top], [right, bottom]}")
        else:
            #Get the height and width of the region of interest (roi)
            # Linearly spaced integers starting from the bottom left coordinate of the image to the top right coordinate
            xSteps = np.linspace(left, right, blocks+1, dtype='int')
            ySteps = np.linspace(bottom, top, blocks+1, dtype='int')
            # loop over blocks in y and x
            for i in range(1, len(ySteps)):
                for j in range(1, len(xSteps)):
                    left = xSteps[j -1]
                    bottom = ySteps[i -1]
                    right = xSteps[j]
                    top = ySteps[i]
                    roi = img[bottom:top, left:right]
                    # Changes the rgb value to an average of the local region of interest
                    (R, G, B) = [int(x) for x in cv2.mean(roi)[:3]]
                    cv2.rectangle(img, (left, bottom), (right, top),
                                  (R, G, B), -1)

            # Writes the image back to the folder with blur_ prepended

            if self.name:
                if self.folder:
                    cv2.imwrite(f"./{self.folder}/blur_{self.name}", img)
                else:
                    cv2.imwrite(f"/blur_{self.name}", img)
            else:
                if self.folder:
                    cv2.imwrite(f"/{self.folder}/blur_{self.image}", img)
                else:
                    cv2.imwrite(f"/blur_{self.image}", img)


