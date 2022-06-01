import os
from flask import Flask, jsonify, request, send_file
from dotenv import load_dotenv
from recognize_face import RecognizeFace
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from zipfile import ZipFile
# This allows for streaming bytes from a file
from io import BytesIO

"""This is the endpoint that the react app would make requests to"""
load_dotenv()
port = os.getenv('PORT')
images_folder = os.getenv('IMAGES')
face_folder = os.getenv('FACE')
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg']

def allowed_file(filename):
    if '.' in filename and filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/<path:endpoint>", methods=['POST'])
# Cross origin allows api calls to be made to this route
@cross_origin(supports_credentials=True)
def upload_file(endpoint):
    #TODO 2: Create route to save images into the images folder
    # This returns a message of the status of the save
    if endpoint == 'save':
        if request.method == 'POST':
            #Check if the post request has the file part
            if 'file' not in request.files:
                print('No file part')
                return jsonify({'message': 'No file part'})
            file = request.files['file']
            # If the user does not select a file, the browser submits
            # an empty file without a filename
            if file.filename == '':
                print('no selected file')
                return jsonify({'message': 'No selected file'})
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(images_folder, filename))
                return jsonify({'message': 'Image saved!'})
    #TODO 1: Create route to load image into face folder,
    # blur images where the face appears from the images folder,
    # and then returns the blurred images as a file.
    # The image sent should be removed from the folder after the operation
    if endpoint == 'find':
        if request.method == 'POST':
            if 'file' not in request.files:
                return jsonify({'message': 'No file part'})
            file = request.files['file']
            if file.filename == '':
                return jsonify({'message': 'No selected file'})
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(face_folder, filename))
                # Match and blur the face the user sent from the 
                # images folder
                RecognizeFace(img=f'{face_folder}/{filename}', folder=images_folder)
                stream = BytesIO()
                with ZipFile(stream, 'w') as zf:
                    for file in images_folder:
                        print(f"file: {file}")
                        #Checks if the file is a blurred
                        if file.split('_')[0] == 'blur':
                            zf.write(file, os.path.basename(file))
                            # Deletes the file after writing it to the zipfile
                            os.remove(file)
                stream.seek(0)
                return send_file(stream,
                                 as_attachment=True,
                                 download_name='blurred images')
                

                
                            



if __name__ == '__main__':
    app.run(port=port, debug=True)