#create token
#crete booking id
#update booking id - BookingID, Token
#delete booking id - BookingID, Token
import logging

#verifying that Create Booking ID when we update we are able to update it and delete it

#create token
#crete booking id
#test_update()
#fixtures --> pass the data in pytest

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.util.utils import Util
from src.helpers.payload import *

class TestCRUDBooking:



    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self,create_token,get_booking_id):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_request(
            url=put_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        logger.info("Request is sent"+str(response.text))
        # verify_json_key_for_not_null(response.json()["firstname"])
        # verify_json_key_for_not_null(response.json()["lastname"])
        verfiy_http_status_code(response_data=response, expect_data=200)





    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description(
        "Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self,create_token,get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_request(
            url=delete_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verfiy_http_status_code(response_data=response, expect_data=201)