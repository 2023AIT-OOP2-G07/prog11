from flask import Blueprint, render_template
import os,sys
list_page = Blueprint('list_page', __name__)

@list_page.route('/upload_show')
def list_show():
    os.listdir('static/images/upload')
    return render_template('list_page.html')

