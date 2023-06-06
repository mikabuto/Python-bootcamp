import os
from flask import Flask, render_template, make_response, request
from flask_uploads import UploadSet, configure_uploads, patch_request_class, AUDIO
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
 
basedir = os.path.abspath(os.path.dirname(__file__))
 
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_FILES_DEST'] = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOADS_DEFAULT_DEST'] = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_EXTENSIONS'] = ['.mp3', '.ogg', '.wav']
 
file_urls = []
 
medias = UploadSet('media', AUDIO)
configure_uploads(app, medias)
patch_request_class(app)

class UploadForm(FlaskForm):
    media = FileField(validators=[FileAllowed(medias, 'Non-audio file detected'),
                                  FileRequired('File was empty!')])
    submit = SubmitField('Upload')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global file_urls
    form = UploadForm()
    if form.validate_on_submit():
        filename = medias.save(form.media.data)
        file_urls.append((medias.url(filename), os.path.basename(filename)))
    resp = make_response(render_template("""index.html""", form=form, file_urls=file_urls))
    resp.delete_cookie('session')
    return resp

@app.route('/list', methods=['GET'])
def get_list():
    global file_urls
    return make_response("</br>".join([file[1] for file in file_urls]))

@app.route('/post', methods=['POST'])
def post_file():
    global file_urls
    form = UploadForm()
    filename = medias.save(form.media.data)
    file_urls.append((medias.url(filename), os.path.basename(filename)))
    resp = make_response("<p>Upload Successfully</p>")
    resp.delete_cookie('session')
    return resp

def prepare_file_urls():
    global file_urls
    base_dir = os.path.join(os.getcwd(), 'uploads', 'media')
    file_urls = [(os.path.join(base_dir, file), os.path.basename(file)) for file in os.listdir(base_dir)]

if __name__ == '__main__':
    prepare_file_urls()
    app.run(port=8888)