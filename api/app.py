import os
from flask import Flask, request
from dotenv import load_dotenv
from recognize_face import RecognizeFace
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

"""This is the endpoint that the react app would make requests to"""
load_dotenv()
port = os.getenv('PORT')
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg']

def allowed_file(filename):
    if '.' in filename and filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

app = Flask(__name__)
CORS(app)

#TODO 1: Create route to load image into face folder,
# blur images where the face appears from the images folder,
# and then returns the blurred images as a file.
# The image sent should be removed from the folder after the operation
@app.route("/find", methods=['POST'])
def upload_file():
   pass
            
        
    


#TODO 2: Create route to save images into the images folder
# This returns a message of the status of the save
@app.route("/save", methods=['POST'])
def upload_filen():
     if request.method == 'POST':
            #Check if the post request has the file part
        if 'file' not in request.files:
            pass
            



if __name__ == '__main__':
    app.run(port=port, debug=True)