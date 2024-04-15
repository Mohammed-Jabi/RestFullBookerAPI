# Read the CSV or EXCEL file
# Create a Function create_token which can take values from the Excel File
# Verify the Expected Result.

# Read the Excel - openpyxl
import openpyxl
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload import payload_create_token, payload_create_booking
from src.util.utils import Util
from conftest import read_credentials_from_excel


# def read_credentials_from_excel(file_path):
#     credentials = []
#     workbook = openpyxl.load_workbook(filename=file_path)
#     sheet = workbook.active
#     for row in sheet.iter_rows(min_row=2, values_only=True):
#         username, password = row
#         credentials.append(({
#             "username": username,
#             "password": password
#         }))
#     return credentials

    # @pytest.fixture()
    # def create_token(self):
    #     response = post_request(
    #         url=APIConstants.url_create_token(),
    #         headers=Util().common_headers_json(),
    #         auth=None,
    #         payload=payload_create_token(),
    #         in_json=False
    #     )
    #     verfiy_http_status_code(response_data=response, expect_data=200)
    #     verify_json_key_for_not_null_token(response.json()["token"])
    #     return response.json()["token"]
    #
    # @pytest.fixture()
    # def get_booking_id(self):
    #     response = post_request(url=APIConstants.url_create_booking(),
    #                             auth=None,
    #                             headers=Util().common_headers_json(),
    #                             payload=payload_create_booking(),
    #                             in_json=False)
    #
    #     booking_id = response.json()["bookingid"]
    #
    #     verfiy_http_status_code(response_data=response, expect_data=200)
    #     verify_json_key_for_not_null(booking_id)
    #     return booking_id
    # return credentials


def create_auth_request(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = post_request(
        url=APIConstants.url_create_token(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload,
        in_json=False
    )
    return response


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(
    "/home/jabir/APIAutomation/tests/test/datadriventesting/testdata_ddt_123.xlsx"))
def test_create_auth_with_excel(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = create_auth_request(username=username, password=password)
    print(response.status_code)