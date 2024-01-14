import os
from flask import Flask, flash, request, redirect, url_for
from image_processing import calculate_humans
from files_operations import download_image, cleanup_memory, allowed_file
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/endpoint1')
def endpoint1():
    number_of_people = calculate_humans("zdjecie.png")
    return '<h1>Number of people on the photo: ' + str(number_of_people) + '</h2>'


@app.route('/endpoint2')
def endpoint2():
    image_link = request.args.get('image-link')
    download_path = download_image(image_link)
    number_of_people = calculate_humans(download_path)
    cleanup_memory(download_path)
    return '<h1>Number of people on the downloaded photo: ' + str(number_of_people) + '</h2>'


@app.route('/endpoint3', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            number_of_people = calculate_humans(filename)
            cleanup_memory(filename)
            return '<h1>Number of people on the uploaded photo: ' + str(number_of_people) + '</h2>'

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)
