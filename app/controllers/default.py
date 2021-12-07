from app import app, db
from app.models.tables import Folder
from config import UPLOAD_FOLDER

import os
from flask import render_template, request
from werkzeug.utils import secure_filename

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return 'Upload feito com sucesso !'