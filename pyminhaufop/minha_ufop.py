import hashlib
import requests


class MinhaUFOP:
    def __init__(self):
        self.token = None

    def login(self,
              usuario: str,
              senha: str,
              encode: bool = True,
              **kwargs) -> dict:
        """Gera o token necessáio para acessar a API simulando um login.

        Args:
            usuario (str):Seu cpf com pontos e hífens (ex.: 123.456.789-10)
            senha (str):Sua senha da MinhaUFOP, também pode ser um hash MD5
            da senha
            encode (bool):True se você estiver usando a senha pura, False se
             você estiver utilizando um hash MD5 da senha

        Kwargs:
            url (str): URL para fazer a requisição ao servidor
            headers (dict): Headers da requisição ao servidor
        """

        if encode:
            senha = hashlib.md5(senha.encode()).hexdigest()

        url = kwargs.get('url', "https://zeppelin10.ufop.br/minhaUfop/v1/auth/login")

        identificacao = kwargs.get('identificacao', '')
        perfil = kwargs.get('perfil', '')
        chave = kwargs.get('chave', "e8c8f5ef-4248-4e81-9cb9-4ab910080485")

        payload = f'{{"identificador":"{usuario}","senha":"{senha}","identificacao":"{identificacao}","perfil":"{perfil}","crypt":true,"chave":"{chave}"}}'
        headers = kwargs.get('headers', {'Content-Type': 'application/json'})
        response = requests.request("POST", url, headers=headers, data=payload)

        perfil_num = kwargs.get('perfil_num')

        if response.ok:
            res_json = response.json()

            if res_json.get("token"):
                self.token = res_json.get("token")
                return res_json
            elif res_json.get("perfil") and perfil_num:
                res = self.login(usuario, senha, encode=encode, identificacao=res_json['perfil'][perfil_num]['identificacao'], perfil=res_json['perfil'][perfil_num]['perfil'])
                return res_json
            elif res_json.get("perfil") and not perfil_num:
                return res_json
        else:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code) +
                            ". Verifique suas informações de login.")

    def saldo_do_ru(self, **kwargs) -> dict:
        """Retorna o CPF do usuário, o saldo do Cartão do RU e se o cartão está
           bloqueado

        Kwargs:
            url (str): URL para fazer a requisição ao servidor
            headers (dict): Headers da requisição ao servidor
        """

        url = kwargs.get('url', "https://zeppelin10.ufop.br/api/v1/ru/saldo")
        headers = kwargs.get('headers', {'Authorization': f'Bearer {self.token}'})

        response = requests.request("GET", url, headers=headers)

        if response.ok:
            return response.json()
        else:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code))

    def cardapio_do_ru(self, **kwargs) -> dict:
        """Retorna o cardapio do RU para a semana

        Kwargs:
            dia_da_semana (int): Retorna o cardápio para o dia da semana
            informado. 0 a 4, onde 0 é segunda e 4 é sexta.
            url (str): URL para fazer a requisição ao servidor
            headers (dict): Headers da requisição ao servidor
        """

        dia = kwargs.get('dia_da_semana')

        url = kwargs.get('url', "https://zeppelin10.ufop.br/api/v1/ru/cardapio")
        headers = kwargs.get('headers', {'Authorization': f'Bearer {self.token}'})

        response = requests.request("GET", url, headers=headers)

        if response.ok:
            if dia:
                return response.json()[dia]
            else:
                return response.json()
        else:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code))

    def extrato_ru(self, inicio, fim, **kwargs) -> dict:
        """Retorna o extrato da carteira do RU.

        Args:
            inicio (str): Data no formato YYYY-MM-DD HH:MM:SS
            fim (str): Data no formato YYYY-MM-DD HH:MM:SS

        Kwargs:
            url (str): URL para fazer a requisição ao servidor
            headers (dict): Headers da requisição ao servidor
        """

        url = kwargs.get('url',
                         f"https://zeppelin10.ufop.br/api/v1/ru/extrato?"
                         f"inicio={inicio}&fim={fim}")

        headers = kwargs.get('headers',
                             {'Authorization': f'Bearer {self.token}'})

        response = requests.request("GET", url, headers=headers)

        if response.ok:
            return response.json()
        else:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code))

    def atestado(self, **kwargs) -> dict:
        """Retorna as matérias do usuário em blocos de 50 minutos.

        Kwargs:
            url (str): URL para fazer a requisição ao servidor
            headers (dict): Headers da requisição ao servidor
        """

        url = kwargs.get('url',
                         f"https://zeppelin10.ufop.br/api/v1/graduacao/alunos/atestado")

        headers = kwargs.get('headers',
                             {'Authorization': f'Bearer {self.token}'})

        response = requests.request("GET", url, headers=headers)

        if response.ok:
            return response.json()
        else:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code))

    def foto(self, cpf: str, **kwargs) -> bytes:
        """Retorna a foto do CPF informado, se disponível.

        Args:
            cpf (str):CPF que você deseja requisitar a foto (ex.:
            123.456.789-10)

        Kwargs:
            url (str): URL para fazer a requisição ao servidor
            headers (dict): Headers da requisição ao servidor
        """

        url = kwargs.get('url', f"https://zeppelin10.ufop.br/api/v1/ru/foto/{cpf}")
        headers = kwargs.get('headers', {'Authorization': f'Bearer {self.token}'})

        response = requests.request("GET", url, headers=headers)

        if response.ok and response.content:
            return response.content
        elif not response.content:
            raise Exception("Servidor não retornou nada. "
                            "Verifique o CPF do pedido.")
        elif not response.ok:
            raise Exception("Servidor retornou o código: " +
                            str(response.status_code))
