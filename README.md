# Face Blur: React & Flask Application

## Overview
Face Blur is a full-stack application that allows users to send an image either to detect faces for blurring from a set of saved images or to add an image to the saved list. The client is built with React and the server is built with Flask. The server leverages Python libraries like OpenCV and face_recognition to perform image processing.

## Features
- **Face Recognition:** Identify and match faces across images.
- **Image Processing:** Apply pixelated blur to regions containing detected faces.
- **Dynamic UI:** Toggle between uploading a reference face or an image for processing.
- **Environment Configurable:** Setup folders and image paths through environment variables.

## Technologies Used
- **Frontend:** React, TypeScript
- **Backend:** Python, Flask
- **Image Processing:** OpenCV, face_recognition, numpy
- **Dependency Management:** npm for client and pip for server

## Installation

### Prerequisites
- Node.js & npm
- Python 3.x
- pip

### Client Setup
1. Navigate to the client directory:
    - `cd client`
2. Install dependencies:
    - `npm install`
3. Start the development server:
    - `npm start`

### Server Setup
1. Navigate to the project root.
2. Create a virtual environment and activate it:
    - `python -m venv venv`
    - Windows: `venv\Scripts\activate`
3. Install required Python packages:
    - `pip install -r requirements.txt`  
      *(If no requirements file exists, install: opencv-python, numpy, face-recognition, python-dotenv)*
4. Set up environment variables by creating a `.env` file in the project root:
    ```
    IMAGES=images
    FACE=face
    ZIP-zip
    ```
5. Start the Flask server:
    - `flask run`

## Folder Structure
```
/C:/[...]/[...]/[...]/Face-Recognition
├── client/                # React frontend source code
│   └── src/
│       └── components/
│           └── App.tsx  # Main React component
├── api/                   # API related documentation
│   └── README.md
├── face_blur.py           # Python module to blur faces in images
├── recognize_face.py      # Python module to recognize and match faces
├── README.md              # Project documentation
└── .env                   # Environment configuration file
```

## Usage
- **Uploading an Image to Process:**  
  Use the client interface to select the mode (`/find` for blur search, `/save` for adding a new reference image).  
- **Server Operation:**  
  When an image is uploaded, the server processes it by detecting faces. Matching faces found in the configured image folder are blurred using the `BlurFace` module.

## Troubleshooting
- **Invalid Coordinates:**  
  Ensure the face detection returns proper coordinates. The `BlurFace` module will print a message if coordinates are invalid.
- **Environment Variables:**  
  Verify that the `.env` file exists and that `IMAGES`, `FACE` and `ZIP` are correctly set.

## Contributing
Feel free to contribute by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License.
