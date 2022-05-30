import os
from flask import Flask
from dotenv import load_dotenv
from recognize_face import RecognizeFace
from werkzeug.utils import secure_filename

"""This is the endpoint that the react app would make requests to"""
load_dotenv()
port = os.getenv('PORT')
ALLOWED_EXTENSIONS = ['']

app = Flask(__name__)

#TODO 1: Create route to load image into face folder,
# blur images where the face appears from the images folder,
# and then returns the blurred images as a file.
# The image sent should be removed from the folder after the operation
@app.route("/find")
def find():
    pass
    


#TODO 2: Create route to save images into the images folder
# This returns a message of the status of the save
@app.route("/save")
def save():
    pass



if __name__ == '__main__':
    app.run(port=port, debug=True)