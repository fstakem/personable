from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
db_config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(db_config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from personable.database import acl_db
target_metadata = acl_db.metadata

# Do you need to import models here?
from personable.db.models.person import Person
from personable.db.models.auth_device import AuthDevice
from personable.db.models.login_device import LoginDevice
from personable.db.models.login_attempt import LoginAttempt

# DB connection str
from personable.personable import app_config
print(app_config)
print(app_config['db_connect_str'])
db_config.set_main_option('sqlalchemy.url', app_config['db_connect_str'])
print(db_config)


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(url=db_connect_str, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        db_config.get_section(db_config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
