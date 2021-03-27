from app import app
import json
from unittest import TestCase
from models import db

app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True

class FlaskAppTestCase(TestCase):
    """Test for route requests"""

    def setUp(self):
        """Clear all data and setup database for database info to be tested"""
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """Clean up fouled transactions."""

        db.session.rollback()
    
    def test_new_lead(self):
        """Test new lead submission"""
        test_lead = {
            "first": "Jose",
            "last": "Cuervo",
            "email": "jc@gmail.com",
            "phone": "9199098976",
            "address": "123 Testing Lane",
            "city": "Margaritaville",
            "state": "California",
            "zipcode": "90210"
        }

        with app.test_client() as client:
            resp = client.post(
                '/new_lead',
                data=json.dumps(test_lead),
                content_type='application/json')

            response_body = json.loads(resp.data)

            assert resp.status_code == 200
            assert response_body["first"] == "Jose"
            assert response_body["email"] == "jc@gmail.com"
            assert response_body["state"] == "California"
            assert response_body["zipcode"] == "90210"