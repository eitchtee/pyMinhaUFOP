# pyMinhaUFOP
Wrapper não-oficial para a API mobile da MinhaUFOP

## O que é?
Este wrapper expõe a API Mobile do Aplicativo [Minha UFOP](https://play.google.com/store/apps/details?id=br.ufop.app).

## Instalação
`pip install pyminhaufop`

## Uso
#### Login simples
```python
from pyminhaufop import MinhaUFOP

# inicializa a classe
api = MinhaUFOP()

# Logue e gere o token
api.login('123.456.789-10', 'sua_senha')

# acesse as funções da API
saldo = api.saldo_do_ru()
print(saldo['saldo'])
```

#### Login com senha hasheada
```python
from pyminhaufop import MinhaUFOP

# inicializa a classe
api = MinhaUFOP()

# Logue usando uma senha hasheada em MD5
api.login('123.456.789-10', 'sua_senha_em_MD5', encode=False)

# acesse as funções da API
saldo = api.saldo_do_ru()
print(saldo['saldo'])
```

#### Login com mais de um perfil
```python
from pyminhaufop import MinhaUFOP

# inicializa a classe
api = MinhaUFOP()

# Logue e selecione um dos perfis. Mais recente primeiro.
api.multi_perfil_login('123.456.789-10', 'sua_senha_em_MD5', perfil=0)

# acesse as funções da API
saldo = api.saldo_do_ru()
print(saldo['saldo'])
```

#### Salvar foto de um CPF
```python
# Salva a foto do CPF como teste.png
api.foto('123.456.789-10', 'teste.png')

# Salva a foto e etorna o caminho onde foi salva
foto = api.foto('123.456.789-10')
print(foto)
# 123.456.789-10.png
```