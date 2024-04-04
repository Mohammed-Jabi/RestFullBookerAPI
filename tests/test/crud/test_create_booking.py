import allure
import pytest

from src.constants.api_constants import ApiConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.util.utils import Utils
from src.helpers.payload import *


class TestCreateBooking:
    # @pytest.mark.positive
    @allure.title("Verifying that Create Booking ID and Booking Status should not be empty")
    @allure.description("Create booking")
    def test_create_booking_positive(self):
        payload = payload_create_booking()
        response = post_request(url = ApiConstants.url_create_booking(),
                                auth = None,
                                headers = Utils().common_headers_json(),
                                payload = payload,
                                in_json = False)
        booking_id = response.json()["bookingid"]

        verfiy_http_status_code(response_data = response, expected_data = 200)
        verify_json_key_for_not_null(booking_id)

    # @pytest.mark.negative
    @allure.title("Verifying that Create Booking ID and Booking give 500 status cod if entered empty payload")
    @allure.description("Create booking")
    def test_create_booking_negative(self):
        # payload = payload_create_booking()
        response = post_request(url = ApiConstants.url_create_booking(),
                                auth = None,
                                headers = Utils().common_headers_json(),
                                payload = {},
                                in_json = False)

        verfiy_http_status_code(response_data = response, expected_data = 500)
