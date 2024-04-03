def verfiy_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data , f"Expected status code is {expected_data} but found {response_data.status_code}"

def verify_json_key_for_not_null(key):
    assert key !=0 , "Key is not Empty" + key
    assert key > 0 , "Key is greater than zero" + key

def verify_response_key_should_not_be_non(key):
    assert key is not None
