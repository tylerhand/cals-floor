from flask import Flask, render_template, redirect, abort, send_file, request
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
admin_password=config['admin_password']
mail_password=config['mail_password']
list_moderators=config['list_moderators']
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

@app.route('/mailing-list/')
def mailing_list_index():
    return render_template('coming-soon.html')

@app.route('/staff/')
def staff_index():
    site_title='Staff Pages - CALS Floor'
    return render_template('staff-index.html',site_title=site_title)

@app.route('/staff/interactions', methods=['GET','POST'])
def staff_interactions():
    page_header='Interaction Logs'
    interactions_options=['August','September','October']
    error=None
    title='Interactions - CALS Floor'
    ico_title='''
    <link rel="icon" href="/static/uidaho.ico" type="image/x-icon"/>
    <link rel="shortcut icon" href="/static/uidaho.ico" type="image/x-icon"/>
    <title>'''+title+'''</title>'''
    if request.method == 'POST':
        choice=request.form['choice']
        if choice not in interactions_options:
            error='That is not a valid selection, please try again'
            return render_template('staff-pages-request.html',ico_title=ico_title,interactions_options=interactions_options,page_header=page_header,error=error)
        if request.form['password'] == admin_password:
            template_path='interactions/'+choice+'.html'
            title='Interactions - Month of '+choice
            ico_title='''
            <link rel="icon" href="/static/uidaho.ico" type="image/x-icon"/>
            <link rel="shortcut icon" href="/static/uidaho.ico" type="image/x-icon"/>
            <title>'''+title+'''</title>'''
            return render_template(template_path,ico_title=ico_title)
        else:
            error='Invalid password, please try again.'
    return render_template('staff-pages-request.html',ico_title=ico_title,interactions_options=interactions_options,page_header=page_header,error=error)

@app.route('/staff/mailing-list', methods=['GET','POST'])
def staff_mailing_list():
    import mailgun
    site_title='Staff Pages - CALS Floor'
    return render_template('staff-mailing-list.html',site_title=site_title,list_moderators=list_moderators)

@app.route('/staff/mailing-list/help')
def staff_mailing_list_docs():
    site_title='Staff Pages - CALS Floor'
    return render_template('staff-list-usage.html',site_title=site_title)

@app.route('/staff/roster', methods=['GET','POST'])
def staff_roster():
    site_title='Staff Pages - CALS Floor'
    page_header='Floor Roster (for the most current version, contact the Housing Office)'
    error=None
    _title='CALS Floor Roster'
    ico_title='''
    <link rel="icon" href="/static/uidaho.ico" type="image/x-icon"/>
    <link rel="shortcut icon" href="/static/uidaho.ico" type="image/x-icon"/>
    <title>'''+_title+'''</title>'''
    if request.method == 'POST':
        if request.form['password'] == admin_password:
            return render_template('roster/roster.html',site_title=site_title,ico_title=ico_title)
        else:
            error='Invalid password, please try again.'
    return render_template('staff-pages-request.html',site_title=site_title,page_header=page_header,error=error)
