from sqlalchemy import Column, String, delete
from sqlalchemy.orm.exc import NoResultFound
from . import BASE, SESSION

class gavestaus(BASE):
    __tablename__ = "gavstats"
    jasem = Column(String, primary_key=True)

    def __init__(self, jasem):
        self.jasem = str(jasem)


gavestaus.__table__.create(checkfirst=True)


def addvar(jasem):
    try:
        if SESSION.query(gavestaus).one():
            del_addvar()
    except NoResultFound:
        pass
    user = gavestaus(jasem)
    SESSION.add(user)
    SESSION.commit()
    SESSION.close()
    return True

def del_addvar():   
    to_check = get_addvar()
    if not to_check:
        return False
    adder = delete(gavestaus)
    SESSION.execute(adder)
    SESSION.commit()
    return adder

def get_addvar():
    try:
        if _result := SESSION.query(gavestaus).one().jasem:
            return _result
    except NoResultFound:
        return None
    finally:
        SESSION.close()
