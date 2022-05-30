import os
from flask import Flask
from dotenv import load_dotenv

"""This is the endpoint that the react app would make requests to"""
load_dotenv()
port = os.getenv('PORT')

app = Flask(__name__)

#TODO 1: Create route to load image into face folder,
# blur images where the face appears from the images folder,
# and then returns the blurred images as a file.
# The image sent should be removed from the folder after the operation


#TODO 2: Create route to load images into the images folder
# This returns a message of the status of the save



if __name__ == '__main__':
    app.run(port=port, debug=True)