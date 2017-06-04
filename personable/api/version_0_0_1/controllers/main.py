# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.30.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask import Blueprint, render_template, abort, request, redirect
from flask import current_app
from flask_restful import Api, Resource, url_for
from jinja2 import TemplateNotFound

from personable.api.version_0_0_1.controllers.person import Person as PersonController
from personable.api.version_0_0_1.controllers.person import PersonList as PersonListController
from personable.api.version_0_0_1.controllers.auth_device import AuthDevice as AuthDeviceController
from personable.api.version_0_0_1.controllers.auth_device import AuthDeviceList as AuthDeviceListController
from personable.api.version_0_0_1.controllers.login_device import LoginDevice as LoginDeviceController
from personable.api.version_0_0_1.controllers.login_device import LoginDeviceList as LoginDeviceListController
from personable.api.version_0_0_1.controllers.login_attempt import LoginAttempt as LoginAttemptController
from personable.api.version_0_0_1.controllers.login_attempt import LoginAttemptList as LoginAttemptListController

from personable.api.version_0_0_1.forms.login_form import LoginForm
from personable.api.version_0_0_1.forms.register_form import RegisterForm

from personable.db.models.person import Person


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
    return render_template('user_home.html', user=user)
    
@app_v0_0_1.route('/index')
def index():
    return render_template('index.html')

@app_v0_0_1.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)

    #p = Person.query.filter_by(username='fred').first()
    #print(p)

    if request.method == 'POST' and form.validate():
        person = Person()

        return redirect('/index')

    return render_template('login.html', form=form)

@app_v0_0_1.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        return redirect('/index')

    return render_template('register.html', form=form)

@app_v0_0_1.route('/register_device')
def register_device():
    return render_template('register_device.html')

rest_api = Api(app_v0_0_1)


# Basic restful routes
rest_api.add_resource(PersonController, '/person/<int:id>')
rest_api.add_resource(PersonListController, '/person/all')
rest_api.add_resource(AuthDeviceController, '/auth_device/<int:id>')
rest_api.add_resource(AuthDeviceListController, '/auth_device/all')
rest_api.add_resource(LoginDeviceController, '/login_device/<int:id>')
rest_api.add_resource(LoginDeviceListController, '/login_device/all')
rest_api.add_resource(LoginAttemptController, '/login_attempt/<int:id>')
rest_api.add_resource(LoginAttemptListController, '/login_attempt/all')




