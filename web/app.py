from flask import Flask, jsonify, request

from web.database import Session
from web.models import ElementsToProcess

app = Flask(__name__)


@app.route('/show-elements', methods=['GET'])
def show_elements():
    with Session() as session:
        elements = session.query(ElementsToProcess).all()
    
    result = [el.__str__() for el in elements]
    return result


@app.route('/show-elements-with-default-status', methods=['GET'])
def show_elements_with_default_status(default_status: int = 60):
    with Session() as session:
        elements = session.query(ElementsToProcess).filter(ElementsToProcess.status == default_status)
    
    result = [el.__str__() for el in elements]
    return result


@app.route('/insert-element', methods=['POST'])
def insert_element(default_id_bulk: int = 0, default_retries: int = 0):
    data = request.get_json()
    if 'status' in data and 'name' in data:
        new_element = ElementsToProcess(
            idBulk = data.get('idBulk', default_id_bulk),
            retries = data.get('retries', default_retries),
            status = data.get('status'),
            name = data.get('name'),
        )
        
        with Session() as session:
            session.add(new_element)
            session.commit()

        response = 'Insert ok'
        response_status = 201

    else:
        response = 'Missing "name" or "status" in request'
        response_status = 400

    return response, response_status
