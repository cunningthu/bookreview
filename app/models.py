from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    review_count = db.Column(db.Integer, nullable=False)
    avg_score = db.Column(db.Float, nullable=False)
    reviews = db.relationship("Review", backref="book", lazy=True)

    def __repr__(self):
        return '<Book {}>'.format(self.title)

    def add_review(self, rating, title, review, username, source):
        r = Review(rating=rating, title=title, review=review, username=username, source=source, review_id=self.id)
        db.session.add(r)
        db.session.commit()

class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=True)
    review = db.Column(db.Text, nullable=True)
    username = db.Column(db.String, nullable=True)
    source = db.Column(db.String, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    review_id = db.Column(db.Integer, db. ForeignKey("books.id"), nullable=False)

    def __repr__(self):
        return '<Review {}>'.format(self.review)
