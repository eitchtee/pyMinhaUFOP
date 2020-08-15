from requests import Response


class MinhaUFOPGenericError(Exception):
    def __init__(self, response: Response, msg):
        self.url = response.url
        self.status_code = response.status_code
        self.response = response
        self.msg = msg

        super().__init__(self.msg)
