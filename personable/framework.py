# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.30.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
import json
import os
import sys
import logging

from flask import Flask

from personable.api.version_0_0_1.controllers.main import app_v0_0_1


# Framework globals
# -----------------------------------------------------
flask_app = None
current_app = app_v0_0_1


# Helper functions
# -----------------------------------------------------
def setup_logger(config):
    # TODO - create app logger
    logger = None
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.setLevel(logging.ERROR)

    return logger

def create_flask_app(config):
    db_name = config['db_name']
    db_path = os.path.join(config['app_path'], 'db', db_name)
    db_connect_str = 'sqlite:///db/{}'.format(db_path)

    flask_app = Flask(__name__)
    flask_app.secret_key                                = 'TTS96tKYthZh2V2jO7Bwi1c4BO0BFYfe8YnDegkg'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
    flask_app.config['SQLALCHEMY_DATABASE_URI']         = db_connect_str
    flask_app.config['DB_NAME']                         = db_name
    return flask_app

def register_versions(flask_app):
    # flask_app.register_blueprint(app_v0_0_1, url_prefix='/v0_0_1')
    flask_app.register_blueprint(current_app)

def load_data(config, db):
    app_path = config['app_path']
    db_name = config['db_name']
    db_path = os.path.join(app_path, 'db', db_name)
    reset_db(db_path, db)

    return db_path

def reset_db(db_path, db):
    try:
        os.remove(db_path)
    except OSError:
        pass

    touch(db_path)
    from frigg.db.models.person import Person
    db.create_all()
    db.session.commit()

def load_fixtures():
    data_path = os.path.join(app_path, 'db', 'fixtures', 'data.csv')

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)
