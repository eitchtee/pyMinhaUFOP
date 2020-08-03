import hashlib
import requests


class MinhaUFOP:
    def __init__(self):
        self.token = None

    def login(self,
              usuario: str,
              senha: str,
              encode: bool = True) -> None:
        """
            Gera o token necessáio para acessar a API simulando um login.

            Parameters:
                usuario (str):Seu cpf com pontos e hífens (ex.: 123.456.789-10)
                senha (str):Sua senha da MinhaUFOP, também pode ser um hash MD5
                da senha
                encode (bool):True se você estiver usando a senha pura, False se
                 você estiver utilizando um hash MD5 da senha
        """

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
        res_json = response.json()

        if response.ok:
            try:
                self.token = res_json['token']
            except KeyError:
                if res_json.get("perfil", False):
                    raise Exception("Mais de um perfil encontrado. "
                                    "Use o metódo multi_perfil_login() "
                                    "para logar.")
                else:
                    raise Exception("Erro desconhecido.")
        else:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code) +
                            ". Verifique suas informações de login.")

    def multi_perfil_login(self, usuario: str,
                           senha: str,
                           perfil: int = 0,
                           encode: bool = True):
        """
                    Gera o token necessáio para acessar a API simulando um
                    login.

                    Parameters:
                        usuario (str):Seu cpf com pontos e hífens (ex.:
                        123.456.789-10)
                        senha (str):Sua senha da MinhaUFOP, também pode ser
                        um hash MD5 da senha
                        perfil (int):O número do perfil que você deseja usar,
                         do mais recente ao mais antigo. Começa no 0.
                        encode (bool):True se você estiver usando a senha
                        pura, False se
                         você estiver utilizando um hash MD5 da senha
                """

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

        if response.ok:
            perfis = response.json()['perfil']
        else:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code) +
                            ". Verifique suas informações de login.")

        if perfil >= len(perfis):
            raise Exception(f"Número do perfil especificado [{perfil}] "
                            f"maior do que o número de perfis disponíveis.")
        if perfil < 0:
            raise Exception(f"Número do perfil especificado [{perfil}] "
                            f"é inválido.")

        url = "https://zeppelin10.ufop.br/minhaUfop/v1/auth/login"

        payload = f"{{\"identificador\":\"{usuario}\"," \
                  f"\"senha\":\"{senha}\"," \
                  f"\"identificacao\":\"{perfis[perfil]['identificacao']}\",\"perfil\":\"{perfis[perfil]['perfil']}\",\"crypt\":true," \
                  "\"chave\":\"e8c8f5ef-4248-4e81-9cb9-4ab910080485\"}"

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.ok:
            self.token = response.json()['token']
        else:
            raise Exception("Servidor retornou: " + str(response.status_code))

    def saldo_do_ru(self):
        """Retorna um dicionário com o CPF do usuário, o saldo do seu Cartão do
        RU e se o cartão está bloqueado"""

        url = "https://zeppelin10.ufop.br/api/v1/ru/saldo"

        headers = {
            'Authorization': f'Bearer {self.token}',
        }

        response = requests.request("GET", url, headers=headers)

        return response.json()

    def foto(self, cpf: str, caminho_de_saida = None):
        """Salva a foto do CPF informado se disponível.

        Parameters:
            cpf (str):CPF que você deseja requisitar a foto (ex.:
            123.456.789-10)
            caminho_de_saida (str):Caminho para salvar a foto.
             Padrão é {cpf}.png
        """

        url = "https://zeppelin10.ufop.br/api/v1/ru/foto/" + str(cpf)

        headers = {
            'Authorization': f'Bearer {self.token}',
        }

        response = requests.request("GET", url, headers=headers)

        saida = cpf + ".png" if not caminho_de_saida else caminho_de_saida

        if response.ok and response.content:
            with open(saida, 'wb') as file:
                file.write(response.content)
        elif not response.content:
            raise Exception("Servidor não retornou nada. "
                            "Verifique o CPF do pedido.")
        elif not response.ok:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code))

