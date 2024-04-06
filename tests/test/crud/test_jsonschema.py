#Get the response
#Create the Json Schema from http://jsonschema.net/
#Save the schema into the name.json file
import os

from jsonschema import validate

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.util.utils import Util
from src.helpers.payload import *

class TestCreateBookingJSONSchema:

    def load_schema(self, file_name):
        with open(file_name, "r") as file:
            return json.load(file)

    # @pytest.mark.positive
    @allure.title("Verifying that Create Booking ID and Booking Status should not be empty")
    @allure.description("Create booking")
    def test_create_booking_positive(self):
        payload = payload_create_booking()
        response = post_request(url = APIConstants.url_create_booking(),
                                auth = None,
                                headers = Util().common_headers_json(),
                                payload = payload,
                                in_json = False)
        booking_id = response.json()["bookingid"]

        verfiy_http_status_code(response_data = response, expect_data = 200)
        verify_json_key_for_not_null(booking_id)

        #response with schema json validation
        #file_path = "/home/jabir/APIAutomation/tests/test/crud/create_schema.json"
        file_path = os.getcwd()+"/create_schema.json"
        schema = self.load_schema(file_path)
        try:
            validate(instance=response.json(), schema=schema)
        except Exception as e:
            print(e)

