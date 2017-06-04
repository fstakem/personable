# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.30.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os
import logging

from flask import request, url_for, jsonify, Flask

from personable.database import acl_db
from config.config import load_config
from personable.api.version_0_0_1.controllers.main import app_v0_0_1


# Framework globals
# -----------------------------------------------------
flask_app = None
current_app = app_v0_0_1


# Config
config          = load_config()

# Logger
logger          = None
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.ERROR)

# DB info
db_name         = config['db_name']
db_path         = os.path.join(config['app_path'], 'db', 'data', db_name)
db_connect_str  = 'sqlite:///db/{}'.format(db_path)

# App
flask_app = Flask(__name__)
flask_app.secret_key                                = 'TTS96tKYthZh2V2jO7Bwi1c4BO0BFYfe8YnDegkg'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
flask_app.config['SQLALCHEMY_DATABASE_URI']         = db_connect_str
flask_app.config['DB_NAME']                         = db_name
flask_app.register_blueprint(current_app)

# Init DB
acl_db.init_app(flask_app)


# App code
# -----------------------------------------------------
@flask_app.route('/')
def root():
    return 'Root page'

@flask_app.route('/version')
def version():
    return config['version']

@flask_app.route('/reload_db')
def reload_db():
    return load_data(flask_app, alc_db)
