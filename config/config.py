# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.6.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os
import json
from os.path import dirname, abspath


def load_config():
    env = os.environ['ENV'].lower()
    config_dir_path = dirname(abspath(__file__))
    config_file = env + '.json'
    config_path = os.path.join(config_dir_path, config_file)
    assert os.path.isfile(config_path)

    with open(config_path) as config_data:    
        config = json.load(config_data)

    # ======== Transform the config file
    config['env'] = env
    add_path(config)
    add_db_connection_str(config)

    return config

def add_path(config):
    project_path = dirname(dirname(abspath(__file__)))
    config['project_path'] = project_path
    config['app_path'] = os.path.join(project_path, config['app_name'])

def add_db_connection_str(config):
    db_path = os.path.join(config['app_path'], 'db', config['db_name'])
    db_connect_str = 'sqlite:///{}'.format(db_path)
    config['db_connect_str'] = db_connect_str