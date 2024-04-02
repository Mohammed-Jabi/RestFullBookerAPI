class Utils:
    def common_headers_json(self):
        headers = {
            'Content-Type': 'application/json',
        }
        return headers

    def common_headers_xml(self):
        headers = {
            'Content-Type': 'application/xml',
        }
        return headers

    def common_header_put_delete():
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YWRtaW46cGFzc3dvcmQxMjM='
        }
        return headers

    def common_header_put_delete(token):
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'token=' + str(token)
        }
        return headers