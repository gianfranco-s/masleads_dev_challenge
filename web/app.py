from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/show-elements', methods=['GET'])
def show_elements():
    mock_db = ({
        'id': 1,
        'idBulk': 1,
        'retries': 0,
        'status': 20,
        'name': 'Element 1',
    },
    {
        'id': 2,
        'idBulk': 1,
        'retries': 1,
        'status': 20,
        'name': 'Element 2',
    })
    return jsonify(mock_db)


@app.route('/show-elements-with-default-status', methods=['GET'])
def show_elements_with_default_status(default_status: int = 60):
    mock_db = ({
        'id': 1,
        'idBulk': 1,
        'retries': 0,
        'status': 20,
        'name': 'Element 1',
    },
    {
        'id': 2,
        'idBulk': 1,
        'retries': 1,
        'status': 60,
        'name': 'Element 60',
    })

    result = [el for el in mock_db if el.get('status') == default_status]
    return jsonify(result)


@app.route('/insert-element', methods=['POST'])
def insert_element(default_id_bulk: int = 0, default_retries: int = 0):
    data = request.get_json()
    if 'status' in data and 'name' in data:
        new_element = {
            'idBulk': data.get('idBulk', default_id_bulk),
            'retries': data.get('retries', default_retries),
            'status': data.get('status'),
            'name': data.get('name'),
        }
        # Insert to db

        response = 'Insert ok'
        response_status = 201

    else:
        response = 'Missing "name" or "status" in request'
        response_status = 400

    return response, response_status
