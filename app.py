from flask import Flask, render_template, redirect, abort, send_file
from flaskext.markdown import Markdown
import os.path
from config import config


app = Flask(__name__)
Markdown(app)

site_title=config['site_title']
site_all_notification=config['site_all_notification']
footer='<small class="m-0 text-center text-white">'+config['footer_text']+'</small>'
root_directory=config['root_directory']
analytics=config['analytics']
seo_author=config['seo_author']
seo_description=config['seo_description']


@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/pages/errors/404'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def redirect_index():
    return redirect('/pages/home')

@app.route('/pages/<path:request_path>')
def render_markdown(request_path):
    path=root_directory+'/markdown/'+request_path+'.md'
    check = os.path.isfile(path)
    if check == False:
        abort(404)
    with open(path, 'r') as markdown_file:
        md = markdown_file.read()
        markdown_file.close()
    return render_template('main_bootstrap_frame.html', md=md,site_all_notification=site_all_notification,site_title=site_title,footer=footer,seo_author=seo_author,seo_description=seo_description)

@app.route('/downloads/<path:file_path>')
def send_a_file(file_path):
    file_path=root_directory+'/documents/'+file_path
    return send_file(file_path)