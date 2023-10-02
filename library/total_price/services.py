from library.extension import db
from library.library_ma import Total_priceSchema
from library.model import Total_price
from flask import request, jsonify, json

total_schema = Total_priceSchema()
totals_schema = Total_priceSchema(many=True)

def add_total_data_service():
    data = request.json
    if ( ('fall' in data)and ('SpO2' in data)):
        fall=data['fall']
        SpO2=data['SpO2']

        try:
            new_total_data = Total_price(fall,SpO2)
            db.session.add(new_total_data)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot add data", "error": str(e)}), 400
    else:
        return jsonify({"message": "Request error"}), 400
  

def get_all_total_data_service():
    totals_data = Total_price.query.all()
    if totals_data:
        return totals_schema.jsonify(totals_data)
    else : 
        return jsonify({"message": "Not found sensors_data!"})
    
def update_total_data_by_id_service(id):
    price = Total_price.query.get(id)
    if price:
        data = request.json
        if (data and ('fall' in data)and ('SpO2' in data)):
            try:
                price.fall=data['fall']
                price.SpO2=data['SpO2']
                db.session.commit()
                return jsonify({"message": "Updated successfully"})
            except Exception as e:
                db.session.rollback()
                return jsonify({"message": "Cannot update !", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found !"}), 404
    
def delete_total_data_by_id_service(id):
    price = Total_price.query.get(id)
    if price:
        try:
            db.session.delete(price)
            db.session.commit()
            return jsonify({"message": "Deleted successfully"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot Delete !", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found !"}), 404



