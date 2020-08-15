from requests import Response


class MinhaUFOPHTTPError(Exception):
    def __init__(self, response: Response):
        self.url = response.url
        self.status_code = response.status_code
        self.response = response

        super().__init__(f'O servidor retornou o código {self.status_code}')
