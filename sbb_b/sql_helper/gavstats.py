from sqlalchemy import Column, String, delete
from sqlalchemy.orm.exc import NoResultFound

from . import BASE, SESSION


class gavestaus(BASE):
    __tablename__ = "gavstats"
    groupez = Column(String, primary_key=True)

    def __init__(self, groupez):
        self.groupez = str(groupez)


gavestaus.__table__.create(checkfirst=True)


def addvar(groupez):
    try:
        if SESSION.query(gavestaus).one():
            del_addvar()
    except NoResultFound:
        pass
    user = gavestaus(groupez)
    SESSION.add(user)
    SESSION.commit()
    SESSION.close()
    return True


def del_addvar():
    to_check = get_addvar()
    if not to_check:
        return False
    abne = delete(gavestaus)
    SESSION.execute(abne)
    SESSION.commit()
    return abne


def get_addvar():
    try:
        if _result := SESSION.query(gavestaus).one().groupez:
            return _result
    except NoResultFound:
        return None
    finally:
        SESSION.close()
