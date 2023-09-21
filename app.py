from flask import Flask, request, render_template
import pandas as pd
from app2 import predict_plant
from werkzeug.utils import secure_filename
import os


# Declare a Flask app
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}



# Function to check if a filename has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('website.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    '''# If the user does not select a file, the browser submits an empty part without a filename.
    if file.filename == '':
        return "No selected file"'''

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        print(file_path)
        file_path=file_path.replace("\\","/")
        return predict_plant(file_path)




if __name__ == '__main__':
    app.run(debug=True)
