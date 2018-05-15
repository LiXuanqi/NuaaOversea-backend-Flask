from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    college = db.Column(db.String(30))
    major = db.Column(db.String(30))
    gpa = db.Column(db.Float('2,1'))
    language_type = db.Column(db.Enum('TOEFL', 'IELTS'))
    language_reading = db.Column(db.Integer)
    language_listening = db.Column(db.Integer)
    language_speaking = db.Column(db.Integer)
    language_writing = db.Column(db.Integer)
    gre_verbal = db.Column(db.Integer)
    gre_quantitative = db.Column(db.Integer)
    gre_writing = db.Column(db.Float('2,1'))
    research_id = db.Column(db.Integer, db.ForeignKey('research.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    recommendation_id = db.Column(db.Integer, db.ForeignKey('recommendation.id'), nullable=False)
    applications = db.relationship('Application', backref='applicant', lazy='dynamic')
    user_id = db.relationship('User', backref='applicant', uselist=False)
    def __repr__(self):
        return '<Applicant {}>'.format(self.username)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    university = db.Column(db.String(64))
    major = db.Column(db.String(64))
    degree = db.Column(db.Enum('Master', 'Ph.D'))
    term = db.Column(db.String(64))
    result = db.Column(db.Enum('ad', 'offer', 'rej'))
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    tags = db.relationship(
        "Tag",
        secondary=db.Table(
            'application_tag',
            db.Model.metadata,
            db.Column("application_id", db.Integer, db.ForeignKey('application.id'), primary_key=True),
            db.Column("tag_id", db.Integer, db.ForeignKey('tag.id'), primary_key=True)
        ),
        backref="applications"
    )
    def __repr__(self):
        return '<Application #{}>'.format(self.id)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True, index=True, nullable=False)
    password = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=True)
    role = db.Column(db.Enum('root', 'admin', 'stuff', 'student'))
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'))
    login_time = db.Column(db.Integer)
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    def __repr__(self):
        return '<Account {}>'.format(self.username)
    def set_password(self, password):
        return generate_password_hash(password)
    def check_password(self, hash, password):
        return check_password_hash(hash, password)
    def get(self, id):
        return self.query.filter_by(id=id).first()
    def add(self, user):
        db.session.add(user)
        return session_commit()
    def update(self):
        return session_commit()

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    applications = db.relationship('Application', backref='country', lazy='dynamic')

class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    applicants = db.relationship('Applicant', backref='research', lazy='dynamic')
    value = db.Column(db.Integer)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    applicants = db.relationship('Applicant', backref='project', lazy='dynamic')
    value = db.Column(db.Integer)

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    applicants = db.relationship('Applicant', backref='recommendation', lazy='dynamic')
    value = db.Column(db.Integer)

def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason