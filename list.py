from flask import Blueprint, render_template
import os
list_page = Blueprint('list_page', __name__)


@list_page.route('/upload_show')
def img_list():
    img_dir = 'static/images/upload'
    file_names = [i for i in os.listdir(img_dir) if i[0] != '.']
    return render_template('list_page.html', file_names=file_names)
