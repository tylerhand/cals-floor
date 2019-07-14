from flask import Flask, render_template, redirect, abort, send_file
from flaskext.markdown import Markdown
import os.path


app = Flask(__name__)
Markdown(app)

site_all_notification='Welcome, this site is still being worked on. It should be complete sometime in August.'

root_directory='/home/tylerhand/www.calsfloor.info/'
analytics='''

'''

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/pages/errors/404'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return redirect('/pages/errors/500'), 500

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
    return render_template('main_bootstrap_frame.html', md=md,site_all_notification=site_all_notification)

@app.route('/downloads/<path:file_path>')
def send_a_file(file_path):
    file_path=root_directory+'/documents/'+file_path
    return send_file(file_path)

