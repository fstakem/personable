# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.30.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os
import time
from datetime import datetime
import random

from flask import request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

from personable.framework import setup_logger, create_flask_app
from personable.framework import register_versions, load_data

from config.config import load_config


# Config
config      = load_config()
logger      = setup_logger(config)
flask_app   = create_flask_app(config)
db          = SQLAlchemy(flask_app)
_           = register_versions(flask_app)



# Globals
# -----------------------------------------------------



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
    return load_data(flask_app, db)


# Helper functions
# -----------------------------------------------------

