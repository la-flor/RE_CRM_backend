from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Seller(db.Model):
    """Seller information"""

    __tablename__ = "sellers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first = db.Column(db.Text, nullable=False)
    last = db.Column(db.Text, nullable=False)
    email = db.Column(db.VARCHAR(320), unique=True, nullable=False)
    phone = db.Column(db.VARCHAR, nullable=False)

class Lead(db.Model):
    """Lead information"""

    __tablename__ = "leads"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.VARCHAR(320), nullable=False)
    city = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    zipcode = db.Column(db.Integer(), nullable=False)

class Seller_Lead(db.Model):
    """Connection between sellers and properties/leads they might sell"""

    __tablename__ = "sellers_leads"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey("sellers.id"))
    lead_id = db.Column(db.Integer, db.ForeignKey("leads.id"))

def connect_db(app):
    """Connect this database to provide Flask app."""

    db.app = app
    db.init_app(app)