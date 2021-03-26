from app import app
from models import db

db.drop_all()
db.create_all()

# must have psql database named RE_CRM to work
# use command python seed.py while in backend directory to populate tables