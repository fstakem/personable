# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.12.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from login_attempt import LoginAttempt
from personable.database import acl_db as db


def attempt_login(self, person):
    login = LoginAttempt()
    login.successful = True
    person.login_attempts.append(login)

    db.session.add(person)
    db.session.add(login)
    db.session.commit()
