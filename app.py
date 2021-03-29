from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, connect_db, Seller, Lead, Seller_Lead
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY", "secret key should be in environment"
)

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
# ^^ replacement for below due to new breaking change in psql from postgres to postgresql and heroku's delayed update
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///RE_CRM')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
connect_db(app)

@app.route("/new_lead", methods=["POST"])
def new_lead():
    """New lead submission accepted and added to database."""
    
    data = request.get_json()

    # new seller input data
    first = data["first"]
    last = data["last"]
    phone = data["phone"]
    email = data["email"]

    # new address input data
    address = data["address"]
    city = data["city"]
    state = data["state"]
    zipcode = data["zipcode"]

    # checking to see if the property is already present in our database
    if len(Lead.query.filter_by(address=address).all()) > 0:
        return jsonify({"errors": ["This property address has already been submitted."]})

    try:
        # if the seller is not already in the database, lets add them in
        if not len(Seller.query.filter_by(email=email).all()):
            new_seller = Seller(first=first, last=last, phone=phone, email=email)
            db.session.add(new_seller)

        # create the new property lead for our database
        new_lead = Lead(address=address, city=city, state=state, zipcode=zipcode)
        db.session.add(new_lead)

        db.session.commit()

        # add connection between seller and lead
        db_seller = Seller.query.filter_by(email=email).first()
        db_lead = Lead.query.filter_by(address=address, city=city).first()
        seller_lead_connection = Seller_Lead(seller_id=db_seller.id, lead_id=db_lead.id)
        db.session.add(seller_lead_connection)
        db.session.commit()

        return jsonify(data)
    except:
        return jsonify({"errors": ["We were unable to process the request.  Make sure all information is correct."]})