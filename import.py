import os
import csv

from flask import Flask, render_template, request
from app.models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+pg8000://Feeva:password@localhost:5432/bookreview'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        book = Book(isbn=isbn, title=title, author=author, year=year, review_count=0, avg_score=0)
        db.session.add(book)
        print(f"Added Title: {title} to database")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
