import json

from web.app import app
from web.tests import HEADERS


def test_basic_auth_with_valid_cretentials():
    response = app.test_client().get('/show-elements', headers=HEADERS)
    assert response.status_code == 200


def test_basic_auth_with_invalid_cretentials():
    response = app.test_client().get('/show-elements', headers=None)
    assert response.status_code == 401


def test_show_elements():
    response = app.test_client().get('/show-elements', headers=HEADERS)
    data = json.loads(response.data.decode('utf-8'))
    test_elements = (
        {
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
        }
    )
    
    assert response.status_code == 200
    for el in test_elements:
        assert el in data



def test_show_elements_with_default_status(default_status=60):
    response = app.test_client().get('/show-elements-with-default-status', headers=HEADERS)
    data = json.loads(response.data.decode('utf-8'))
    
    assert response.status_code == 200
    for el in data:
        assert el.get('status') == default_status


def test_insert_element_with_all_mandatory_values():
    test_insert_element = {
        'status': 999,
        'name': 'Test insert element'
    }
    response = app.test_client().get('/insert-element', 
                                     headers=HEADERS,
                                     content_type='application/json',
                                     data=json.dumps(test_insert_element))
    
    assert response.status_code == 201
    assert 'Insert ok' in response.data.decode('utf-8')


def test_insert_element_with_missing_name():
    test_insert_element = {
        'status': 999
    }
    response = app.test_client().get('/insert-element', 
                                     headers=HEADERS,
                                     content_type='application/json',
                                     data=json.dumps(test_insert_element))
    
    assert response.status_code == 400


def test_insert_element_with_all_values():
    test_insert_element = {
        'status': 999,
        'name': 'Test insert full element',
        'retries': 99,
        'idBulk': 9999
    }
    response = app.test_client().get('/insert-element', 
                                     headers=HEADERS,
                                     content_type='application/json',
                                     data=json.dumps(test_insert_element))
    
    assert response.status_code == 201
    assert 'Insert ok' in response.data.decode('utf-8')
