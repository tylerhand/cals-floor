# CALS Floor Website
This is the repository for the CALS Floor Website [\(which can be viewed here\)](www.calsfloor.info). It is hosted on Pythonanywhere.
Feel free to use this for your own floor.

## How to Set Up on Pythonanywhere...
First, you will need a [Pythonanywhere Account](https://www.pythonanywhere.com). You can create one free website at your_username.pythonanywhere.com or
have a website with your own domain for $5/month \(a premium account also gives you unlimited consoles, ssh access and no whitelist restrictions. Also,
on a free account, you get only one web worker, low bandwidth and no iPython notebooks. If you are using a free account, I am not sure if you can use
git clone due to no secure ssh...if so, you will have to manually copy the app.py and other files.\) <br><br>
First, open a BASH console and imput the following command...

    git clone https://github.com/tylerhand/cals-floor

This app runs on Flask with Flask-Markdown as a dependancy. You need to create a virtual environment and enter this list of commands...

    mkvirtualenvwrapper Flask-Cals-Floor --python-/usr/bin/python3.7
    cd cals-floor
    pip install -r requirements.txt


Now, create a new web app and choose "manual configuration". Next, go to your WSGI \(there is a link on the web tab\) and replace the contents with the
following code. Replace <myusername> with your Pythonanywhere username.

    import sys
    project_home = u'/home/<myusername>/cals-floor/'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path
    from app import app as application  # noqa

Next, scroll down on the web tab to the static file mappings and add a mapping with URL: /static/ and Directory: /home/insert_username/cals-floor/static<br>
It would also be a good idea to create an SSL certificate and enforce HTTPS.

**Lastly, make sure you customize the configuration settings at the top of the app.py file! Change the root directory to /home/tylerhand/cals-floor. The analytics variable is for Google Analytics. If you do not plan to use it, just change this to "None"**


Now, reload the web app for these changes to take effect and navigate to the site to test it.