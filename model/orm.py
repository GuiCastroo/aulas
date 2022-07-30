from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Lojista(db.Model):
    __tablename__ = 'lojistas'
    id = db.Column(db.String(300), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    document = db.Column(db.String(255))
