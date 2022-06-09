from distutils.log import debug
import os
from flask import Flask, jsonify, make_response, render_template, request, send_file, send_from_directory
from dotenv import load_dotenv
from recognize_face import RecognizeFace
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import time
# This allows for streaming bytes from a file
from io import BytesIO


"""This is the endpoint that the react app would make requests to"""
load_dotenv()
port = os.getenv('PORT')
images_folder = os.getenv('IMAGES')
face_folder = os.getenv('FACE')
zip_file = os.getenv('ZIP')
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg']

if images_folder not in os.listdir(os.curdir) and face_folder not in os.listdir(os.curdir):
    os.mkdir(images_folder)
    os.mkdir(face_folder)
    

def allowed_file(filename):
    if '.' in filename and filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

app = Flask(__name__, static_folder='client/build', static_url_path='/')
CORS(app, supports_credentials=True)


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


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
                print('No file part')
                return jsonify({'message': 'No file part'})
            file = request.files['file']
            if file.filename == '':
                print('no selected file')
                return jsonify({'message': 'No selected file'})
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(face_folder, filename))
                # Match and blur the face the user sent from the 
                # images folder
                RecognizeFace(img=f'{face_folder}/{filename}', folder=images_folder)
                os.remove(os.path.join(face_folder, filename))
                # Creates/Open zip file for writing
                with ZipFile(zip_file, 'w') as my_zip:
                    # Writes the blurred images into the zip folder
                    # and removes them from the images folder
                    for filename in os.listdir(images_folder):
                        if filename.split("_")[0] == 'blur':
                            file = os.path.join(images_folder, filename)
                            my_zip.write(file)
                            os.remove(file)
                to_send = os.path.join(zip_file)
                return send_file(to_send, as_attachment=True, download_name='Images')            

if __name__ == '__main__':
    app.run(debug=True)