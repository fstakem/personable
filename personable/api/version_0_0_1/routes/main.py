# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.30.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask import Blueprint, render_template, abort
from flask_restful import Api, Resource, url_for
from jinja2 import TemplateNotFound

from personable.api.version_0_0_1.routes.person import Person, PersonList
from personable.api.version_0_0_1.routes.auth_device import AuthDevice, AuthDeviceList
from personable.api.version_0_0_1.routes.login_device import LoginDevice, LoginDeviceList
from personable.api.version_0_0_1.routes.login_attempt import LoginAttempt, LoginAttemptList

from personable.api.version_0_0_1.forms.login_form import LoginForm
from personable.api.version_0_0_1.forms.register_form import RegisterForm


version_value = '0_0_1'
version_name = 'app_v' + version_value

app_v0_0_1 = Blueprint(version_name, version_name, 
    static_folder='personable/api/version_0_0_1/static', 
    static_url_path='',
    template_folder='personable/api/version_0_0_1/templates')


# Web routes
@app_v0_0_1.route('/')
def version_hello():
    return 'v0.0.1'

@app_v0_0_1.route('/<user>')
def user(user):
    try:
        return render_template('user_home.html', user=user)
    except TemplateNotFound:
        abort(404)
    
@app_v0_0_1.route('/index')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@app_v0_0_1.route('/login', methods=('GET', 'POST'))
def login():
    try:
        form = LoginForm()
        if form.validate_on_submit():
            return redirect('/')

        return render_template('login.html', form=form)
    except TemplateNotFound:
        abort(404)

@app_v0_0_1.route('/register', methods=('GET', 'POST'))
def register():
    try:
        form = RegisterForm()
        if form.validate_on_submit():
            return redirect('/')

        return render_template('register.html', form=form)
    except TemplateNotFound:
        abort(404)

@app_v0_0_1.route('/register_device')
def register_device():
    try:
        return render_template('register_device.html')
    except TemplateNotFound:
        abort(404)

rest_api = Api(app_v0_0_1)


# Basic restful routes
rest_api.add_resource(Person, '/person/<int:id>')
rest_api.add_resource(PersonList, '/person/all')
rest_api.add_resource(AuthDevice, '/auth_device/<int:id>')
rest_api.add_resource(AuthDeviceList, '/auth_device/all')
rest_api.add_resource(LoginDevice, '/login_device/<int:id>')
rest_api.add_resource(LoginDeviceList, '/login_device/all')
rest_api.add_resource(LoginAttempt, '/login_attempt/<int:id>')
rest_api.add_resource(LoginAttemptList, '/login_attempt/all')




