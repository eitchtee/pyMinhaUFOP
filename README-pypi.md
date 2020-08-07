# pyMinhaUFOP
Wrapper não-oficial para a API mobile da MinhaUFOP

**Veja mais detalhes no [Github](https://github.com/eitchtee/pyMinhaUFOP)**

---

## O que é?
Este wrapper expõe a API Mobile do Aplicativo [Minha UFOP](https://play.google.com/store/apps/details?id=br.ufop.app).

## Instalação


#### Automático (recomendado)

```
$ pip install pyminhaufop --upgrade
```

#### Manual

1. Clone este repositório
2. ```$ python setup.py install```

<br/>

> Lembre-se de manter a biblioteca sempre atuaizada.

## Uso e Exemplos

### Login
#### simples
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

#### com senha hasheada
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

#### utilizando conta com mais de um perfil
```python
from pyminhaufop import MinhaUFOP

# inicializa a classe
api = MinhaUFOP()

# Você pode passar os dados de forma direta
# identificacao = matrícula com pontos
# perfil = 
#        - "G" - Alunos de Graduação
api.login('123.456.789-10', 'sua_senha', identificacao="20.1.0000", perfil="G")

# ou 

# Indique o index do perfil. O mais recente é o index 0.
api.login('123.456.789-10', 'sua_senha', perfil_num=0)
```

### RU
#### Saldo
```python
saldo = api.saldo_do_ru()

print(saldo)
# >> {'cpf': '123.456-789-10', 'saldo': 1.0, 'bloqueado': False}
```

#### Cardápio
```python

# Acessar cardápio da semana
cardapio = api.cardapio_do_ru()

# Acessar cardápio de um dia específico na semana
# dia_da_semana: int =
#                      - 0 = Segunda
#                      - ...
#                      - 4 = Sexta
cardapio = api.cardapio_do_ru(dia_da_semana=0)

print(cardapio)
# >> [{'almoco': {'opma': [ ... }]
```

### Salvar foto de um CPF
```python
# Salva a foto do CPF como teste.png
api.foto('123.456.789-10', 'teste.png')

# Salva a foto e etorna o caminho onde foi salva
foto = api.foto('123.456.789-10')
print(foto)
# 123.456.789-10.png
```