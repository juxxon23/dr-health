from db.postgresql.model import db
from sqlalchemy.exc import SQLAlchemyError


class PostgresqlManager:
    def add(self, *args):
        try:
            for new in args:
                db.session.add(new)
                db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'

    def update(self):
        try:
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'

    def delete(self, obj):
        try:
            db.session.delete(obj)
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'

    def get_all(self, table_name):
        try:
            data = db.session.query(table_name).all()
            return data
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'
