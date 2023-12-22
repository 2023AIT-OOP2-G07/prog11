from flask import Blueprint, render_template
import os

list_page = Blueprint('list_page', __name__)


def render_template_img_list(img_dir: str) -> str:
    """
    'static/images' フォルダの中にある 'img_dir' ディレクトリ内にある画像を抽出しテンプレートを生成する関数
    """
    props = {"img_dir": img_dir}
    image_path = 'static/images/' + img_dir
    props["file_names"] = [i for i in os.listdir(image_path) if i[0] != '.']
    props["empty_img"] = not props["file_names"]

    print(props)
    return render_template('list_page.html', **props)


@list_page.route('/upload_list')
def upload_list():
    """
    static/images/upload に配置されている画像ファイルを読み込みテンプレート生成
    """
    return render_template_img_list('upload')


@list_page.route('/gray_list')
def gray_list():
    """
    static/images/gray に配置されている画像ファイルを読み込みテンプレート生成
    """
    return render_template_img_list('gray')
