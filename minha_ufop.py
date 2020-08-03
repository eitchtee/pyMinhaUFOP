import hashlib
import requests


class MinhaUFOP:
    def __init__(self):
        self.token = None

    def login(self,
              usuario: str = None,
              senha: str = None,
              encode: bool = True):

        if encode:
            senha = hashlib.md5(senha.encode()).hexdigest()

        url = "https://zeppelin10.ufop.br/minhaUfop/v1/auth/login"

        payload = f"{{\"identificador\":\"{usuario}\"," \
                  f"\"senha\":\"{senha}\"," \
                  "\"identificacao\":\"\",\"perfil\":\"\",\"crypt\":true," \
                  "\"chave\":\"e8c8f5ef-4248-4e81-9cb9-4ab910080485\"}"

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response)

        if response.ok:
            self.token = response.json()['token']
        else:
            raise Exception("Login mal sucedido. Verifique seu usuário e senha.")
