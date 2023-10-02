from library.extension import db
from flask_jwt_extended import get_jwt_identity
class Total_price(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fall = db.Column(db.String(50),nullable = False)
    SpO2 = db.Column(db.String(50),nullable = False)

    def __init__(self,fall,SpO2):
        self.fall=fall 
        self.SpO2=SpO2

