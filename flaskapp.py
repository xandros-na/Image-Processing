import os
from flask import Flask, request, flash, url_for, redirect, \
    render_template, abort, send_from_directory, abort
from werkzeug import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from filters import get_matrix, apply_kernel, produce_output
from ImageFile import ImageFile
from thinning import zs_thin
from features import feature_histogram, trim, zoning_method
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

ALLOWED_EXTENSIONS = set(['bmp'])

app = Flask(__name__)
run_config = 'dev'
app.config.from_pyfile('flaskapp.cfg')
app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'img')
app.config['MAX_CONTENT_LENGTH'] = 0.5 * 1024 * 1024
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
import models

db.init_app(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/image/<filename>')
def image(filename):
    if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        return render_template('index.html', filename=filename)
    else:
        return abort(404)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            try:
                filename = ImageFile.time_stamp() + secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                file.close()
                return redirect(url_for('image', filename=filename))
            except RequestEntityTooLarge as e:
                flash('data too large')
                return redirect(url_for('upload'))
        else:
            flash('File extension not allowed. Only .bmp files are supported')

    return render_template('index.html')


def convert(n):
    try:
        float(n)
        return float(n)
    except ValueError as v:
        return False


def parse(k):
    if '/' in k:
        fraction = k.split("/")
        numer = convert(fraction[0])
        denom = convert(fraction[1])
        if numer and denom:
            return numer / denom
        else:
            return False
    else:
        n = convert(k)
        return n


def move_file(new_file):
    os.rename(new_file, os.path.join(app.config['UPLOAD_FOLDER'], new_file))
    return


@app.route('/filter', methods=['POST'])
def filter():
    kernel = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    counter = 0
    filename = request.form['filename']

    for k in range(len(kernel)):
        for j in range(len(kernel)):
            n = parse(request.form['k' + str(counter)])
            if n is not False:
                kernel[k][j] = n
                counter += 1
            else:
                flash("Bad kernel value")
                return render_template('index.html', filename=filename)

    img = ImageFile(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    output = produce_output(kernel, img)
    new_file = img.save_img(output, filename)
    move_file(new_file)
    return render_template('index.html', filename=filename, new_file=new_file)


@app.route('/thinning', methods=['POST'])
def thinning():
    filename = request.form['filename']
    img = ImageFile(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    output = zs_thin(img)
    new_file = img.save_img(output, filename, thinning=True)
    move_file(new_file)
    return render_template('index.html', filename=filename, new_file=new_file)


@app.route('/histogram', methods=['POST'])
def histogram():
    filename = request.form['filename']
    img = ImageFile(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    trimmed = trim(img)
    img_vector = feature_histogram(trimmed)
    return render_template('index.html', filename=filename, img_vector=img_vector)


@app.route('/zoning', methods=['POST'])
def zoning():
    filename = request.form['filename']
    img = ImageFile(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    trimmed = trim(img)
    img_vector = zoning_method(trimmed)
    return render_template('index.html', filename=filename, img_vector=img_vector)


@app.route('/test/add/', methods=['GET'])
def db_test():
    s = models.Symbol(name="test")
    v = models.V1(histogram_value=0.99, number=s)
    db.session.add(s)
    db.session.add(v)
    db.session.commit()
    return '<h1> Done </h1>'


@app.route('/test/get/', methods=['GET'])
def db_get():
    all_sym = models.Symbol.query.all()
    return '<h1>' + all_sym[0].name + '</h1>'


@app.route('/recognize', methods=['POST'])
def recognize():
    filename = request.form['filename']
    img = ImageFile(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    trimmed = trim(img)
    img_vector = zoning_method(trimmed)
    symbols = models.Symbol.query.all()
    min_int = 0
    min_index = 0

    for j, symbol in enumerate(symbols):
        c = 0
        duplicate = False
        for i, v in enumerate(img_vector):
            data = list(symbol.v1s[j], symbol.v2s[j], symbol.v3s[j], symbol.v4s[j], symbol.v5s[j], symbol.v6s[j], \
                        symbol.v7s[j], symbol.v8s[j], symbol.v9s[j], symbol.v10s[j], symbol.v11s[j], symbol.v12s[j], \
                        symbol.v13s[j], symbol.v14s[j], symbol.v15s[j], symbol.v16s[j])
            c += abs(v - data[i])

        if c == min_int:
            duplicate = True
        elif c < min_int:
            min_int = c
            min_index = j
            duplicate = False

    if duplicate:
        min_index = "Cant tell"
    return render_template('index.html', filename=filename, number=min_index)


if __name__ == '__main__':
    manager.run()
