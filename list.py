from flask import Blueprint, render_template
import os
list_page = Blueprint('list_page', __name__)


@list_page.route('/upload_show')
def list_show():
    file_names = [i for i in os.listdir('./static/images/upload') if i[0] != '.']
    
    
    return render_template('list_page.html')
