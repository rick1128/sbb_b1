from sqlalchemy import Column, String, delete
from sqlalchemy.orm.exc import NoResultFound
from . import BASE, SESSION

class grism(BASE):
    __tablename__ = "autogrpe"
    agroup = Column(String, primary_key=True)

    def __init__(self, agroup):
        self.agroup = str(agroup)


grism.__table__.create(checkfirst=True)


def autogroup(
    agroup,
):
    try:
        if SESSION.query(grism).one():
            del_autogroup()
    except NoResultFound:
        pass
    user = grism(agroup)
    SESSION.add(user)
    SESSION.commit()
    SESSION.close()
    return True

def del_autogroup():   
    to_check = get_autogroup()
    if not to_check:
        return False
    stmt = delete(grism)
    SESSION.execute(stmt)
    SESSION.commit()
    #SESSION.close()
    return stmt

def get_autogroup():
    try:
        if _result := SESSION.query(grism).one().agroup:
            return _result
    except NoResultFound:
        return None
    finally:
        SESSION.close()
