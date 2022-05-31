import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from recognize_face import RecognizeFace
from werkzeug.utils import secure_filename
from flask_cors import CORS

"""This is the endpoint that the react app would make requests to"""
load_dotenv()
port = os.getenv('PORT')
images_folder = os.getenv('IMAGES')
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg']

def allowed_file(filename):
    if '.' in filename and filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

app = Flask(__name__)
CORS(app)


@app.route("/<path:endpoint>", methods=['POST'])
def upload_file(endpoint):
    #TODO 2: Create route to save images into the images folder
    # This returns a message of the status of the save
    if endpoint == 'save':
        if request.method == 'POST':
            #Check if the post request has the file part
            if 'file' not in request.files:
                return jsonify({'message': 'No file part'})
            file = request.files['file']
            # If the user does not select a file, the browser submits
            # an empty file without a filename
            if file.filename == '':
                return jsonify({'message': 'No selected file'})
            if file and allowed_file(file.filename):
                with open(os.path.join(os.curdir, images_folder,
                                    file.filename), 'w') as image:
                    image.write(file)
                    return jsonify({'message': 'image saved!'})
    #TODO 1: Create route to load image into face folder,
    # blur images where the face appears from the images folder,
    # and then returns the blurred images as a file.
    # The image sent should be removed from the folder after the operation
    if endpoint == 'find':
        pass
            



if __name__ == '__main__':
    app.run(port=port, debug=True)