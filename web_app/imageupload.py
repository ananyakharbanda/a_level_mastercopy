
import flask 
import os
from flask import render_template, redirect, request, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)

@app.route('/home/', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'GET':
        return render_template("imageupload.html")
    else:
        photo = request.files["imagefile"]
        s_filename = secure_filename(photo.filename)
        path_tosave = os.path.join('/Users/ananya/a_level_mastercopy/web_app/uploads', s_filename)
        photo.save(path_tosave)
        return 'got file ' + str(photo.filename)      


@app.route('/view/', methods=['GET', 'POST'])
def viewall():
    only_files = [x for x in os.listdir('/Users/ananya/a_level_mastercopy/web_app/uploads') if os.path.isfile(os.path.join('/Users/ananya/a_level_mastercopy/web_app/uploads', x))]
    print(only_files)
    for afile in only_files:
        return send_from_directory('/Users/ananya/a_level_mastercopy/web_app/uploads', afile)

if __name__ == '__main__':
    app.run()