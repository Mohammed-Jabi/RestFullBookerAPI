# This file contains the constants used in the API tests
#keep the URLs

class ApiConstants:

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    #Update https method requires booking id
    @staticmethod
    def url_update_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(self.booking_id)